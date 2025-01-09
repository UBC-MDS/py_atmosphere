def temp_conversion(properties_ICAO_list, property, desired_unit):
    """
    Change the units of a selected property.

    Parameters:
    ----------
    properties_ICAO_list : List
        Four element list that describes the inputed altitude (km), along with the temperature (Celsius), pressure (Pascal) and density (kg/m3) of the air. 
        Valid for output from "properties_ICAO" function.
    property : str
        Selected property for which units need to be changed. Valid inputs are: "altitude", "temperature", "pressure"
    desired_unit : str
        Desired units for the selected property.
        Valid units for temperature: C (Celsius), F (Fahrenheit), K (Kelvin), R (Rankine)
        Valid units for altitude: m (meters), km (kilometers), ft (feet), miles (miles)
        Valid units for pressure: bar (bar), Pa (Pascal), psia (Pounds over square inch)

    Returns:
    -------
    List
        Returns a four element list with values transformed into the indicated units.

    Examples
    --------
    >>>temp_conversion([0.0, 288.15, 101325, 1.225], "temperature", "K")
    [0.0, 288.15, 101325, 1.225]
    """
    