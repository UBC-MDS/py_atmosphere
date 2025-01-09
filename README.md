# py_atmosphere

The International Standard Atmospher (ISA) is an atmospheric model of how pressure, temperature, density of the Earth's atmosphere change over a wide range of altitudes. It is published by the International Organization for Standardization (ISO) as an International Standard ISO 2533:1975 (https://www.iso.org/standard/7472.html).

The International Civil Aviation Organization (ICAO) uses this atmospheric models as baseline in their own standards. This standard is extensively used in the Aerospace industry for aircraft and engine design across operational envelope.

This package contains the most basic version of the ICAO Standard Atmosphere and calculates standard atmospheric air properties for an inputed altitude, as well as supports Mach number calculation for a moving object in space at the same altitude.

## Contributors 

- Francisco Ramirez
- Zhengling Jiang 
- Tianjiao Jiang

## About

There are multiple Python packages in the ecosystem that have the similar characteristics, particularly when it comes to characterization of the standard atmophere. However, none of them have applications of the standard on minor physical calculations such as speed of sound and Mach number.

Existing packages with similar functionalities, particularly regarding containing ICAO standard calculations:

- atmos (https://pypi.org/project/atmos/)
- metpy (https://pypi.org/project/MetPy/)
- pyatmos (https://pypi.org/project/pyatmos/)

The package includes the following Functions included in package:

- py_atmosphere.py: Function calculates the ICAO standard ambient temperature, pressure and density of the air at a given altitude.
- temp_conversion.py: Function does temperature unit conversion to a variaty of units for ambient conditions that describe the ICAO standard atmosphere.
- mach_number.py: Given an altitude, function calculates the speed of sound in the embient conditions and calculates the Mach number for the speed of an object moving in the same environment.

## Installation

```bash
$ pip install py_atmosphere
```

## Usage

- TODO - Test

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`py_atmosphere` was created by Tianjiao Jiang, Zhengling Jiang, Francisco Ramirez. It is licensed under the terms of the MIT license.

## Credits

`py_atmosphere` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
