#extract_title.py

def extract_title(markdown):
    md_lines = markdown.split('\n')

    for line in md_lines:
        if line.startswith('#'):
            return line[1:].strip()
    raise Exception("No h1 header!  Please correct and retry.")

            