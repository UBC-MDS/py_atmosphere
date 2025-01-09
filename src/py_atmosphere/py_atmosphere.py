def py_atmosphere(altitude, alt_units):
    """
    Display standard ICAO air properties given altitude input.

    Given an altitude entered with specified units, this function first transforms the altitude units to a standard in order to read a 
    table that associates altitude with standard air temperature, pressure and density according to the ICAO standard atmosphere.
    It outputs the air properties in degrees Celsius (temperature), Pascal (Pressure) and kg/m3 (density)

    Parameters:
    ----------
    altitude : float
        A numeric value that represents the altitude of interest. This value is the reference to extract air properties, specifically, temperature, pressure and density.
    alt_units : str
        Units of the altitude input to function. Valid units are: m (meters), km (kilometers), ft (feet), miles (miles)

    Returns:
    -------
    List
        Four element list that describes the inputed altitude (km), along with the temperature (Celsius), pressure (Pascal) and density (kg/m3) of the air.

    Examples
    --------
    >>>py_atmosphere(0.0, "ft")
    [0.0, 15, 101325, 1.225]
    """
    pass