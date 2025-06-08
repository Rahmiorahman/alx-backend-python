# utils.py

def access_nested_map(nested_map, path):
    """Access a value in a nested dictionary using a tuple path."""
    for key in path:
        nested_map = nested_map[key]
    return nested_map
