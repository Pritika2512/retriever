import sys

def test_python_version_compatibility():
    """
    Ensure the project runs on supported Python versions.
    """
    assert sys.version_info >= (3, 8)