# -- Path setup --------------------------------------------------------------

import os
import sys

# Add the project root to the path so Sphinx can find the 'mapu' package
sys.path.insert(0, os.path.abspath('../../'))


# -- Project information -----------------------------------------------------

project = 'mapu'
copyright = '2025, Sean Ma'
author = 'Sean Ma'
release = '0.0.1'


# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',  # The core extension for reading docstrings
    'sphinx.ext.napoleon',  # For Google/NumPy style docstrings (optional but good practice)
    'sphinx.ext.viewcode',  # Links source code
    'myst_parser',  # Allows reStructuredText to include Markdown files
]

# Use the Furo theme (a modern alternative)
html_theme = 'furo'

# Set the source file suffix to allow both .rst and .md
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

html_theme = 'furo'
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = []  # ['_static'] for custom CSS/images
