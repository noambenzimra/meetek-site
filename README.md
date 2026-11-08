# meetek.ai

Marketing site for Meetek. Static HTML in `public/`. Hosted on GitHub Pages: `.github/workflows/pages.yml` publishes `public/` on every push to `main`. `public/CNAME` sets the custom domain meetek.ai.

- `public/index.html`: the site (Hebrew, hand-edited; source of truth is `Desktop/Meetek/website/index.html`). `build.py` is the old generator and is no longer used: running it would overwrite the site.
- `public/models/`: 3D models for the hero (CC BY 4.0, credited in the footer).
- `public/styles.css`: design (light and dark themes).
- `public/site.js`: theme toggle and scroll animations.

Every push to `main` is deployed by the host.
