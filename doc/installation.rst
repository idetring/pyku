Installation
============

.. rubric:: Too Long; Didn't Read

To install pyku, ensure your system is properly configured:

* System Binaries: ``geos``, ``udunits``, ``hdf5``, ``netcdf``, and ``proj``,
  as well as
* ``pandoc`` to build the documentation.
* Environment: Create and activate a clean virtual environment.
* Connectivity: Ensure an active internet connection is available.

Once these prerequisites are met, you can install the latest release of pyku
using the command ``pip install``.

.. code:: bash

   # Install the latest stable pyku release
   # --------------------------------------

   pip3 install pyku \
     --index-url https://gitlab.dwd.de/api/v4/projects/1719/packages/pypi/simple

   # Install extra dependencies to build documentation
   # -------------------------------------------------

   pip3 install pyku[documentation] \
     --index-url https://gitlab.dwd.de/api/v4/projects/1719/packages/pypi/simple

Upgrade
-------

This command installs or updates to the latest version.

.. code:: bash

   pip3 install pyku --upgrade \
   --index-url https://gitlab.dwd.de/api/v4/projects/1719/packages/pypi/simple

Downgrade
---------

By specifying an exact version, it can also be used to downgrade pyku:

.. code:: bash

   pip3 install pyku==0.11 \
   --index-url https://gitlab.dwd.de/api/v4/projects/1719/packages/pypi/simple

System Dependencies
-------------------

The following non-python dependencies are required:

* `geos <https://libgeos.org/>`_
* `proj <https://proj.org/>`_
* `hdf5 <https://www.hdfgroup.org/solutions/hdf5/>`_
* `netcdf <https://www.unidata.ucar.edu/software/netcdf/>`_
* `udunits <https://www.unidata.ucar.edu/software/udunits/>`_

from pip
--------

To install the latest release from the registry:

.. code:: bash

   pip3 install pyku \
        --index-url https://gitlab.dwd.de/api/v4/projects/1719/packages/pypi/simple

from master
-----------

To install the current master from the repository:

.. code:: bash

   pip3 install git+https://gitlab.dwd.de/ku/libraries/pyku

from source
-----------

To install from source you will need to clone the repository first.

.. code:: bash

   pip install .

for development
---------------

To install in development mode:

.. code:: bash

   pip install -e .

Optional packages
-----------------

To install the necessary packages for building the documentation, including all
Sphinx dependencies and Jupyter, use this setup. These packages will be
installed automatically, making it an excellent starting point.

.. code:: bash

   pip install pyku[documentation]\
       --index-url https://gitlab.dwd.de/api/v4/projects/1719/packages/pypi/simple

Bindings to CDO should generally be avoided within the scope of pyku. However,
there is one exception: a function required for derotating wind components in
rotated model data. This functionality is isolated from the rest of the code
and can be installed using:

.. code:: bash

   pip install pyku[cdo_bindings]\
       --index-url https://gitlab.dwd.de/api/v4/projects/1719/packages/pypi/simple

Compiled dependencies
---------------------

The following dependencies are not installed automatically with *pyku* because
additional non-Python dependencies are required.

.. rubric:: python-SBCK

Download and install the required eigen dependency:

.. code:: bash

   wget https://gitlab.com/libeigen/eigen/-/archive/3.4.0/eigen-3.4.0.tar.gz
   mkdir build
   cd build
   cmake ../ -DCMAKE_INSTALL_PREFIX=/path/to/eigen-3.4.0/install
   export PKG_CONFIG_PATH=$PKG_CONFIG_PATH:/path/to/eigen-3.4.0/install/share/pkgconfig

Install the SBCK library from source:

.. code:: bash

   git clone https://github.com/yrobink/SBCK-python.git
   CPPFLAGS='-I/path/to/eigen-3.4.0/install/include' pip3 install SBCK

.. rubric:: Conservative resampling

There were issues with multiprocessing when using conservative resampling
within pyku. To resolve this, disable multiprocessing in the ESMF library and
allow pyku to manage multiprocessing as described below:

.. code:: bash

   # Load the apple-cake base configuration
   # --------------------------------------

   module load base/apple-cake

   # Clone repository
   # ----------------

   git clone https://github.com/esmf-org/esmf

   # Export path to esmf directory
   # -----------------------------

   export ESMF_DIR=/path/to/esmf/

   # Build
   # -----

   export ESMF_OPENACC='OFF'
   export ESMF_OPENMP='OFF'
   export ESMF_PTHREADS='OFF'
   export ESMF_PIO='OFF'
   git checkout v8.6.1
   make
   make install

   # Set that environment variable
   # -----------------------------

   export ESMFMKFILE=/path/to/esmf/DEFAULTINSTALLDIR/lib/libO/Linux.gfortran.64.mpiuni.default/esmf.mk

.. code:: bash

   pip3 uninstall esmpy  # If applicable
   cd esmf/src/addon/esmpy
   make install

.. code:: bash

   pip3 uninstall xESMF  # If applicable
   pip3 install xESMF






