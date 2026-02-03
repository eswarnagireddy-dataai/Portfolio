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

BASE_URL = "https://eswarnagireddy-dataai.github.io/Portfolio" # Update this to your custom domain if applicable

def build():
    # Ensure output directory exists
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
    else:
        # Delete all contents except the google verification file
        for item in os.listdir(OUTPUT_DIR):
            item_path = os.path.join(OUTPUT_DIR, item)
            if "google4c0ec9f6aae47acb" in item:
                continue
            if os.path.isdir(item_path):
                shutil.rmtree(item_path)
            else:
                os.remove(item_path)

    # Load data
    profile = load_data("profile.yaml")
    projects = load_data("projects.yaml")
    
    # Setup Jinja2
    env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
    
    # Track pages for sitemap
    pages = ["index.html"]
    
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
                
                html_content = markdown.markdown(md_content, extensions=['fenced_code', 'tables', 'md_in_html'])
                
                output_filename = f"case-study-{slug}.html"
                pages.append(output_filename)
                
                rendered_page = case_study_template.render(
                    profile=profile,
                    title=title,
                    content=html_content
                )
                
                with open(os.path.join(OUTPUT_DIR, output_filename), "w") as f:
                    f.write(rendered_page)

    # 3. Iceberg Page
    iceberg_template = env.get_template("iceberg.html")
    iceberg_output = iceberg_template.render(profile=profile)
    with open(os.path.join(OUTPUT_DIR, "iceberg.html"), "w") as f:
        f.write(iceberg_output)
    pages.append("iceberg.html")
                    
    # Generate Sitemap
    sitemap_content = '<?xml version="1.0" encoding="UTF-8"?>\n'
    sitemap_content += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for page in pages:
        url = f"{BASE_URL}/{page}" if page != "index.html" else BASE_URL
        sitemap_content += f'  <url>\n    <loc>{url}</loc>\n    <priority>{"1.0" if page == "index.html" else "0.8"}</priority>\n  </url>\n'
    sitemap_content += '</urlset>'
    
    with open(os.path.join(OUTPUT_DIR, "sitemap.xml"), "w") as f:
        f.write(sitemap_content)
        
    # Generate Robots.txt
    robots_content = f"User-agent: *\nAllow: /\nSitemap: {BASE_URL}/sitemap.xml"
    with open(os.path.join(OUTPUT_DIR, "robots.txt"), "w") as f:
        f.write(robots_content)

    # Copy Static Files
    output_static = os.path.join(OUTPUT_DIR, "static")
    if os.path.exists(STATIC_DIR):
        shutil.copytree(STATIC_DIR, output_static)

    print(f"Site built successfully in '{OUTPUT_DIR}' directory with sitemap and robots.txt.")

if __name__ == "__main__":
    build()
