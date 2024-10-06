import google.generativeai as genai
from dotenv import load_dotenv
import os
load_dotenv()
api_key = os.getenv('API_KEY')
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-pro")
amount = 10
topics = "Cybersecurity"
def getinfo(amount,topics):
    prompt = ("Give me %d questions on the topic of %s in the form of Multiple Choice Question. Display the question, the options and the correct option in the same line separated by dollar signs. Show everything in the same line. Show the solution too separated by a dollar sign. show options as numbers. Show only the correct number in the solution"%(amount,topics))
    response = model.generate_content(prompt)
    return response.text
def separateques(response):
    separaratedq = response.split("\n")
    return separaratedq
def separateoptandsol(question):
    elements = question.split("$")
    return elements

    