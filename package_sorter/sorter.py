"""
Package Sorter Module

This module provides functionality for sorting packages based on their dimensions and mass.
It uses the pint library for unit handling and defines an enumeration for different stack types.

Usage:
    from package_sorter.sorter import sort, Stack
    result = sort(width_cm=10, height_cm=20, length_cm=30, mass_kg=5)

Dependencies:
    - pint: For handling units and conversions
"""

from enum import Enum
import pint

# Initialize the unit registry
ureg = pint.UnitRegistry()

class Stack(Enum):
    STANDARD = "STANDARD"
    SPECIAL = "SPECIAL"
    REJECTED = "REJECTED"

class PackageDimensionError(ValueError):
    """Raised when package dimensions are invalid."""
    pass

class PackageMassError(ValueError):
    """Raised when package mass is invalid."""
    pass

def sort(width_cm: float, height_cm: float, length_cm: float, mass_kg: float) -> Stack:
    """
    Sort packages based on their dimensions and mass.

    Args:
        width_cm (float): Width of the package in centimeters.
        height_cm (float): Height of the package in centimeters.
        length_cm (float): Length of the package in centimeters.
        mass_kg (float): Mass of the package in kilograms.

    Returns:
        Stack: The stack where the package should be sorted.

    Raises:
        PackageDimensionError: If any dimension is not a positive non-zero value.
        PackageMassError: If mass is not a positive non-zero value.
    """
    # Validate input: dimensions and mass must be positive
    if width_cm <= 0 or height_cm <= 0 or length_cm <= 0:
        raise PackageDimensionError("Dimensions must be positive non-zero values.")
    
    if mass_kg <= 0:
        raise PackageMassError("Mass must be a positive non-zero value.")
    
    # Convert dimensions to centimeters and mass to kilograms
    width = width_cm * ureg.centimeter
    height = height_cm * ureg.centimeter
    length = length_cm * ureg.centimeter
    mass = mass_kg * ureg.kilogram

    # Calculate the volume in cubic centimeters (cm³)
    volume = width * height * length

    # Define the bulky and heavy criteria
    is_bulky = volume >= 1_000_000 * ureg.cubic_centimeter or \
               width >= 150 * ureg.centimeter or \
               height >= 150 * ureg.centimeter or \
               length >= 150 * ureg.centimeter

    is_heavy = mass >= 20 * ureg.kilogram

    # Use match (Python 3.10+) to dispatch based on conditions
    match (is_bulky, is_heavy):
        case (True, True):
            return Stack.REJECTED
        case (True, False) | (False, True):
            return Stack.SPECIAL
        case (False, False):
            return Stack.STANDARD

