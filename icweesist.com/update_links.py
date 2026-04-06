import os, re

directory = r'c:\Users\Sumit\Desktop\SIST\IRC website\irc\icweesist.com'

files_to_update = [os.path.join(directory, 'index.html'), os.path.join(directory, 'index-2.html')]

# We'll use regex to match the anchor tags for Download Brochure and Register Now
# Currently: <a class="lgx-btn" href="downloads/ICWEE-2024-Brochure.pdf" ...>Download Brochure</a>
# Currently: <a class="lgx-btn lgx-btn-red" href="https://docs.google.com/forms/..." ...>Register Now</a>

brochure_link = "https://drive.google.com/uc?export=download&id=1qkhYZUcblWETuYnF9AWw0Py8hcUhuJUq"
registration_link = "https://drive.google.com/uc?export=download&id=1G48Cr21nTc3hUhxYaZKrKaeRGAWur2dc"

for filepath in files_to_update:
    if not os.path.exists(filepath):
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Update Download Brochure links only if they are not already correct
    pattern_brochure = r'(<a[^>]*href=")[^"]*("[^>]*>\s*Download Brochure\s*</a>)'
    content = re.sub(pattern_brochure, r'\g<1>' + brochure_link + r'\2', content, flags=re.IGNORECASE)
    
    # Update Register Now links
    pattern_register = r'(<a[^>]*href=")[^"]*("[^>]*>\s*Register Now\s*</a>)'
    content = re.sub(pattern_register, r'\g<1>' + registration_link + r'\2', content, flags=re.IGNORECASE)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Linked updated successfully!")
