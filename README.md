# meetek.ai

Marketing site for Meetek. Static HTML in `public/`. Hosted on GitHub Pages: `.github/workflows/pages.yml` publishes `public/` on every push to `main`. `public/CNAME` sets the custom domain meetek.ai.

- `build.py`: generates `public/index.html` (Hebrew) and `public/en/index.html` (English) from one template. Edit the text there, then run `python3 build.py`.
- `public/styles.css`: design (light and dark themes).
- `public/site.js`: theme toggle and scroll animations.

Every push to `main` is deployed by the host.
