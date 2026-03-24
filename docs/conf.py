# =========================================================
# Open Water Lab (OWL)
# =========================================================

import os
import sys

# package documentation (e.g. owl-data)
# sys.path.insert(0, os.path.abspath("../../owl-data/src"))
# sys.path.insert(0, os.path.abspath("../../owl-twin/src"))

# ---------------------------------------------------------
# Project information
# ---------------------------------------------------------

project = "Open Water Lab (OWL)"
author = "Open Water Lab (OWL)"
copyright = "2026, Open Water Lab (OWL), BIOMATH, UGent"
release = "0.1.0"

# ---------------------------------------------------------
# General configuration
# ---------------------------------------------------------

extensions = [
    "myst_parser",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx_autodoc_typehints",     
]

autodoc_default_options = {
    "members": True,
    "undoc-members": False,
    "private-members": False,
    "show-inheritance": True,
}

napoleon_google_docstring = False
napoleon_numpy_docstring = True

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

# ---------------------------------------------------------
# HTML output
# ---------------------------------------------------------

html_theme = "pydata_sphinx_theme"

html_title = "Open Water Lab (OWL)"


html_static_path = ["_static"]

def setup(app):
    app.add_css_file("custom.css")

# ---------------------------------------------------------
# Theme options
# ---------------------------------------------------------

html_theme_options = {
    "show_toc_level": 2,
    "navbar_start": ["navbar-logo"],
    "navbar_center": ["navbar-nav"],
    "navbar_end": ["theme-switcher", "navbar-icon-links"],

    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/OpenWaterLab",
            "icon": "fa-brands fa-github",
            "type": "fontawesome",
        },
    ],

    "show_toc_level": 2,
    "navigation_with_keys": True,
    "show_prev_next": False,

    "logo": {
        "text": "Open Water Lab (OWL)",
    },
}

# ---------------------------------------------------------
# Logos
# ---------------------------------------------------------


html_logo = "_static/OWL.png"
html_favicon = "_static/OWL.png"

# ---------------------------------------------------------
# MyST (Markdown) configuration
# ---------------------------------------------------------

myst_enable_extensions = [
    "colon_fence",     
    "deflist",         
    "html_admonition",
    "html_image",
]

# ---------------------------------------------------------
# Output tweaks
# ---------------------------------------------------------

html_show_sourcelink = False
html_copy_source = False
html_show_sphinx = False

autosummary_generate = True

# ---------------------------------------------------------
# Optional
# ---------------------------------------------------------

# from sphinx.ext.autosectionlabel import *
# extensions.append("sphinx.ext.autosectionlabel")
# autosectionlabel_prefix_document = True
html_context = {
    "github_user": "OpenWaterLab",
    "github_repo": "openwaterlab.github.io",
    "github_version": "main",
    "doc_path": "docs",
}
