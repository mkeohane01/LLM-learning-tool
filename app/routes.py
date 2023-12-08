from app import app
from flask import render_template, request
from app.utils import prompt_llm


@app.route('/')
def prompt_engineering():
    '''
    This function is called when the user visits the root URL of the website.
    It renders the template 'prompt_engineering.html'
    '''
    return render_template('prompt_engineering.html')

@app.route('/results', methods=['POST'])
def submit_prompt():
    '''
    This function is called when the user submits the form on the page
    'prompt_engineering.html'. It renders the template 'results.html' with the
    results of the prompt generation.
    '''
    role = request.form.get('role')
    context = request.form.get('context')
    style = request.form.get('style')
    task = request.form.get('task')
    constraints = request.form.get('constraints')

    # Query GPT
    prompt, response = prompt_llm(role, context, style, task, constraints)

    return render_template('results.html', result={
        'prompt': prompt,
        'response': response
    })
