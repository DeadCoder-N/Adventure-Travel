import re

# Read the HTML file
with open('Home.html', 'r', encoding='utf-8') as file:
    content = file.read()

# Fix external URLs to point to local files
content = content.replace('href="https://safar.devsvibe.co/"', 'href="Home.html"')
content = content.replace('action="https://safar.devsvibe.co/accommodation/"', 'action="accommodation/"')

# Fix any remaining absolute paths that might have been missed
remaining_fixes = {
    'href="/blog/"': 'href="#"',
    'href="https://safar.devsvibe.co/blog/"': 'href="#"',
    'href="https://safar.devsvibe.co/contact/"': 'href="Pages/Other Pages/contact.html"',
    'href="/accommodation/?': 'href="accommodation/accommodation.html?',
    'href="/accommodation/disneyland-park-adventure-land/"': 'href="accommodation/disneyland-park-adventure-land.html"',
    'href="/blog/?': 'href="#?',
    'href="/your-guide-to-stress-free-booking/?': 'href="#?'
}

for old, new in remaining_fixes.items():
    content = content.replace(old, new)

# Write the updated content back to the file
with open('Home.html', 'w', encoding='utf-8') as file:
    file.write(content)

print("All navigation links have been fixed!")