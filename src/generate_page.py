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
        final_content = final_content.replace("{{ Content }}", Master_string)
    
    dest_dir = os.path.dirname(dest_path)
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    with open(dest_path, 'w') as file:
        file.write(final_content)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    
    dirs = [item for item in os.listdir(dir_path_content) if os.path.isdir(os.path.join(dir_path_content, item))]
    files = [item for item in os.listdir(dir_path_content) if os.path.isfile(os.path.join(dir_path_content, item))]
    template = os.path.abspath(template_path)

    #print(dirs)     #debug
    #print(files)    #debug
    #print(template) #debug

    for file in files:
        try:
            if os.path.splitext(file)[1] == ".md":
                base_name, old_ext = os.path.splitext(file)
                new_file = base_name + ".html"
                generate_page(os.path.join(dir_path_content, file), template, os.path.join(dest_dir_path, new_file))
        except:
            print(f"An error occured while converting the file {file}")

    for dir in dirs:
        try:
            generate_pages_recursive(os.path.join(dir_path_content, dir), template, os.path.join(dest_dir_path, dir))
        except:
            print(f"An error occured while crawling directory {dir}")