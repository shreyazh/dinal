import os

# Path to your images folder
folder = "images/book"

# Get all JPG files
images = [f for f in os.listdir(folder) if f.lower().endswith(".jpg")]

# Sort them (optional, to keep order consistent)
images.sort()

# Generate HTML
html_output = ""
for img in images:
    html_output += f'''<div class="page"><img src="{folder}/{img}"  alt="Book"></div>
    '''
    
# Save to file
with open("book.html", "w", encoding="utf-8") as f:
    f.write(html_output)

print("✅ HTML generated")
