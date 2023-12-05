from app import app
from flask import render_template, request


@app.route('/')
def prompt_engineering():
    return render_template('prompt_engineering.html')

@app.route('/results', methods=['POST'])
def submit_prompt():
    role = request.form.get('role')
    context = request.form.get('context')
    style = request.form.get('style')
    task = request.form.get('task')
    constraints = request.form.get('constraints')

    # Process the data as needed for your application

    return render_template('results.html', result={
        'role': role,
        'context': context,
        'style': style,
        'task': task,
        'constraints': constraints
    })
