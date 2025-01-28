import pytest
from py_atmosphere_ubc.mach_number import mach_number
import math


@pytest.mark.parametrize("altitude, alt_units, speed", [
    (0.0, "m", 340.29),  
    (11000.0, "m", 295.0),  
    (25000.0, "m", 250.0),  
])
def test_output_type_postive(altitude, alt_units, speed):
    """Test output for type and postive number."""
    result = mach_number(altitude, alt_units, speed)
    assert result > 0, "Mach number must be positive."
    assert isinstance(result, float), "Mach number must be a float."

@pytest.mark.parametrize("altitude, alt_units, speed, expected_mach", [
    (0.0, "m", 340.29, 1.0),  
    (11000.0, "m", 295.0, 1.0),  
    (25000.0, "m", 250.0, 0.847),  
])
def test_valid_calculation(altitude, alt_units, speed, expected_mach):
    """Test mach_number calculations"""
    result = mach_number(altitude, alt_units, speed)
    assert math.isclose(result, expected_mach, abs_tol=0.01), (
        f"Failed for altitude={altitude}, units={alt_units}, speed={speed}. "
    )
    
def test_invalid_speed_type_error():
    """Test error handling when speed is not a numeric value."""
    with pytest.raises(TypeError, match="Speed must be a numeric value."):
        mach_number(0.0, "m", "speed")


def test_invalid_speed_value_error():
    """Test error handling when speed is a negative value."""
    with pytest.raises(ValueError, match="Speed must be a non-negative."):
        mach_number(0.0, "m", -1)


@pytest.mark.parametrize("altitude, alt_units, speed", [
    (-1, "m", 340.29),  # invalid altitude
    (11000.0, "unit", 295.0),  # invalid unit
    (25100.0, "m", 250.0),  # exceeds model maximum altitude
])
def test_invalid_altitude_unit(altitude, alt_units, speed):
    """Test error handling for invalid altitude and units."""
    with pytest.raises(ValueError):
        mach_number(altitude, alt_units, speed)