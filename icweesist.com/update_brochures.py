import os, glob, re

directory = r'c:\Users\Sumit\Desktop\SIST\IRC website\irc\icweesist.com'
files_to_update = glob.glob(os.path.join(directory, '*.html'))

brochure_link = "https://drive.google.com/uc?export=download&id=17nXtZt228L6shf-4DfwwmH5aEoDLOUdh"

count = 0
for filepath in files_to_update:
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    new_content = re.sub(
        r'(<a[^>]*href=")[^"]*("[^>]*>\s*Download\s+Brochure\s*</a>)',
        r'\g<1>' + brochure_link + r'\2',
        content,
        flags=re.IGNORECASE
    )

    new_content = re.sub(
        r'(<a[^>]*href=")[^"]*("[^>]*>\s*Brochure\s*-\s*Download[^<]*</a>)',
        r'\g<1>' + brochure_link + r'\2',
        new_content,
        flags=re.IGNORECASE
    )

    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        count += 1

print(f"Updated brochure links in {count} files.")
