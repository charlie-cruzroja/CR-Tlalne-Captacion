project = 'Captacion'
author = 'Captadoras'
release = '0.1.0'

extensions = [
    'sphinx.ext.autodoc',    # For docstrings
    'sphinx.ext.viewcode',   # Adds source code links
]

templates_path = ['_templates']
exclude_patterns = []

# The master document (entry point)
master_doc = 'index'

# HTML output options
html_theme = 'alabaster'  # You can change this to 'sphinx_rtd_theme' if installed
html_static_path = ['_static']