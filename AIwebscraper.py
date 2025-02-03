import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import os
import time
import logging
from transformers import pipeline

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

generator = pipeline('text-generation', model='EleutherAI/gpt-neo-2.7B')
#prompt
def generate_code(instructions):
    prompt = f"Generate Python code for the following web scraping task: {instructions}"
    print(prompt)
    try:
        response = generator(prompt, max_length=300, num_return_sequences=1)
        code = response[0]['generated_text'].strip()
        logging.info(f"Generated code: {code}")
        return code
    except Exception as e:
        logging.error(f"Error generating code: {e}")
        return None

def execute_code(code):
    try:
        exec(code)
    except Exception as e:
        logging.error(f"Error executing code: {e}")


def main():
    clear_terminal()
    instructions = input("Enter the instructions: ")
    generated_code = generate_code(instructions)
    if generated_code:
        execute_code(generated_code)
    else:
        logging.error("Failed to generate code based on the instructions.")

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    main()
