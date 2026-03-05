# docs/conf.py

from __future__ import annotations

from datetime import datetime

from turtini_sphinx_theme import get_theme_paths


# ---- Project metadata ----
project = "OpenShift VM Demo"
author = "Turtini LLC"
copyright = f"{datetime.utcnow().year}, Turtini LLC"


# ---- Extensions ----
extensions = [
    "myst_parser",
]


# ---- Source config ----
source_suffix = {".md": "markdown"}
root_doc = "readme"

exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# ---- Theme ----
html_theme = "sphinx_rtd_theme"
html_theme_options = {
    "collapse_navigation": False,
    "navigation_depth": 4,
}


# ---- MyST ----
myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "tasklist",
    "attrs_inline",
]


# ---- Shared theme assets (from turtini-sphinx-theme package) ----
_paths = get_theme_paths()

# Use the package templates FIRST so it overrides the RTD theme layout
templates_path = [_paths["templates"]]

# Sphinx will copy these into _static at build time
html_static_path = [_paths["static"]]

# These reference the build output _static/ directory, not your repo folder
html_logo = "_static/turtini-logo.png"
html_favicon = "_static/favicon.ico"

# Add your shared CSS/JS
html_css_files = ["turtini.css"]
# If you add a JS file in the package, uncomment:
# html_js_files = ["turtini-banner.js"]


# ---- Footer "Last updated" ----
html_last_updated_fmt = "%B %d, %Y"


# ---- Variables for Jinja templates ----
html_context = {
    "turtini_year": datetime.utcnow().year,
}

# RTD may inject canonical URL; safe default:
html_baseurl = ""
