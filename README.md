# py_atmosphere

Package intended to use the ICAO Standard Atmosphere to display its standard air properties and calculate the Mach number of a moving object in space at a particular altitude.

## Contributors 

- Francisco Ramirez
- Zhengling Jiang 
- Tianjiao Jiang

## About

Functions included in package:
- py_atmosphere.py: Function calculates the ICAO standard ambient temperature, pressure and density of the air at a given altitude and displays it. 
- temp_conversion.py: Function does temperature unit conversion to a variaty of units for ambient conditions that describe the ICAO standard atmosphere.
- mach_number.py: Given an altitude, function calculates the speed of sound in the embient conditions and calculates the Mach number for the speed of an object moving in the same environment.

To do: a paragraph describing where your packages fit into the Python ecosystem (are there any other Python packages that have the same/similar functionality? Provide links to any that do. If none exist, then clearly state this as well).

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
