#!/usr/bin/env python3

"""
OGC functionalities
"""


def create_ogc_resource(name, datasource, type, **kwargs):

    """
    Generate an OGC resource for use with the geoserver.

    Arguments:
        name (str): To be defined.
        datasource (tbd): To be defined.
        type (tbd): To be defined

    Returns:
        tbd: To be defined

    Example:

        .. ipython::

           In [0]: import pyku, pyku.ogc
              ...: print("Doctest to be implemented")
    """

    raise Exception('Not implemented')


def publish_ogc_resource(name):

    """
    Publish an OGC resource to the geoserver

    Arguments:
        name (str): To be defined.

    Example:

        .. ipython::

           In [0]: import pyku, pyku.ogc
              ...: print("Doctest to be implemented")
    """

    raise Exception('Not implemented')


def sld_colormap(identifier=None):

    """
    Generates a standardized KU colormap for use with the *Style Layer
    Descriptor* (SLD). Here the output should consist of text (or if possible a
    xml file directly) that returns the colormap formatted for use as SLD for
    the geoserver. the function shall be built based on the *pyku*
    ``colormaps`` module.

    Arguments:
        identifier (str): The standardized KU colormap identifier.

    Returns:
        str: The SLD-ready colormap.

    Example:

        .. ipython::

           In [0]: import pyku, pyku.ogc
              ...: print("Doctest to be implemented")
    """

    raise Exception('Not implemented')


def ogc_check(ds):

    """
    Check datasets for compatibility issues before delivering them to the
    Geoserver. For example, ensure that datetime types are compatible with the
    Geoserver, particularly when using non-standard calendars like a 365-day
    calendar. Address any other potential issues that may arise.

    Arguments:
        ds (:class:`xarray.Dataset`): The input Dataset.

    Returns:
        :class:`pandas.DataFrame`: Dataframe with issues.

    Example:

        .. ipython::

           In [0]: import pyku, pyku.ogc
              ...: print("Doctest to be implemented")
    """

    raise Exception("Not implemented")


def ogc_repair(ds):

    """
    Return repaired dataset. Some of the datasets we will bring to the geosever
    may have broken metadata. These shall be repaired automatically and
    on-the-fly with the ogc_repair function.

    Arguments:
        ds (:class:`xarray.Dataset`): The input Dataset.

    Returns:
        ds (:class:`xarray.Dataset`): The repaired dataset

    Example:

        .. ipython::

           In [0]: import pyku, pyku.ogc
              ...: print("Doctest to be implemented")
    """

    raise Exception("Not implemented")


def ogc_resample_datetimes(ds):

    """
    Resample the dataset datetimes. For example, a daily dataset can be
    resampled to a monthly dataset. Ensure all resulting metadata are
    compatible for delivery to the Geoserver.

    Arguments:
        ds (:class:`xarray.Dataset`): The input Dataset.

    Returns:
        :class:`xarray.Dataset`: Dataset with resampled datetimes

    Example:

        .. ipython::

           In [0]: import pyku, pyku.ogc
              ...: print("Doctest to be implemented")
    """

    raise Exception("Not implemented")


def ogc_mean_map(ds):

    """
    Calculate the mean value for all pixels in the dataset. Ensure all
    resulting metadata are compatible for delivery to the Geoserver.

    Arguments:
        ds (:class:`xarray.Dataset`): The input Dataset.

    Returns:
        :class:`xarray.Dataset`: Dataset containing the mean

    Example:

        .. ipython::

           In [0]: import pyku, pyku.ogc
              ...: print("Doctest to be implemented")
    """

    raise Exception("Not implemented")


def ogc_mask(ds, gdf):

    """
    Given a dataset and a polygon/multipolygon, mask all values outside the
    polygon. Ensure all resulting metadata are compatible for delivery to the
    Geoserver.

    .. note::

       The function should also be able to deal with multiple polygons given as
       a :class:`geopandas.GeoDataFrame` in one go.

    Arguments:
        ds (:class:`xarray.Dataset`): The input Dataset.
        gdf (:class:`geopandas.GeoDataFrame`): The polygon(s) used for masking.

    Returns:
        :class:`xarray.Dataset`: Dataset containing the mean

    Example:

        .. ipython::

           In [0]: import pyku, pyku.ogc
              ...: print("Doctest to be implemented")
    """

    raise Exception("To be implemented")


def ogc_list_standards():

    """
    List all defined standards defined in 'pyku/geoserver.yaml'

    Example:

        .. ipython::

           In [0]: import pyku, pyku.ogc
              ...: print("Doctest to be implemented")
    """

    raise Exception("Not implemented")


def ogc_filename(ds, standard):

    """
    Return file name according to the metadata in the dataset.

    Arguments:
        ds (:class:`xarray.Dataset`): The input Dataset.
        standard (str): The standard used to distinguish between dataset types,
            which must be defined in 'pyku/geoserver.yaml'.

    Returns:
        str: The filename.

    Example:

        .. ipython::

           In [0]: import pyku, pyku.ogc
              ...: print("Doctest to be implemented")
    """

    raise Exception("Not implemented")


