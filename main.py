# Define major and minor colors
MAJOR_COLORS = ['White', 'Red', 'Black', 'Yellow', 'Violet']
MINOR_COLORS = ["Blue", "Orange", "Green", "Brown", "Slate"]

# Functions for color and number conversion

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

def generate_reference_manual():
    """
    Generate a reference manual that maps color pairs to their corresponding numbers.
    """
    manual = []
    for major_color in MAJOR_COLORS:
        for minor_color in MINOR_COLORS:
            pair_number = get_pair_number_from_color(major_color, minor_color)
            manual.append(f'Pair Number {pair_number}: {major_color} {minor_color}')
    return "\n".join(manual)

# Testing functions

def test_number_to_pair(pair_number, expected_major_color, expected_minor_color):
    """
    Test conversion from pair number to color pair.
    """
    major_color, minor_color = get_color_from_pair_number(pair_number)
    assert major_color == expected_major_color, f'Expected {expected_major_color}, but got {major_color}'
    assert minor_color == expected_minor_color, f'Expected {expected_minor_color}, but got {minor_color}'

def test_pair_to_number(major_color, minor_color, expected_pair_number):
    """
    Test conversion from color pair to pair number.
    """
    pair_number = get_pair_number_from_color(major_color, minor_color)
    assert pair_number == expected_pair_number, f'Expected {expected_pair_number}, but got {pair_number}'

def test_generate_reference_manual():
    """
    Test generation of the reference manual.
    """
    manual = generate_reference_manual()
    assert 'Pair Number 1: White Blue' in manual
    assert 'Pair Number 25: Violet Slate' in manual
    assert len(manual.split('\n')) == 25  # Ensure there are 25 pairs

# Main function to run tests and generate manual

if __name__ == '__main__':
    # Run tests
    test_number_to_pair(4, 'White', 'Brown')
    test_number_to_pair(5, 'White', 'Slate')
    test_pair_to_number('Black', 'Orange', 12)
    test_pair_to_number('Violet', 'Slate', 25)
    test_pair_to_number('Red', 'Orange', 7)
    test_generate_reference_manual()
    print('All tests passed!')
    
    # Generate and print reference manual
    print('\nReference Manual:')
    print(generate_reference_manual())
