from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory data store (replace with a database in a real-world scenario)
tasks = []

@app.route('/')
def index():
    """
    Display the home page with the list of tasks.
    """
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    """
    Add a new task to the list.
    """
    task = request.form.get('task')
    if task:
        tasks.append(task)
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    """
    Delete a task from the list.
    """
    if 0 <= task_id < len(tasks):
        del tasks[task_id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
