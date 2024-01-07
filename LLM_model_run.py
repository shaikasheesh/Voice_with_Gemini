from dotenv import load_dotenv
import os
import google.generativeai as genai
from IPython.display import display
from IPython.display import Markdown
import textwrap3
load_dotenv() 
os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def to_markdown(text):
  text = text.replace('•', '  *')
  return textwrap3.indent(text, '> ', predicate=lambda _: True)

def get_gemini_response(prompt):
    model = genai.GenerativeModel('gemini-pro') #text input only model
    response = model.generate_content(prompt)
    output = to_markdown(response.text)
    return output 


#prompt = "tell me about India Country"

#print(get_gemini_response(prompt))