def ogc_stem(ds, standard):

    """
    Return file stem (basename) according to the metadata in the Dataset.

    Arguments:
        ds (:class:`xarray.Dataset`): The input Dataset.
        standard (str): The standard used to distinguish between dataset types,
            which must be defined in 'pyku/geoserver.yaml'.

    Returns:
        str: File base name

    Example:

        .. ipython::

           In [0]: import pyku, pyku.ogc
              ...: print("Doctest to be implemented")
    """

    raise Exception("Not implemented")


def ogc_parent(ds, standard):

    """
    Generates a directory based on the input dataset metadata.

    Arguments:
        ds (:class:`xarray.Dataset`): The input Dataset.
        standard (str): The standard used to distinguish between dataset types,
            which must be defined in 'pyku/geoserver.yaml'.

    Returns:
        str: The filename parent.

    Example:

        .. ipython::

           In [0]: import pyku, pyku.ogc
              ...: print("Doctest to be implemented")
    """

    raise Exception('Not implemented')


def to_georaster(ds, standard, connection_string='None'):

    """
    Write the dataset into an Oracle Spatial GeoRaster.

    Arguments:
        ds (:class:`xarray.Dataset`): The input dataset.
        standard (str): The standard used to distinguish between dataset types,
            which must be defined in 'pyku/geoserver.yaml'.
        connection_string (str): The ORACLE connection string.

    Example:

        .. ipython::

           In [0]: import pyku, pyku.ogc
              ...: print("Doctest to be implemented")
    """

    raise Exception("Not implemented")


def to_ogc_units(ds):

    """
    Convert dataset units to a format compatible with Geoserver and natural for
    the end user. For example, convert precipitation to millimeters or
    millimeters per hour, and temperatures to Celsius.

    Arguments:
        ds (:class:`xarray.Dataset`): The input dataset.

    Returns:
        :class:`xarray.Dataset`: The dataset with geoserver units.

    Example:

        .. ipython::

           In [0]: import pyku, pyku.ogc
              ...: print("Doctest to be implemented")
    """

    raise Exception("Not implemented")


def to_ogc_attrs(ds, var):

    """
    Convert dataset attributes to a format compatible with the geoserver.

    Arguments:
        ds (:class:`xarray.Dataset`): The input dataset.
        var (str): The variable name.

    Returns:
        :class:`xarray.Dataset`: The dataset with goeserver-compatible
            attributes.

    Example:

        .. ipython::

           In [0]: import pyku, pyku.ogc
              ...: print("Doctest to be implemented")
    """

    raise Exception("Not implemented")


def to_ogc_varnames(ds, var):

    """
    Convert variable names to a format compatible with Geoserver and a naming
    convention that is user-friendly. For example, rename the variable 'tas' to
    'temperature', depending on the context.

    Arguments:
        ds (:class:`xarray.Dataset`): The input dataset.
        var (str): The variable name.

    Returns:

        :class:`xarray.Dataset`: The variable names compatible with the
        geoserver

    Example:

        .. ipython::

           In [0]: import pyku, pyku.ogc
              ...: print("Doctest to be implemented")
    """

    raise Exception("Not implemented")


def to_ogc_georeferencing(ds):

    """
    Convert and apply georeferencing to a geoserver-compatible format.

    Arguments:
        ds (:class:`xarray.Dataset`): The input dataset.

    Returns:
        :class:`xarray.Dataset`: The dataset with geoserver compatible
        georeferencing

    Example:

        .. ipython::

           In [0]: import pyku, pyku.ogc
              ...: print("Doctest to be implemented")
    """

    raise Exception("Not implemented")


def to_ogc_format(ds):

    """
    Convert the dataset to a format compatible with Geoserver. This function
    should integrate subfunctions for converting attributes, units, naming
    conventions, and georeferencing to Geoserver standards

    Arguments:
        ds (:class:`xarray.Dataset`): The input dataset.

    Returns:
        :class:`xarray.Dataset`: The geoserver-compatible dataset

    Example:

        .. ipython::

           In [0]: import pyku, pyku.ogc
              ...: print("Doctest to be implemented")
    """

    raise Exception("Not implemented")


def to_geoserver_netcdf(ds, var=None, basedir=None):

    """
    Write the dataset to disk in a format compatible with Geoserver. This
    function handles the technical details associated with file writing for
    delivery to the Geoserver. For instance, it manages data splitting (e.g.
    into regions if needed) and ensures the naming convention aligns with
    Geoserver requirements.

    Arguments:
        ds (:class:`xarray.Dataset`): The input dataset with metadata
            compatible with delivery to the geoserver.
        var (str): The variable name.
        basedir (str): The base directory where NetCDF files are written

    Example:

        .. ipython::

           In [0]: import pyku, pyku.ogc
              ...: print("Doctest to be implemented")
    """

    raise Exception("Not implemented")
