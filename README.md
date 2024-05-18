<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Project Name</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 20px;
        }
        h1 {
            font-size: 28px;
            margin-bottom: 20px;
        }
        h2 {
            font-size: 24px;
            margin-bottom: 15px;
        }
        h3 {
            font-size: 20px;
            margin-bottom: 10px;
        }
        code {
            background-color: #f4f4f4;
            padding: 5px;
            border-radius: 3px;
            font-family: monospace;
        }
        pre {
            background-color: #f4f4f4;
            padding: 10px;
            border-radius: 5px;
            overflow-x: auto;
        }
        pre code {
            background-color: transparent;
            padding: 0;
            border-radius: 0;
        }
        ul, ol {
            margin-bottom: 20px;
            padding-left: 20px;
        }
        li {
            margin-bottom: 5px;
        }
    </style>
</head>
<body>
    <h1>Project Name</h1>

    <p>This project is a Django application.</p>

    <h2>Setup Instructions</h2>

    <ol>
        <li><strong>Clone the Repository</strong></li>
        <pre><code>git clone https://github.com/your_username/project_name.git<br>cd project_name</code></pre>
        
        <li><strong>Set Up Virtual Environment</strong></li>
        <p>It's recommended to use a virtual environment to manage dependencies.</p>
        <pre><code>python3 -m venv venv</code></pre>
        <p>Activate the virtual environment:</p>
        <ul>
            <li><strong>On macOS/Linux:</strong></li>
            <pre><code>source venv/bin/activate</code></pre>

            <li><strong>On Windows:</strong></li>
            <pre><code>venv\Scripts\activate</code></pre>
        </ul>

        <li><strong>Install Required Packages</strong></li>
        <pre><code>pip install -r requirements.txt</code></pre>

        <li><strong>Perform Migrations</strong></li>
        <pre><code>python manage.py migrate</code></pre>

        <li><strong>Run the Development Server</strong></li>
        <pre><code>python manage.py runserver</code></pre>
        <p>The development server will start running at <code>http://localhost:8000/</code>.</p>
    </ol>

    <h2>System Requirements</h2>

    <ul>
        <li>Python 3.10</li>
    </ul>

</body>
</html>
