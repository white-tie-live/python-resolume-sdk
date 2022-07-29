"""Sphinx configuration."""
project = "Resolume SDK"
author = "Allen Ellis"
copyright = "2022, Allen Ellis"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
