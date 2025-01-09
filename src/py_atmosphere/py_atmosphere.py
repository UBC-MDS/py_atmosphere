def py_atmosphere(altitude, alt_units):
    """
    Display standard ICAO air properties for a given altitude.

    This function calculates standard air properties (temperature, pressure, and density) based on the ICAO standard atmosphere. 
    The input altitude, provided in a specified unit, is first converted to a standard unit (kilometers) for processing. 
    The resulting air properties are returned in degrees Celsius (temperature), Pascals (pressure), and kilograms per cubic meter (density).

    Parameters:
    ----------
    altitude : float
        A numeric value that represents the altitude of interest. This value is the reference to extract air properties, specifically, temperature, pressure and density.
    alt_units : str
        The unit of the input altitude. Valid units are: m (meters), km (kilometers), ft (feet), miles (miles)

    Returns:
    -------
    list
        A list containing four elements that describes the inputed altitude (km), along with the temperature (Celsius), pressure (Pascal) and density (kg/m3) of the air.

    Examples
    --------
    >>> py_atmosphere(0.0, "ft")
    [0.0, 15, 101325, 1.225]
    """
    pass