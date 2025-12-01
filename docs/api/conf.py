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
    'sphinx.ext.viewcode',  # To link to the source code
    'sphinx.ext.autosummary',  # To automatically generate summary tables
    # Additional utility extensions
    # 'sphinx_autodoc_typehints',  # To display type hints nicely
    'numpydoc',  # To support NumPy style docstrings
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
html_static_path = ['_static']

# Custom CSS files
html_css_files = [
    'custom.css',
]

# If true, the reST sources are included in the HTML build as _sources/foo.txt.
html_copy_source = False

# If true, "Created using Sphinx" is shown in the HTML footer.
html_show_sphinx = True

# -- Autodoc configuration ---------------------------------------------------
# Type hints: show in signature only (not in description)
# autodoc_typehints = "signature"

# Use short format for type hints
# autodoc_typehints_format = "short"

# Preserve the defaults in signatures
autodoc_preserve_defaults = True

# -- Sphinx autodoc typehints configuration ----------------------------------
# This prevents duplicate parameter documentation in the body
# typehints_defaults = "comma"

# -- Numpydoc configuration ---------------------------------------------------
# Don't show class members automatically
numpydoc_show_class_members = False

# Don't show type hints in the parameter descriptions since they're in signature
numpydoc_show_type_hint = False
