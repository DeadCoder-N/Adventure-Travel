import re

# Read the HTML file
with open('Home.html', 'r', encoding='utf-8') as file:
    content = file.read()

# Fix logo links to point to Index.html
content = content.replace('href="Home.html"', 'href="Index.html"')

# Write the updated content back to the file
with open('Home.html', 'w', encoding='utf-8') as file:
    file.write(content)

print("Logo links now point to Index.html!")