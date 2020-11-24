# Django ToDo List App
A simple todo list app.<br>
The hosted version can be found [HERE](https://powerful-reef-25565.herokuapp.com/).

## Functionality
The app has the following features:
- Create, update, and delete tasks.
- Create, update, and delete categories.
- Mark a task as complete, and move it to its own category.
- User authentication to access your own todo list and categories.
- <b><u>Coming soon:</u></b> Share a task with another user

## Tech Stack
Front-end: Django HTML Templates<br>
Back-end: Django<br>
Database: PostgreSQL<br>
Deployment: Docker & Heroku

## Development Installation
1. Clone this repo
2. Create a new virtual environment and install the packages from `requirements.txt`
3. Connect to your own postgresql database by providing a `DATABASE_URL` environment variable. Another option is to modify `./django_todo_list/settings.py` to add your local postgresql database settings (otherwise it will use the default sqlite3)
4. Run `python manage.py runserver`

## App Testing
Ensure the app is running by making a GET request to http://127.0.0.1:8000/ (you can change the port by providing an environment variable)

## Hosted Version
The latest version is deployed using Docker and hosted on Heroku. Check it out by clicking [HERE](https://powerful-reef-25565.herokuapp.com/).

## Usage
1. Sign up.
2. Add Task.
3. Start adding and managing tasks and categories as you wish.

## Notes
1. The Web App uses SSL encryption through HTTPS protocol to transfer input data.
2. Passwords are hashed by django once received by the backend.
3. Despite 1 and 2, I'd still recommend using a fake password to avoid any potential future attacks.
4. If you decided to create a category before creating a task after your first login, make sure you add a category called `Uncategorized`, otherwise the app will break (will fix this soon).
