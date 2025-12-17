import yaml
import os
import shutil
from jinja2 import Environment, FileSystemLoader

OUTPUT_DIR = "docs"
DATA_DIR = "data"
TEMPLATE_DIR = "templates"
STATIC_DIR = "static"

def load_data(filename):
    filepath = os.path.join(DATA_DIR, filename)
    with open(filepath, "r") as f:
        return yaml.safe_load(f)

def build():
    # Ensure output directory exists
    if os.path.exists(OUTPUT_DIR):
        shutil.rmtree(OUTPUT_DIR)
    os.makedirs(OUTPUT_DIR)

    # Load data
    profile = load_data("profile.yaml")
    projects = load_data("projects.yaml")
    
    # Setup Jinja2
    env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
    
    # Render Templates
    # 1. Index Page
    index_template = env.get_template("index.html")
    index_output = index_template.render(profile=profile, projects=projects)
    with open(os.path.join(OUTPUT_DIR, "index.html"), "w") as f:
        f.write(index_output)
        
    # Copy Static Files
    output_static = os.path.join(OUTPUT_DIR, "static")
    if os.path.exists(STATIC_DIR):
        shutil.copytree(STATIC_DIR, output_static)

    print(f"Site built successfully in '{OUTPUT_DIR}' directory.")

if __name__ == "__main__":
    build()
