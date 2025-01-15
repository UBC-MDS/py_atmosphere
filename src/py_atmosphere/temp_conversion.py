def temp_conversion(properties_ICAO_list, property, desired_unit):
    """
    Convert the units of a selected atmospheric property.

    Parameters:
    ----------
    properties_ICAO_list : List
        A four-element list that describes the inputed altitude (km), along with the temperature (Celsius), pressure (Pascal) and density (kg/m3) of the air. 
        This is typically the output of `properties_ICAO` function.
    property : str
        Selected property for which units need to be changed. Valid inputs are: "altitude", "temperature", "pressure"
    desired_unit : str
        The desired units for the selected property.
        Valid units for temperature: C (Celsius), F (Fahrenheit), K (Kelvin), R (Rankine)
        Valid units for altitude: m (meters), km (kilometers), ft (feet), miles (miles)
        Valid units for pressure: bar (bar), Pa (Pascal), psia (Pounds over square inch)

    Returns:
    -------
    list
        A four-element list with the selected property converted to the specified units.

    Examples
    --------
    >>> temp_conversion([0.0, 288.15, 101325, 1.225], "temperature", "K")
    [0.0, 288.15, 101325, 1.225]
    """
    # Extract the values from the input list
    altitude, temperature, pressure, density = properties_ICAO_list

    # Conversion for temperature
    if property.lower() == "temperature":
        if desired_unit == "F":
            temperature = (temperature * 9/5) + 32
        elif desired_unit == "K":
            temperature = temperature + 273.15
        elif desired_unit == "R":
            temperature = (temperature + 273.15) * 9/5
        elif desired_unit == "C":
            temperature = temperature  # No conversion needed for Celsius
        else:
            raise ValueError("Invalid desired_unit for temperature")

    # Conversion for altitude
    elif property.lower() == "altitude":
        if desired_unit == "m":
            altitude = altitude * 1000  # km to m
        elif desired_unit == "km":
            altitude = altitude  # No conversion needed for km
        elif desired_unit == "ft":
            altitude = altitude * 3280.84  # km to feet
        elif desired_unit == "miles":
            altitude = altitude * 0.621371  # km to miles
        else:
            raise ValueError("Invalid desired_unit for altitude")

    # Conversion for pressure
    elif property.lower() == "pressure":
        if desired_unit == "Pa":
            pressure = pressure  # No conversion needed for Pascal
        elif desired_unit == "bar":
            pressure = pressure / 100000  # Pascal to bar
        elif desired_unit == "psia":
            pressure = pressure * 0.000145038  # Pascal to pounds per square inch (absolute)
        else:
            raise ValueError("Invalid desired_unit for pressure")

    else:
        raise ValueError("Invalid property. Valid options are 'altitude', 'temperature', or 'pressure'")

    # Return the updated list with the converted value
    return [altitude, temperature, pressure, density]

    
