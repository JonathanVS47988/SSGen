#generate_page.py

import os
from htmlnode import markdown_to_html_node
from extract_title import extract_title

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    with open(from_path) as file:
        md_content = file.read()
    
    page_title = extract_title(md_content)
    Master_node = markdown_to_html_node(md_content)
    Master_string = Master_node.to_html()
    
    with open(template_path) as file:
        template_content = file.read()
        final_content = template_content.replace("{{ Title }}", page_title)
        final_content = template_content.replace("{{ Content }}", Master_string)
    
    dest_dir = os.path.dirname(dest_path)
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    with open(dest_path, 'w') as file:
        file.write(final_content)