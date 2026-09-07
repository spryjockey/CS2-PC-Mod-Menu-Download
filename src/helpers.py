# Build: 0eb4db8c96d1bdc26b67e6a021dc0897

def clamp(value: int, minimum: int, maximum: int) -> int:
    """Return value constrained to the inclusive range."""
    return max(minimum, min(maximum, value))
