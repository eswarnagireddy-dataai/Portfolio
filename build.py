import yaml
import os
import shutil
import markdown
from jinja2 import Environment, FileSystemLoader

OUTPUT_DIR = "docs"
DATA_DIR = "data"
TEMPLATE_DIR = "templates"
STATIC_DIR = "static"
CONTENT_DIR = "content"

def load_data(filename):
    filepath = os.path.join(DATA_DIR, filename)
    if not os.path.exists(filepath):
        return []
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
        
    # 2. Case Study Pages
    case_study_template = env.get_template("case_study.html")
    case_studies_path = os.path.join(CONTENT_DIR, "case-studies")
    
    if os.path.exists(case_studies_path):
        for filename in os.listdir(case_studies_path):
            if filename.endswith(".md"):
                slug = filename.replace(".md", "")
                with open(os.path.join(case_studies_path, filename), "r") as f:
                    md_content = f.read()
                
                # Extract Title from first H1
                title = "Case Study"
                for line in md_content.split('\n'):
                    if line.startswith('# '):
                        title = line.replace('# ', '').strip()
                        break
                
                html_content = markdown.markdown(md_content, extensions=['fenced_code', 'tables'])
                
                output_filename = f"case-study-{slug}.html"
                rendered_page = case_study_template.render(
                    profile=profile,
                    title=title,
                    content=html_content
                )
                
                with open(os.path.join(OUTPUT_DIR, output_filename), "w") as f:
                    f.write(rendered_page)
                    
    # Copy Static Files
    output_static = os.path.join(OUTPUT_DIR, "static")
    if os.path.exists(STATIC_DIR):
        shutil.copytree(STATIC_DIR, output_static)

    print(f"Site built successfully in '{OUTPUT_DIR}' directory.")

if __name__ == "__main__":
    build()
