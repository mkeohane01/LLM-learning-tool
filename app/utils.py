from openai import OpenAI
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()
try:
    client = OpenAI(api_key= os.getenv('OPENAI_API_KEY'))
except:
    print("Error: Please set your OpenAI API key in the .env file.")

def prompt_llm(role, context, style, task, constraints):
    '''
    This function takes in the user's input, queries the GPT-3.5 API, and 
    returns the prompt and response.
    '''
    # concatenate the prompt in to one cohererent prompt, query the API, and return the result
    prompt = f"{role}, {context}, {style}, {task}, {constraints}"
    response = query_gpt(prompt)
    return prompt, response

# make funciton to query GPT-3.5
def query_gpt(prompt, engine='gpt-3.5-turbo', max_tokens=400, temperature=0.5):
    '''
    This function takes in the prompt, engine, max tokens, and temperature and
    returns the response from the GPT-3.5 API.
    '''
    response = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
            model=engine,
            temperature=temperature,  
            max_tokens=max_tokens  
        )

    return response.choices[0].message.content
