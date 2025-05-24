from os import read
import os
import re
# import shutil

from markdown_blocks import markdown_to_html_node

def extract_title(markdown):
    match = re.search("^#{1,6} (.*)", markdown)
    if not match:
        raise Exception("No header")
    
    return match.group(1)

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    with open(from_path, 'r') as markdown_file:
        markdown = markdown_file.read()
    
    markdown_html = markdown_to_html_node(markdown).to_html()

    with open(template_path, 'r') as template_path:
        template = template_path.read()

    title = extract_title(markdown)
    template = template.replace(r"{{ Title }}", title)
    template = template.replace(r"{{ Content }}", markdown_html)

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    with open(dest_path, 'w') as generated_file:
        generated_file.write(template)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    print(f"Generating Page Recursive {dir_path_content}, {template_path}, {dest_dir_path}")
    for filename in os.listdir(dir_path_content):
        print(f"Staring {filename}")
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        print(f" * {from_path} -> {dest_path}")
        if os.path.isfile(from_path):
            print(f"  * {from_path} is a file create report {dest_path}")
            generate_page(from_path, template_path, dest_path.replace(".md",".html"))
        else:
            print(f"  * {from_path} is a folder keep looking")
            generate_pages_recursive(from_path, template_path, dest_path)




# def copy_files_recursive(source_dir_path, dest_dir_path):
#     if not os.path.exists(dest_dir_path):
#         os.mkdir(dest_dir_path)

#     for filename in os.listdir(source_dir_path):
#         from_path = os.path.join(source_dir_path, filename)
#         dest_path = os.path.join(dest_dir_path, filename)
#         print(f" * {from_path} -> {dest_path}")
#         if os.path.isfile(from_path):
#             shutil.copy(from_path, dest_path)
#         else:
#             copy_files_recursive(from_path, dest_path)