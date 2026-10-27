# Student Management API

A Django REST Framework project for managing student records through
REST API endpoints.

> **Project status:** The Django configuration check has passed. The
> MySQL connection and API endpoints still need to be tested end to end,
> so this README does not claim that database/API testing is complete.

## Features

-   Django-based project structure
-   Django REST Framework for building REST APIs
-   Student model, serializer, and `ModelViewSet`
-   Router-based API URL configuration
-   MySQL database configuration through environment variables
-   Git ignore rules for local database files, virtual environments, and
    secrets

## Tech Stack

-   Python
-   Django
-   Django REST Framework
-   MySQL / MariaDB (configured; connection verification pending)
-   Git and GitHub

## Project Structure

``` text
student_mgt_api/
├── manage.py
├── studentapi/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── students/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── ...
├── .gitignore
└── README.md
```

## Setup on Windows

### 1. Clone the repository

``` cmd
git clone https://github.com/Sakshi-tech347/student_mgt_api.git
cd student_mgt_api
```

If you want the feature branch currently used for development:

``` cmd
git checkout feature/new-student-management-system
```

### 2. Create and activate a virtual environment

``` cmd
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install dependencies

If a `requirements.txt` file exists in the repository:

``` cmd
python -m pip install -r requirements.txt
```

If the project does not yet have a `requirements.txt`, install the core
packages in the active virtual environment:

``` cmd
python -m pip install django djangorestframework mysqlclient
```

> `mysqlclient` may require additional setup on Windows depending on
> your Python version and installed build tools.

### 4. Configure the database

Start MySQL/MariaDB using your local database service (for example,
XAMPP). Create a database named `student_management_db` if it does not
already exist.

The project settings read these environment variables:

-   `DB_NAME` --- defaults to `student_management_db`
-   `DB_USER` --- defaults to `root`
-   `DB_PASSWORD` --- defaults to an empty password
-   `DB_HOST` --- defaults to `127.0.0.1`
-   `DB_PORT` --- defaults to `3307` in the current settings

Set values that match your local database configuration. For example, in
Windows Command Prompt for the current terminal session:

``` cmd
set DB_NAME=student_management_db
set DB_USER=root
set DB_PASSWORD=your_local_database_password
set DB_HOST=127.0.0.1
set DB_PORT=3306
```

Replace the example password and port with your own local settings. Do
not commit real passwords or secret keys to GitHub. The default port in
the current project settings is `3307`; verify the port used by your
database before running migrations.

### 5. Check Django configuration

``` cmd
python manage.py check
```

The check previously completed successfully with
`System check identified no issues (0 silenced)`.

### 6. Apply migrations

After confirming that the database connection settings are correct:

``` cmd
python manage.py makemigrations
python manage.py migrate
```

If `makemigrations` reports that no model changes are detected, continue
with `migrate`. Resolve any database connection errors before
proceeding.

### 7. Run the development server

``` cmd
python manage.py runserver
```

The development server normally runs at `http://127.0.0.1:8000/`.

## API Routes

The project includes the student routes under the `/api/` prefix and
uses a DRF router for `StudentViewSet`.

After starting the server, check the router configuration in
`students/urls.py` to confirm the exact registered endpoint. If the
router registers `students`, the collection endpoint will normally be:

``` text
http://127.0.0.1:8000/api/students/
```

The exact route and supported methods should be verified against the
current URL configuration and by testing the API.

## Current Validation

-   [x] `python manage.py check` passed
-   [x] Project changes pushed to the
    `feature/new-student-management-system` branch
-   [ ] Verify MySQL connection
-   [ ] Verify migrations against MySQL
-   [ ] Test student API create, list, retrieve, update, and delete
    operations
-   [ ] Add a `requirements.txt` with the project's verified
    dependencies

## GitHub

Repository: https://github.com/Sakshi-tech347/student_mgt_api

Development branch: `feature/new-student-management-system`

## Future Improvements

-   Add API request/response examples
-   Add automated tests
-   Add input validation and consistent error responses
-   Document verified endpoints with screenshots or sample requests
-   Prepare deployment settings with `DEBUG=False` and environment-based
    secrets

## Author

Created as a Python/Django REST API portfolio project to practice
backend development.
