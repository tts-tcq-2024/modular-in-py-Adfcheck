# color_mapping.py

MAJOR_COLORS = ['White', 'Red', 'Black', 'Yellow', 'Violet']
MINOR_COLORS = ["Blue", "Orange", "Green", "Brown", "Slate"]

def color_pair_to_string(major_color, minor_color):
    """
    Convert a pair of major and minor colors into a string representation.
    """
    return f'{major_color} {minor_color}'

def get_color_from_pair_number(pair_number):
    """
    Convert a pair number (1-25) to its corresponding major and minor color.
    """
    zero_based_pair_number = pair_number - 1
    major_index = zero_based_pair_number // len(MINOR_COLORS)
    if major_index >= len(MAJOR_COLORS):
        raise ValueError(f'Major index {major_index} out of range for pair number {pair_number}')
    minor_index = zero_based_pair_number % len(MINOR_COLORS)
    if minor_index >= len(MINOR_COLORS):
        raise ValueError(f'Minor index {minor_index} out of range for pair number {pair_number}')
    return MAJOR_COLORS[major_index], MINOR_COLORS[minor_index]

def get_pair_number_from_color(major_color, minor_color):
    """
    Convert a major and minor color to its corresponding pair number.
    """
    try:
        major_index = MAJOR_COLORS.index(major_color)
    except ValueError:
        raise ValueError(f'{major_color} is not a valid major color')
    try:
        minor_index = MINOR_COLORS.index(minor_color)
    except ValueError:
        raise ValueError(f'{minor_color} is not a valid minor color')
    return major_index * len(MINOR_COLORS) + minor_index + 1
