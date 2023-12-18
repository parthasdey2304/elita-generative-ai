import requests
import sys
import re
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import TerminalFormatter

if len(sys.argv) != 2:
    print("Usage: python elita.py <prompt>")
    sys.exit(1)

prompt = sys.argv[1]

url = "https://chatgpt-best-price.p.rapidapi.com/v1/chat/completions"

payload = {
    "model": "gpt-3.5-turbo",
    "messages": [
        {
            "role": "user",
            "content": prompt
        }
    ]
}

headers = {
    "content-type": "application/json",
    "X-RapidAPI-Key": "USE_YOUR_OWN_RAPID_API_KEY",
    "X-RapidAPI-Host": "chatgpt-best-price.p.rapidapi.com"
}

# os.system('echo -e "\e[32m[INFO] Generating...."')
# os.system('echo -e "\e[32m[INFO] Here we go!!')

response = requests.post(url, json=payload, headers=headers)
response = response.json()

code_output = response['choices'][0]['message']['content']

# Extract code block from triple backticks
code_blocks = re.findall(r'```(.*?)```', code_output, re.DOTALL)

# Replace code blocks with highlighted versions within a box
for code_block in code_blocks:
    lexer = get_lexer_by_name("python", stripall=True)
    highlighted_code = highlight(code_block, lexer, TerminalFormatter())

    # Create a box around the highlighted code
    box_width = 80  # Adjust as needed
    box_horizontal_line = '+' + '-' * (box_width - 2) + '+'
    box_code = f"|{highlighted_code}\n"
    box_code += box_horizontal_line

    code_output = code_output.replace(f'```{code_block}```', box_code)

# Print the modified output
print(code_output)

