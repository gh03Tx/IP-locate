import requests
from bs4 import BeautifulSoup
import shutil
import textwrap
print("""
(^_^) IP LOCATER
""")

def print_in_box_centered(text):
    terminal_width = shutil.get_terminal_size().columns
    wrapped_lines = textwrap.wrap(text, width=60)
    box_width = max(len(line) for line in wrapped_lines) + 4

    top = '+' + '-' * (box_width - 2) + '+'
    bottom = '+' + '-' * (box_width - 2) + '+'

    print(top.center(terminal_width))
    for line in wrapped_lines:
        padded = '| ' + line.ljust(box_width - 4) + ' |'
        print(padded.center(terminal_width))
    print(bottom.center(terminal_width))


# === Web scraping part ===
url = 'https://www.dnsleaktest.com'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Extract target div
target_div = soup.find('div', class_='welcome text-center')
if target_div:
    text = target_div.text.strip()
    print_in_box_centered(text)
else:
    print("Target <div> not found.")
