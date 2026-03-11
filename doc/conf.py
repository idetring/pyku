project = 'pyku'
copyright = '2026, Deutscher Wetterdienst'
author = 'KU'

extensions = [
    'matplotlib.sphinxext.mathmpl',
    'matplotlib.sphinxext.plot_directive',
    'sphinx.ext.viewcode',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.napoleon',
    'sphinx.ext.autodoc',
    'sphinx.ext.todo',
    'sphinxcontrib.programoutput',
    'IPython.sphinxext.ipython_directive',
    'IPython.sphinxext.ipython_console_highlighting',
    'sphinx_togglebutton',
    'nbsphinx',
    'sphinx_gallery.load_style',
]

# Build links to external documentation
# -------------------------------------

primary_domain = 'py'

intersphinx_mapping = {
    'xarray': ('https://docs.xarray.dev/en/stable/', None),
    'geopandas': ('https://geopandas.org/en/stable/', None),
    'pandas': ('https://pandas.pydata.org/pandas-docs/stable/', None),
    'numpy': ('https://numpy.org/doc/stable/', None),
    'pyresample': ('https://pyresample.readthedocs.io/en/stable/', None),
    'cartopy': ('https://cartopy.readthedocs.io/latest/', None),
    'matplotlib': ('https://matplotlib.org/stable/', None),
}

ipython_warning_is_error = False

sphinx_ipython_plot = "inline"
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme = 'sphinx_book_theme'
html_static_path = ['_static', 'savefig']

nbsphinx_kernel_name = 'python3'

# html_title = 'pyku'
html_favicon = '_static/pyku_logo.jpg'

html_theme_options = {
    "navigation_with_keys": True,
    "logo": {
        "text": "PYKU",
        "sizes": "32x32",
        "image_light": "_static/pyku_logo.jpg",
        "image_dark": "_static/pyku_logo.jpg",
    }

}
# html_css_files = ['css/custom.css']

todo_include_todos = True

nbsphinx_thumbnails = {
     'plugins/climate_indicators/clix': '_static/pyku_indicators.jpg',
     'tutorials/colormaps': '_static/pyku_colors.jpg',
     'tutorials/polygons': '_static/pyku_polygons.jpg',
     'tutorials/geographic_projections': '_static/pyku_mercator.jpg',
     'tutorials/downscaling_svd': '_static/pyku_downscaled.jpg',
     'tutorials/pdf_transfer': '_static/pyku_transfer.jpg',
     'tutorials/starter': '_static/pyku_bike.jpg',
     'tutorials/named_ensembles': '_static/pyku_together.jpg',
     'tutorials/CMORization': '_static/pyku_bored.jpg',
     'tutorials/finding_and_preprocessing': '_static/pyku_find.jpg',
     'tutorials/opendap': '_static/pyku_network.jpg',
     'tutorials/distributed_computing': '_static/pyku_distributed.jpg',
     'tutorials/customize_plots': '_static/pyku_customize.jpg',
}

# When working on the documentation, it can be usefull to turn off everything
# we are not working on at the moment, or just what is needed

# include_patterns = [
#     "index.rst",
#     "api.rst",
#     "analyse.rst"
# ]

# exclude_patterns = [
#     "api.rst",
#     "analyse.rst",
#     "check.rst",
#     "cicd.rst",
#     "changelog.rst",
#     "colormaps.rst",
#     "command_line.rst",
#     "compute.rst",
#     "concept.rst",
#     "contribute.rst",
#     "downscale.rst",
#     "downscaling.rst",
#     "drs.rst",
#     "features.rst",
#     "find.rst",
#     "geo.rst",
#     "installation.rst",
#     "jupyter.rst",
#     "mask.rst",
#     "meta.rst",
#     "plugins.rst",
#     "plugins/climate_forecast/climate_forecast.rst",
#     "postmodel.rst",
#     "pdftransfer.rst",
#     "read.rst",
#     "repair.rst",
#     "roadmap.rst",
#     "style_guideline.rst",
#     "test.rst",
#     "troubleshooting.rst",
#     "tutorials.rst",
#     "tutorials/pdf_transfer.ipynb",
#     "tutorials/downscaling_svd.ipynb",
#     "tutorials/colormaps.rst",
#     "tutorials/distributed_computing.rst",
#     "tutorials/geographic_projections.rst",
#     "tutorials/opendap.rst",
#     "tutorials/starter.rst",
#     "tutorials/core_functions.rst",
#     "tutorials/customize_plots.rst",
# ]
