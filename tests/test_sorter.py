import pytest
from package_sorter.sorter import sort, Stack, PackageDimensionError, PackageMassError

def test_sort():
    assert sort(70, 80, 90, 5) == Stack.STANDARD
    assert sort(200, 100, 50, 10) == Stack.SPECIAL  # Bulky by volume
    assert sort(150, 100, 100, 5) == Stack.SPECIAL  # Bulky by dimension
    assert sort(100, 100, 99, 25) == Stack.SPECIAL  # Heavy
    assert sort(200, 200, 100, 25) == Stack.REJECTED  # Both bulky and heavy
    assert sort(99.9, 99.9, 99.9, 19.9) == Stack.STANDARD  # Borderline STANDARD
    assert sort(150, 150, 150, 20) == Stack.REJECTED  # Borderline REJECTED


def test_invalid_input():
    with pytest.raises(PackageDimensionError):
        sort(0, 100, 100, 5)  # Invalid: width is 0
    with pytest.raises(PackageDimensionError):
        sort(-100, 100, 100, 5)  # Invalid: negative dimension
    with pytest.raises(PackageMassError):
        sort(100, 100, 100, 0)  # Invalid: mass is 0
    with pytest.raises(PackageMassError):
        sort(100, 100, 100, -5)  # Invalid: negative mass
