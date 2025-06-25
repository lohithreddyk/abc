from difflib import SequenceMatcher


def similarity(a: str, b: str) -> float:
    """Return a similarity ratio between two strings."""
    return SequenceMatcher(None, a, b).ratio()
