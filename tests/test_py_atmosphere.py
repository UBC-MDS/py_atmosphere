import pytest
from py_atmosphere.py_atmosphere import py_atmosphere
import math

baseline_output_0m = [0.0, 15.04, 101.29]
baseline_output_11000m = [11000.0, -56.35, 22.7349]
baseline_output_25000m = [25000.0, -56.46, 2.52227]

#Valid Input Data Type Testing

def test_invalid_altitude_type_error():
    """Test error handling when altitude is not a numeric value."""
    with pytest.raises(TypeError, match="Altitude must be a numeric value."):
        py_atmosphere("0.0", "m")

def test_invalid_altitude_value_error():
    """Test error handling when altitude is a negative value."""
    with pytest.raises(ValueError, match="Altitude must be a non-negative."):
        py_atmosphere(-1.0, "m")

#Valid Output Testing

def test_output_datatype():
    "Test output data type"
    assert isinstance(py_atmosphere(0.0, "m"), list)

@pytest.mark.parametrize("altitude, alt_units", [
    (0.0, "m"),  
    (11000.0, "m"),  
    (25000.0, "m"),  
])
def test_output_type_positive(altitude, alt_units):
    """Test output data type"""
    result = py_atmosphere(altitude, alt_units)
    assert isinstance(result[0], float), "Altitude must be a float."
    assert isinstance(result[1], float), "Temperature must be a float."
    assert isinstance(result[2], float), "Pressure must be a float."

#Valid Internal Unit Conversion

def test_alt_unit_conversion():
    """Test altitude output conversion"""
    assert py_atmosphere(0, "m")[0] == baseline_output_0m[0] , "The baseline output at 0 m is incorrect!"
    assert py_atmosphere(11000, "m")[0] == baseline_output_11000m[0], "The baseline output at 11000 m is incorrect!"
    assert py_atmosphere(11000/0.3048, "ft")[0] == baseline_output_11000m[0], "The baseline output at 11000 m is incorrect! Check ft unit conversion."
    assert py_atmosphere(11, "km")[0] == baseline_output_11000m[0], "The baseline output at 11000 m is incorrect! Check km unit conversion."
    assert py_atmosphere(11000/(1000 * 1.60934), "miles")[0] == baseline_output_11000m[0], "The baseline output at 11000 m is incorrect! Check miles unit conversion."

def test_temperature():
    """Test temperature output"""
    assert math.isclose(py_atmosphere(0, "m")[1], baseline_output_0m[1], abs_tol = 0.001), "The baseline output at 0 m is incorrect!"
    assert math.isclose(py_atmosphere(11000, "m")[1], baseline_output_11000m[1], abs_tol = 0.001), "The baseline output at 11000 m is incorrect!"
    assert math.isclose(py_atmosphere(25000, "m")[1], baseline_output_25000m[1], abs_tol = 0.001), "The baseline output at 25000 m is incorrect!"

def test_pressure():
    """Test pressure output"""
    assert math.isclose(py_atmosphere(0, "m")[2], baseline_output_0m[2], abs_tol = 0.001), "The baseline output at 0 m is incorrect!"
    assert math.isclose(py_atmosphere(11000, "m")[2], baseline_output_11000m[2], abs_tol = 0.001), "The baseline output at 11000 m is incorrect!"
    assert math.isclose(py_atmosphere(25000, "m")[2], baseline_output_25000m[2], abs_tol = 0.001), "The baseline output at 25000 m is incorrect!"

#Valid Input Altitude (Units and Range)

def test_invalid_alt_units():
    """Test Error Message if Alt Units are not correct"""
    try:
        py_atmosphere(1000, 'invalid_unit')
    except ValueError as e:
        if str(e) == "Invalid altitude unit. Valid units are: 'm', 'km', 'ft', 'miles'":
            print("ValueError raised with correct message.")
        else:
            print("ValueError raised, but the message was incorrect.")
    else:
        print("Test Failed: ValueError was not raised.")

def test_max_altitude():
    """Test Error Message if Alt value is out or fance"""
    try:
        py_atmosphere(25001, 'm')
    except ValueError as e:
        if str(e) == "Invalid altitude value. Model maximum value is 25,000 m.":
            print("ValueError raised with correct message.")
        else:
            print("ValueError raised, but the message was incorrect.")
    else:
        print("Test Failed: ValueError was not raised.")

def test_min_altitude():
    """Test Error Message if Alt value is out or fance"""
    try:
        py_atmosphere(-0.1, 'm')
    except ValueError as e:
        if str(e) == "Invalid altitude value. Model maximum value is 25,000 m.":
            print("ValueError raised with correct message.")
        else:
            print("ValueError raised, but the message was incorrect.")
    else:
        print("Test Failed: ValueError was not raised.")