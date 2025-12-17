# Data & AI Strategic Portfolio

This is a static portfolio website generated with Python and Jinja2.

## How to Build
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the build script:
   ```bash
   python build.py
   ```
3. The site will be generated in the `docs/` folder.

## GitHub Pages Deployment
1. Push this repository to GitHub.
2. Go to **Settings** > **Pages**.
3. Under **Build and deployment**, select **Source** as `Deploy from a branch`.
4. Select `main` (or `master`) branch and `/docs` folder.
5. Save. Your site will be live!

## Editing Content
- **Profile Info**: Edit `data/profile.yaml`
- **Projects**: Edit `data/projects.yaml`
- **Styling**: Edit `static/css/style.css`
