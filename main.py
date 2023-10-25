import requests
from decouple import Config

config = Config('.env')
AUTH_TOKEN = config.get('MY_TOKEN')
ORG_TOKEN = config.get("ORG_TOKEN")
STARTING_YEAR = '2023'
PEN_TEST_DICTIONARY = {}
EXCLUDED_PEN_TESTS = ['Goal Based Internal - Professional Services - May 2023']

headers = {
    'Accept': 'application/vnd.cobalt.v2+json',
    'Authorization': 'Bearer %s' % AUTH_TOKEN,
    'X-Org-Token': ORG_TOKEN,
}


def get_org_token():
    response = requests.get('https://api.cobalt.io/orgs', headers=headers)
    print(response.text)


def get_this_years_active_pen_tests():
    response = requests.get('https://api.cobalt.io/pentests?start_date_gte=%s-01-01&limit=30' % STARTING_YEAR, headers=headers)
    # print(response.text)

    for item in response.json()["data"]:
        resource_data = item.get("resource", {})
        item_title = resource_data.get("title", "")
        item_id = resource_data.get("id", "")
        if item_title not in EXCLUDED_PEN_TESTS:
            PEN_TEST_DICTIONARY[item_title] = item_id

    # Print the dictionary of title:id pairs
    print('**********************************************************************')
    print('Current Pen Test in Non-Closed Status:')
    for key, value in PEN_TEST_DICTIONARY.items():
        print(f"{key}: {value}")

    print('\nTotal amount of open pen tests: %s' % len(PEN_TEST_DICTIONARY))


def print_report():
    for pen_test_title, pen_test_id in PEN_TEST_DICTIONARY.items():
        response = requests.get('https://api.cobalt.io/pentests/%s/report' % pen_test_id, headers=headers)

        if response.status_code == 200:
            json_data = response.json()["data"]
            print('\n**********************************************************************')
            print('Pen Test: %s' % pen_test_title)

            print('\nTotal Reported Issues')
            crit_len = len(json_data['resource']['findings']['severity']['critical'])
            print('Critical: %s' % crit_len)

            high_len = len(json_data['resource']['findings']['severity']['high'])
            print('High: %s' % high_len)

            med_len = len(json_data['resource']['findings']['severity']['medium'])
            print('Medium: %s' % med_len)

            low_len = len(json_data['resource']['findings']['severity']['low'])
            print('Low: %s' % low_len)

            info_len = len(json_data['resource']['findings']['severity']['informational'])
            print('Informational: %s' % info_len)

            total_len = info_len+low_len+med_len+high_len+crit_len
            print('Total: %s' % total_len)

            print('\nTotal Remaining Issues')
            need_len = len(json_data['resource']['findings']['state']['need_fix'])
            print('Status - Need Fix: %s' % need_len)

            wont_len = len(json_data['resource']['findings']['state']['wont_fix'])
            print('Status - Wont Fix: %s' % wont_len)

            check_len = len(json_data['resource']['findings']['state']['check_fix'])
            print('Status - Check Fix: %s' % check_len)

            total_state_len = need_len+wont_len+check_len
            print('Total: %s' % total_state_len)


if __name__ == '__main__':
    # If you are running this for the first time, you need the Org Token.
    # Uncomment the following function to get a print out of the Org Token.
    # get_org_token()

    get_this_years_active_pen_tests()
    print_report()
