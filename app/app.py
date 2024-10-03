from flask import Flask, render_template, request, redirect, url_for

# In-memory storage for tasks
tasks = []

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return render_template('index.html', tasks=tasks)

    @app.route('/add', methods=['POST'])
    def add_task():
        task = request.form.get('task')
        if task:
            tasks.append(task)
        return redirect(url_for('index'))

    @app.route('/delete/<int:task_id>')
    def delete_task(task_id):
        if 0 <= task_id < len(tasks):
            tasks.pop(task_id)
        return redirect(url_for('index'))

    return app

# Only run the app if this script is executed directly
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
