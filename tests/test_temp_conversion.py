import pytest
from py_atmosphere.temp_conversion import temp_conversion 
import math

@pytest.mark.parametrize("properties, property_to_change, desired_unit, expected_result", [
    ([0.0, 15.04, 101325], "temperature", "K", [0.0, 288.19, 101325]),  
    ([0.0, 15.04, 101325], "temperature", "F", [0.0, 59.07, 101325]),  
    ([0.0, 15.04, 101325], "pressure", "bar", [0.0, 15.04, 1.01325]),  
    ([0.0, 15.04, 101325], "pressure", "psia", [0.0, 15.04, 14.696]),  
    ([1000.0, 8.54, 89874], "altitude", "km", [1.0, 8.54, 89874]),  
    ([1000.0, 8.54, 89874], "altitude", "ft", [3280.84, 8.54, 89874]),  
    ([1000.0, 8.54, 89874], "altitude", "miles", [0.621371, 8.54, 89874]),  
])
def test_valid_conversion(properties, property_to_change, desired_unit, expected_result):
    """Test valid conversions for temperature, altitude, and pressure."""
    result = temp_conversion(properties, property_to_change, desired_unit)
    
    # Assert each element of the result is close to the expected result with an appropriate tolerance
    assert math.isclose(result[0], expected_result[0], abs_tol=0.01), (
        f"Failed for properties={properties}, property={property_to_change}, "
        f"desired_unit={desired_unit}. Expected altitude {expected_result[0]}, got {result[0]}."
    )
    assert math.isclose(result[1], expected_result[1], abs_tol=0.01), (
        f"Failed for properties={properties}, property={property_to_change}, "
        f"desired_unit={desired_unit}. Expected temperature {expected_result[1]}, got {result[1]}."
    )
    assert math.isclose(result[2], expected_result[2], abs_tol=0.01), (
        f"Failed for properties={properties}, property={property_to_change}, "
        f"desired_unit={desired_unit}. Expected pressure {expected_result[2]}, got {result[2]}."
    )


@pytest.mark.parametrize("properties, property_to_change, desired_unit", [
    ([0.0, 15.04, 101325], "temperature", "Celsius"),  # Invalid temperature unit
    ([1000.0, 8.54, 89874], "altitude", "meters"),  # Invalid altitude unit
    ([0.0, 15.04, 101325], "pressure", "atm"),  # Invalid pressure unit
])
def test_invalid_unit_error(properties, property_to_change, desired_unit):
    """Test error handling for invalid units."""
    with pytest.raises(ValueError):
        temp_conversion(properties, property_to_change, desired_unit)


@pytest.mark.parametrize("properties, property_to_change, desired_unit", [
    ([0.0, 15.04, 101325], "speed", "K"),  # Invalid property
])
def test_invalid_property_error(properties, property_to_change, desired_unit):
    """Test error handling for invalid property."""
    with pytest.raises(ValueError):
        temp_conversion(properties, property_to_change, desired_unit)


def test_no_conversion_needed():
    """Test if no conversion is performed when requested unit matches the current unit."""
    properties = [0.0, 15.04, 101325]
    result = temp_conversion(properties, "temperature", "C")
    assert result == properties, "No conversion should occur when the desired unit matches the current unit."

    result = temp_conversion(properties, "altitude", "m")
    assert result == properties, "No conversion should occur when the desired unit matches the current unit."

    result = temp_conversion(properties, "pressure", "Pa")
    assert result == properties, "No conversion should occur when the desired unit matches the current unit."
