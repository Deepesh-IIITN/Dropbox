# Project Name

This project is a Django application.

## Setup Instructions

Follow these steps to set up the project locally:

1. **Clone the Repository**
    ```bash
    git clone https://github.com/your_username/project_name.git
    cd project_name
    ```

2. **Set Up Virtual Environment**
    It's recommended to use a virtual environment to manage dependencies.
    ```bash
    python3 -m venv venv
    ```
    Activate the virtual environment:

    - **On macOS/Linux:**
        ```bash
        source venv/bin/activate
        ```

    - **On Windows:**
        ```bash
        venv\Scripts\activate
        ```

3. **Install Required Packages**
    ```bash
    pip install -r requirements.txt
    ```

4. **Perform Migrations**
    ```bash
    python manage.py migrate
    ```

5. **Run the Development Server**
    ```bash
    python manage.py runserver
    ```
    The development server will start running at `http://localhost:8000/`.

## System Requirements

- Python 3.10
