<!DOCTYPE html>
<html>
<body>
    <h1>How to Install Packages from venv_packages.txt and Run main.py</h1>
    <h2>Installing Packages</h2>
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
        <li><strong>Navigate to the Directory Containing venv_packages.txt</strong></li>
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
                <li>Open your .env file in a text editor.</li>
                <li>Add or update key-value pairs as needed.</li>
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
