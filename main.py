import sys
import requests
import logging
from decouple import Config
from decouple import UndefinedValueError

logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger()

try:
    config = Config('.env')
    AUTH_TOKEN = config.get("MY_TOKEN")
    if len(AUTH_TOKEN) == 0:
        raise ValueError("Please update your .env file with your Cobalt Auth Token, if running this script locally.")
    ORG_TOKEN = config.get("ORG_TOKEN")
    if len(ORG_TOKEN) == 0:
        raise ValueError("Please run get_org_token() to get the token and then update the .env file.")
except UndefinedValueError:
    # Doing this for Jenkins
    logger.error("Unable to find environment variables, please provide them via command line arguments.")
    AUTH_TOKEN = sys.argv[1]
    ORG_TOKEN = sys.argv[2]

STARTING_YEAR = '2023'
EXCLUDED_PEN_TESTS = ['List of Cobalt Pen Tests to exclude']

pen_test_dictionary = {}

headers = {
    'Accept': 'application/vnd.cobalt.v2+json',
    'Authorization': 'Bearer %s' % AUTH_TOKEN,
    'X-Org-Token': ORG_TOKEN,
}

def get_org_token():
    response = requests.get('https://api.cobalt.io/orgs', headers=headers)
    if response.status_code == 200:
        logger.info('Successfully fetched org token.')
        logger.info(response.text)
    else:
        logger.error(f"Failed to fetch org token. HTTP {response.status_code}: {response.reason}")

def get_this_years_active_pen_tests():
    response = requests.get('https://api.cobalt.io/pentests?start_date_gte=%s-01-01&limit=30' % STARTING_YEAR, headers=headers)
    if response.status_code == 200:
        logger.info('Successfully fetched active pen tests.')
        for item in response.json()["data"]:
            resource_data = item.get("resource", {})
            item_title = resource_data.get("title", "")
            item_id = resource_data.get("id", "")
            if item_title not in EXCLUDED_PEN_TESTS:
                pen_test_dictionary[item_title] = item_id

        logger.info('**********************************************************************')
        logger.info('Current Pen Test in Non-Closed Status:')
        for key, value in pen_test_dictionary.items():
            logger.info(f"{key}: {value}")

        logger.info(f'\nTotal amount of open pen tests: {len(pen_test_dictionary)}')

    else:
        logger.error(f"Failed to fetch active pen tests. HTTP {response.status_code}: {response.reason}")

def print_report():
    global_issues_reported = 0
    global_issues_remaining = 0
    any_successful_report = False

    for pen_test_title, pen_test_id in pen_test_dictionary.items():
        response = requests.get(f'https://api.cobalt.io/pentests/{pen_test_id}/report', headers=headers)

        if response.status_code == 200:
            any_successful_report = True
            json_data = response.json()["data"]
            logger.info(f'\n**********************************************************************')
            logger.info(f'Pen Test: {pen_test_title}')

            logger.info('\nTotal Reported Issues')
            crit_len = len(json_data['resource']['findings']['severity']['critical'])
            logger.info(f'Critical: {crit_len}')

            high_len = len(json_data['resource']['findings']['severity']['high'])
            logger.info(f'High: {high_len}')

            med_len = len(json_data['resource']['findings']['severity']['medium'])
            logger.info(f'Medium: {med_len}')

            low_len = len(json_data['resource']['findings']['severity']['low'])
            logger.info(f'Low: {low_len}')

            info_len = len(json_data['resource']['findings']['severity']['informational'])
            logger.info(f'Informational: {info_len}')

            total_reported_len = info_len + low_len + med_len + high_len + crit_len
            logger.info(f'Total: {total_reported_len}')
            global_issues_reported += total_reported_len

            # Remaining Issues
            logger.info('\nTotal Remaining Issues')
            need_len = len(json_data['resource']['findings']['state']['need_fix'])
            logger.info(f'Status - Need Fix: {need_len}')

            wont_len = len(json_data['resource']['findings']['state']['wont_fix'])
            logger.info(f'Status - Won\'t Fix: {wont_len}')

            check_len = len(json_data['resource']['findings']['state']['check_fix'])
            logger.info(f'Status - Check Fix: {check_len}')

            total_remaining_len = need_len + wont_len + check_len
            logger.info(f'Total: {total_remaining_len}')
            global_issues_remaining += total_remaining_len
        else:
            logger.error(f"Failed to fetch report for pen test {pen_test_title}. HTTP {response.status_code}: {response.reason}")

    if any_successful_report:
        logger.info(f'**********************************************************************')
        logger.info(f'Total reported issues (across all pen tests): {global_issues_reported}')
        logger.info(f'Total remaining issues (across all pen tests): {global_issues_remaining}')
        if global_issues_reported > 0:
            remediation_percentage = 100 - round(global_issues_remaining / global_issues_reported * 100)
            logger.info(f'Percentage of remediated issues: {remediation_percentage}%')
        else:
            logger.warning('No reported issues found, unable to calculate remediation percentage.')
        logger.info(f'**********************************************************************\n')
    else:
        logger.warning('No reports were successfully fetched.')

if __name__ == '__main__':
    # If you are running this for the first time, you need the Org Token.
    # Uncomment the following function to get a print out of the Org Token.
    # get_org_token()

    get_this_years_active_pen_tests()
    print_report()
