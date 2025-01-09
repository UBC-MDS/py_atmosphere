def mach_number(altitude, units, speed):
    """
    Calculate the mach number of an object moving at a given altitude.

    Given an altitude, and assumptions of air composition, this function calculates the speed of sound in m/s in specific altitude 
    given -> speed of sound = c = sqrt(gamma*R*T), where gamma and R are standard air properties. Then it calculates the Mach number of
    an object moving in said environment.

    Parameters:
    ----------
    altitude : float
        A numeric value that represents the altitude of interest. This value is the reference to extract air properties, specifically, temperature, pressure and density.
    alt_units : str
        Units of the altitude input to function. Valid units are: m (meters), km (kilometers), ft (feet), miles (miles)
    speed: float
        Speed of object moving in m/s

    Returns:
    -------
    Float
        Mach number (adimensional) in specific altitude given -> Mach = speed / speed of sound as calculated in speed_of_sound function.

    Examples
    --------
    >>>mach_number(0.0, "ft", 340.4)
    1.0
    """
    pass