# py_atmosphere

The International Standard Atmosphere (ISA) is an atmospheric model of how pressure, temperature, density of the Earth's atmosphere change over a wide range of altitudes. It is published by the International Organization for Standardization (ISO) as an International Standard ISO 2533:1975 (https://www.iso.org/standard/7472.html).

The International Civil Aviation Organization (ICAO - https://www.icao.int/Pages/default.aspx) uses this atmospheric models as baseline in its own standard enforcing. This standard is extensively used in the Aerospace industry for aircraft and engine design tasks considering operational envelopes.

As simplified, but useful atmospheric model was created by NASA's Glenn Research Center for academic purposes (https://www.grc.nasa.gov/www/k-12/airplane/atmosmet.html#:~:text=In%20the%20troposphere%2C%20the%20temperature,atmosphere%20model%20is%20also%20available).

This package contains the simplified NASA's GRC Earth Atmospheric model and calculates atmospheric air properties for an altitude of interest, as well as supports Mach number calculation for a moving object in space at the same altitude.

## Package Functions

The package includes the following Functions included in package:

- `py_atmosphere.py` - Function calculates the NASA's GRC ambient temperature, pressure and density of the air at a given altitude (from 0 to 25,000 meters).
- `temp_conversion.py` -  Function does temperature unit conversion to a variety of units for ambient conditions that describe the atmospheric model.
- `mach_number.py` - Given an altitude, function calculates the speed of sound in the embient conditions and calculates the Mach number for the speed of an object moving in the same environment.

## py_atmosphere in the Python Ecosystem

There are multiple Python packages in the ecosystem that have the similar characteristics particularly when it comes to characterization of the standards atmopheres. Existing packages with similar functionalities, particularly for ICAO standard calculations:

- atmos - programming utilities for atmospheric sciences (https://pypi.org/project/atmos/)
- metpy - reading, visualization and performing calculations with weather data (https://pypi.org/project/MetPy/)
- pyatmos - archive of routines that estimate the vertical structure of atmosphere with various density models (https://pypi.org/project/pyatmos/)

## Unique features of py_atmosphere

Use of the standard model on practical aerospace applications is quite limited. This package stands out given its unique blend of reference standards on practical design calculations, tailored for individuals with little to no technical expertise of the Aerospace industry and aircraft design. Here is what sets `py_atmosphere` apart:

- Package avoids complexity by performing simple, transparent calculations of high value on aircraft design parameters, applying a simple interpretable atmospheric model (NASA's GRC).
- Makes use of the standard for calculation on simple physical parameters such as speed of sound and Mach number for a moving object.

## Installation

```bash
$ pip install py_atmosphere
```

## Usage

- Usage examples will be added in a future release.

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`py_atmosphere` was created by Tianjiao Jiang, Zhengling Jiang, Francisco Ramirez. It is licensed under the terms of the MIT license.

## Credits

`py_atmosphere` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).

## Contributors 

- Francisco Ramirez
- Zhengling Jiang 
- Tianjiao Jiang
