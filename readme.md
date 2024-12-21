<!DOCTYPE html>
<html>
<body>
    <h1>Setup and Run</h1>
    <h2>Creating a Virtual Environment</h2>
    <ol>
        <li><strong>Create a New Virtual Environment:</strong>
            <ul>
                <li>On Windows:
                    <code>python -m venv venv</code>
                </li>
                <li>On macOS and Linux:
                    <code>python3 -m venv venv</code>
                </li>
            </ul>
        </li>
        <li><strong>Activate Your Virtual Environment:</strong>
            <ul>
                <li>On Windows:
                    <code>venv\Scripts\activate</code>
                </li>
                <li>On macOS and Linux:
                    <code>source venv/bin/activate</code>
                </li>
            </ul>
        </li>
    </ol>
    <h2>Installing Packages</h2>
    <ol>
        <li><strong>Generate venv_packages.txt Using `pip freeze`:</strong>
            <ul>
                <li>Run: <code>pip freeze > venv_packages.txt</code></li>
                <li>This command generates a list of installed packages and versions and saves it in the venv_packages.txt file.</li>
            </ul>
        </li>
        <li><strong>Install Packages from the venv_packages.txt File:</strong>
            <ul>
                <li>Run: <code>pip install -r venv_packages.txt</code></li>
            </ul>
        </li>
        <li><strong>Verify Installed Packages:</strong>
            <ul>
                <li>Run: <code>pip list</code></li>
            </ul>
        </li>
    </ol>
    <h2>Updating the .env File</h2>
    <ol>
        <li><strong>Edit the .env File:</strong>
            <ul>
                <li>Open your backup.env file in a text editor.</li>
                <li>Add or update key-value pairs as needed.</li>
                <li>Rename 'backup.env' to '.env'.</li>
            </ul>
        </li>
    </ol>
    <h2>Running main.py</h2>
    <ol>
        <li><strong>Activate Your Virtual Environment:</strong>
            <ul>
                <li>On Windows:
                    <code>venv\Scripts\activate</code>
                </li>
                <li>On macOS and Linux:
                    <code>source venv/bin/activate</code>
                </li>
            </ul>
        </li>
        <li><strong>Navigate to the Directory Containing main.py</strong></li>
        <li><strong>Run main.py:</strong>
            <ul>
                <li>Execute: <code>python main.py</code></li>
            </ul>
        </li>
        <li><strong>Deactivate the Virtual Environment (Optional):</strong>
            <ul>
                <li>Run: <code>deactivate</code></li>
            </ul>
        </li>
    </ol>
</body>
</html>
