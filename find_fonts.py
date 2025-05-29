# Import the built-in regular expressions module
import re

# import the requests library to download a CSS file from the web
import requests

# Set to True to load from the web, or False to load from a local file
use_web = True

# URL of a CSS file
css_url = "https://fonts.googleapis.com/css2?family=Roboto:wght@100;300;400;700&family=Open+Sans:wght@300;400;600;700&display=swap"

# Path to a local CSS file (if not using the web)
css_file_path = "example.css"

# Get the CSS content depending on the selected mode
if use_web:
    # Load CSS from the web using requests
    response = requests.get(css_url)
    css_content = response.text
    print("Loaded CSS from the web.") 
else:
    # Load CSS from a local file using the built-in open() function
    # "r" means read-only mode; we're not changing the file, just reading its contents
    with open(css_file_path, "r", encoding="utf-8") as f:
        # 'f' is the file object. Calling f.read() reads the entire file as one big string.
        css_content = f.read()
    print("Loaded CSS from local file")

# Define a regular expression to find font file URLs inside the CSS content
# This pattern matches values like: url("...woff2"), url('...ttf'), url(...otf), etc.
# It looks for the word 'url(', then captures the file path ending in a font extension.
font_pattern = re.compile(r'url\((["\']?)([^)\'"]+\.(woff2?|ttf|otf|eot))\1\)', re.IGNORECASE)

# Use the regex pattern to find all matching font file URLs in the CSS content
# Each match is a tuple because our regex has two capturing groups
matches = font_pattern.findall(css_content)

# Count how many matches were found
print(f"Found {len(matches)} font file matches.")

# Create a list of only the font URLs by extracting the second item from each regex match tuple
font_urls = [match[1] for match in matches]

# Print each URL on a separate line
print("Font file URLs found:")
for url in font_urls:
    print(url)

# Save the list of font URLs to a text file (one URL per line)
# "w" mode means overwrite if the file already exists
with open("font_urls.txt", "w", encoding="utf-8") as f:
    f.write(f"Found {len(font_urls)} font files\n\n")
    for url in font_urls:
        f.write(url + "\n")

# Confirm that the file was saves successfully
print("Saved font URLs to font_urls.txt.")  
