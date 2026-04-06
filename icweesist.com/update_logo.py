import os, re, glob

directory = r'c:\Users\Sumit\Desktop\SIST\IRC website\irc\icweesist.com'

# We'll use glob to find all html files
html_files = glob.glob(os.path.join(directory, '*.html'))

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # We need to change the anchor tag to use flexbox so the image and text align horizontally
    # It currently is: <a href="index-2.html" class="lgx-scroll">
    # We will replace it safely (only if inside the lgx-logo div)
    
    # 1. Update the a-tag inside lgx-logo
    pattern_a_tag = r'(<div class="lgx-logo">\s*)<a href="index-2\.html" class="lgx-scroll">'
    repl_a_tag = r'\1<a href="index-2.html" class="lgx-scroll" style="display: flex; align-items: center; text-decoration: none;">'
    new_content = re.sub(pattern_a_tag, repl_a_tag, content)
    
    # 2. Add the title text right after the image
    # Current image tag: <img src="assets/img/icweesist-logo.jpeg" alt="ICWEE-2026" style="max-height: 70px; width: auto;" />
    
    # The text we want to append
    title_html = r'''
                                <div style="margin-left: 15px; font-size: 20px; font-weight: 800; color: #007336; line-height: 1.2; text-align: left; font-family: 'Oswald', sans-serif;">
                                    5th International conference on <br/>waste, energy and environment (ICWEE-2026)
                                </div>'''
    
    # Match the image tag and any following comments, then inject the title_html before the closing </a>
    # We'll just replace the image tag with itself + the title
    pattern_img = r'(<img src="assets/img/icweesist-logo\.jpeg" alt="ICWEE-2026" style="max-height: 70px; width: auto;"\s*/>)'
    
    # Only replace if it doesn't already have the text
    if "5th International conference on" not in new_content:
        new_content = re.sub(pattern_img, r'\1' + "\n" + title_html, new_content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

print("Updated HTML files!")
