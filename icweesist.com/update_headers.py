import os

# Define the target block to search for
# This is the standard header start in most files
header_start_pattern = "<!--HEADER-->\n        <header>\n            <div id=\"lgx-header\" class=\"lgx-header\">"
header_style_pattern = "<!--HEADER-->\n<header>\n    <div id=\"lgx-header\" class=\"lgx-header\">"

# Define the new header style and top bar
new_header_block = """        <!--HEADER-->
        <style>
            .lgx-header-top {
                background: #fff;
                padding: 20px 0;
                border-bottom: 2px solid #e11c21;
                text-align: center;
                transition: all 0.3s ease;
            }
            .lgx-header-top h1 {
                font-family: 'Oswald', sans-serif;
                font-weight: 700;
                text-transform: uppercase;
                font-size: clamp(18px, 5vw, 36px);
                color: #222;
                margin: 0;
                line-height: 1.2;
                letter-spacing: 0.5px;
            }
            .lgx-logo img {
                border-radius: 8px;
                transition: all 0.3s ease;
                box-shadow: 0 4px 10px rgba(0,0,0,0.1);
            }
            .menu-onscroll .lgx-logo img {
                max-height: 50px !important;
            }
            @media (max-width: 767px) {
                .lgx-header-top {
                    padding: 10px 5px;
                }
            }
        </style>
        <header>
            <div id="lgx-header-top" class="lgx-header-top">
                <div class="container">
                    <h1>5th International conference on waste, energy and environment (ICWEE-2026)</h1>
                </div>
            </div>
            <div id="lgx-header" class="lgx-header">"""

# List of files to update (excluding ones already updated or likely different)
files_to_update = [
    "about-chennai.html", "about-cwm.html", "about-icetas.html",
    "advisory-committee.html", "awards-prizes.html", "conference-schedule.html",
    "conference-themes.html", "contact.html", "delegate-fee.html",
    "downloads.html", "gallery.html", "guidelines-to-authors.html",
    "mode-of-payment.html", "organizing-committee.html", "organizingchair-conveners.html",
    "patrons.html", "publications.html", "speakers.html", "technical-committee.html"
]

base_path = "c:\\Users\\Sumit\\Desktop\\SIST\\IRC website\\irc\\icweesist.com\\"

for filename in files_to_update:
    filepath = os.path.join(base_path, filename)
    if not os.path.exists(filepath):
        print(f"File not found: {filename}")
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Try different indentations/formats
    updated = False
    if header_start_pattern in content:
        content = content.replace(header_start_pattern, new_header_block)
        updated = True
    elif header_style_pattern in content:
        content = content.replace(header_style_pattern, new_header_block)
        updated = True
    else:
        # Failsafe: search for just the header tag if the comment above it varies
        simple_pattern = "<header>\n            <div id=\"lgx-header\" class=\"lgx-header\">"
        if simple_pattern in content:
            content = content.replace(simple_pattern, new_header_block)
            updated = True
            
    if updated:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated: {filename}")
    else:
        print(f"Could not find pattern in: {filename}")
