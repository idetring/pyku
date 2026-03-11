#!/usr/bin/env python3

"""
Functions for reading data
"""


def template(ds, var):

    # {{{

    """
    Template function

    Arguments:
        ds (xarray.dataset): Input dataset
        var (str): Variable name

    Returns:
        dict: Attributes of variable
    """

    return ds[var].attrs

    # }}}
