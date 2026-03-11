#!/usr/bin/env python3

"""
Regression library
"""


class LR:
    """
    Numpy Linear Regression
    """

    def __str__(self):
        return "numpy Linear Regression"

    def __init__(self, data, predictors):
        """
        Class initialization

        Arguments:
            data (:class:`numpy.ndarray`): Data with shape (time x ny x nx)
            predictors (:class:`numpy.ndarray`): Predictor data with shape
                (predictor x ny x nx)
        """

        from sklearn.linear_model import LinearRegression

        self.data = data
        self.predictors = predictors
        self.linear_regression = LinearRegression()

    def fit(self):
        """
        Linear regression
        """

        import numpy as np

        # Get numpy arrays
        # ----------------

        ntimes_x_nsamples_nan = self.data
        npreds_x_nsamples_nan = self.predictors

        print("MarkerA", self.data.shape)
        print("MarkerB", self.predictors.shape)

        # Get numerical values
        # --------------------

        ntimes_x_nsamples_num = \
            ntimes_x_nsamples_nan[~np.isnan(ntimes_x_nsamples_nan).any(axis=1)]

        npreds_x_nsamples_num = \
            npreds_x_nsamples_nan[~np.isnan(npreds_x_nsamples_nan).any(axis=1)]

        nsamples_x_ntimes_num = ntimes_x_nsamples_num.T
        nsamples_x_npreds_num = npreds_x_nsamples_num.T

        # Fit
        # ---

        self.linear_regression.fit(
            nsamples_x_npreds_num,
            nsamples_x_ntimes_num
        )

    def predict(self, data):
        """
        Predict

        Arguments:
            data (:class:`numpy.ndarray`): The data to be predicted.

        Returns:
            :class:`numpy.ndarray`: predicted values with size (ntimes x
            nsamples)
        """

        import numpy as np

        # Rename for clarity
        # ------------------

        ntimes_x_nsamples_nan = data

        # Get data without nans
        # ---------------------

        ntimes_x_nsamples_num = \
            ntimes_x_nsamples_nan[~np.isnan(ntimes_x_nsamples_nan)]

        nsamples_x_ntimes_num = ntimes_x_nsamples_num.T

        # Perform linear regression
        # -------------------------

        nsamples_x_ntimes_num = \
            self.linear_regression.predict(nsamples_x_ntimes_num)

        # Get indices of numerical values
        # -------------------------------

        nsamples_x_ntimes_nan = ntimes_x_nsamples_nan.T
        num_indices = np.argwhere(~np.isnan(nsamples_x_ntimes_nan))

        # Replace regressed numerical values and return
        # ---------------------------------------------

        nsamples_x_ntimes_nan[num_indices] = nsamples_x_ntimes_num

        return nsamples_x_ntimes_nan


class LinearRegression:
    """
    xarray Linear Regression
    """

    # def __str__(self):
    #     return "Linear Regression"

    def __init__(self, data, predictors):
        """
        Class initialization

        Arguments:
            data (:class:`xarray.Dataset`): Data used to fit the linear
                regression
            predictors (:class:`xarray.Dataset`): Predictor data. The predictor
                data shall have the dimension predictor, and y/x projection
                coordinates
        """

        self.data = data
        self.predictors = predictors

        self.linear_regressions = {}

    def fit(self):
        """
        Fit
        """

        # Loop over data variables
        # ------------------------

        for varname in self.data.pyku.get_geodata_varnames():

            print('Marker', varname)

            # Select data from Datasets
            # -------------------------

            y_name, x_name = self.data.pyku.get_projection_yx_varnames()
            data = self.data[[varname, 'time', y_name, x_name]]

            y_name, x_name = self.data.pyku.get_projection_yx_varnames()

            predictors = \
                self.predictors[['predictors', y_name, x_name]]['predictors']

            ntimes = len(data.coords['time'])
            npredictors = len(predictors.coords['predictor'])

            self.linear_regressions[varname] = LR(
                data=data[varname].values.reshape(ntimes, -1),
                predictors=predictors.values.reshape(npredictors, -1)
            )

            self.linear_regressions[varname].fit()

    def predict(self, data):
        """
        Predict
        """

        import pyku.meta as meta
        import dask.array as dk
        import xarray as xr

        # Gather predicted DataArrays in list
        # -----------------------------------

        predicted_da_list = []

        # Loop over data variables
        # ------------------------

        for varname in meta.get_geodata_varnames(data):

            # Return exception is the number of NaNs does not match
            # -----------------------------------------------------

            count_training_data_non_zeros = dk.count_nonzero(
                dk.isnan(self.data.isel(time=0)[varname].data.reshape(-1))
            ).compute()

            count_data_non_zeros = dk.count_nonzero(
                dk.isnan(data[varname].isel(time=0).data.reshape(-1))
            ).compute()

            if count_training_data_non_zeros != count_data_non_zeros:

                raise Exception(
                    " The number of NaNs in the first timestep of thelow "
                    f"training data is {count_training_data_non_zeros} while "
                    "the number of NaNs in the first timestemp of the dataset "
                    f"to be fitted is {count_data_non_zeros}. This likely "
                    "indicates that the mask is not the same for both "
                    "datasets, while it should be."
                )

            # Select and order data dimensions
            # --------------------------------

            y_name, x_name = meta.get_projection_yx_varnames(data)

            lat_name, lon_name = meta.get_geographic_latlon_varnames(data)

            da = data[[varname, 'time', y_name, x_name]]

            # Get data dimension length
            # -------------------------

            ntimes = len(data[varname].coords['time'])

            np_out = self.linear_regressions[varname].predict(
                da[varname].values.reshape(ntimes, -1)
            )

            predicted = xr.DataArray(
                name=f'{varname}',
                data=np_out.reshape(
                    ntimes,
                    data.clu.get_ny(),
                    data.clu.get_nx()
                ),
                dims=['time', y_name, x_name],
                coords={
                    'time': (["time"], data.coords['time'].values),
                    y_name: ([y_name], data.coords[y_name].values),
                    x_name: ([x_name], data.coords[x_name].values),
                    lat_name: ([y_name, x_name], data.coords[lat_name].values),
                    lon_name: ([x_name, x_name], data.coords[lon_name].values),
                },
                attrs=data[varname].attrs
            )

            # Append data to list
            # -------------------

            predicted_da_list.append(predicted)

        # Merge downscaled data to DataSet and return
        # -------------------------------------------

        ds_predicted = xr.merge(predicted_da_list)

        # Copy attributes
        # ---------------

        ds_predicted.attrs = data.attrs

        return ds_predicted
