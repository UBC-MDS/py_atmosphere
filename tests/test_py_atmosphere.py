from py_atmosphere.py_atmosphere import py_atmosphere
import math

baseline_output_0m = [0.0, 15.04, 101.29]
baseline_output_11000m = [11000.0, -56.35, 22.7349]
baseline_output_25000m = [25000.0, -56.46, 2.52227]

#Test input type

#Test plot

def test_output_datatype():
    "Test output data type"
    assert isinstance(py_atmosphere(0.0, "m"), list)

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