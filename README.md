# Basic Web Application with Flask

Welcome to the Basic Web Application with Flask! This Python project provides a simple web application using the Flask framework. Users can view, add, and delete tasks through a basic web interface.

## How to Use

1. Run the script (`app.py`).
2. Access the web application at `http://127.0.0.1:5000/` in your browser.
3. Interact with the web interface to view, add, and delete tasks.

## Features

### Routes

- `/`: Home page displaying the list of tasks.
- `/add`: Endpoint to add a new task.
- `/delete/<int:task_id>`: Endpoint to delete a task.

### Functions

#### `index()`

- Renders the home page (`index.html`) with the list of tasks.

#### `add_task()`

- Adds a new task to the list when the user submits a form.

#### `delete_task(task_id)`

- Deletes a task from the list based on the specified task_id.

### Templates

- Use Jinja2 templating to dynamically render tasks in the HTML templates.

### Dependencies

- [Flask](https://pypi.org/project/Flask/): A micro web framework for Python.

## Running the Application

1. Install Flask: `pip install flask`.
2. Run the script: `python app.py`.
3. Access the web application at `http://127.0.0.1:5000/` in your browser.

## Author

Jeel patel
