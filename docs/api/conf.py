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
    # Core Sphinx extensions
    'sphinx.ext.autodoc',  # To include documentation from docstrings
    'numpydoc',  #'sphinx.ext.napoleon',  # To support NumPy and Google style docstrings
    'sphinx.ext.viewcode',  # To link to the source code
    'sphinx.ext.autosummary',  # To automatically generate summary tables
    # Additional utility extensions
    'sphinx_autodoc_typehints',  # To display type hints nicely
    'sphinx_design',  # For badges, cards, etc.
]

# The suffix(es) of source filenames.
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use. This enables the PyData Sphinx Theme.
html_theme = 'pydata_sphinx_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = []  # ['_static'] for custom CSS/images


# If true, the reST sources are included in the HTML build as _sources/foo.txt.
html_copy_source = False

# If true, "Created using Sphinx" is shown in the HTML footer.
html_show_sphinx = True


# -- Numpydoc configuration ---------------------------------------------------

# Type hints: only show in signature
autodoc_typehints = "signature"

# Break signature into multiline format
autodoc_typehints_format = "split"

# Optional but helps match Polars aesthetic
numpydoc_show_class_members = False
