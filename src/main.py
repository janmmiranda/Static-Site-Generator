import os, shutil

from textnode import *
from htmlnode import *
from text_type_enum import *
from inline_markdown import *
from block_markdown import *
from block_type_enum import *
from static_helper import copy_dir

def main():
    generate_pages_recursive("content", "template.html", "public")

def get_file_contents(path):
    with open(path) as f:
        return f.read()    
    
def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    md = get_file_contents(from_path)
    template = get_file_contents(template_path)
    content = markdown_to_html_node(md).to_html()
    title = extract_title(md)
    template = template.replace("{{ Title }}", title, 1)
    template = template.replace("{{ Content }}", content, 1)
    create_target_dir(dest_path)
    html_file = open(dest_path, "w+")
    html_file.write(template)
    html_file.close()


def create_target_dir(dest_path):
    if os.path.exists(dest_path):
        print(f"{dest_path} file exists")
        return
    
    dirs = dest_path.split("/")[:-1]
    path = "/".join(dirs)
    if os.path.exists(path):
        print(f"{path} dir exists")
        return
    
    print(f"creating new dir {path}")
    os.makedirs(path)        

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    if not os.path.exists(dir_path_content):
        raise ValueError(f"{dir_path_content} does not exist!")
    
    source_contents = os.listdir(dir_path_content)
    for content in source_contents:
        old_path = dir_path_content
        new_path = dest_dir_path
        if not old_path.endswith("/"):
            old_path += "/"
        old_path += content
        if not new_path.endswith("/"):
            new_path += "/"

        if os.path.isfile(old_path):
            new_path += old_path.split("/")[-1]
            new_path = new_path.replace(".md", ".html")
            print(f"calling generate_page for src: {old_path} target: {new_path}")
            generate_page(old_path, template_path, new_path)
        else:
            new_path += content
            print(f"{old_path} is a dir, recursive call made with target: {new_path}")
            generate_pages_recursive(old_path, template_path, new_path)

main()