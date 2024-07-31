from color_mapping import MAJOR_COLORS, MINOR_COLORS, get_pair_number_from_color

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

if __name__ == '__main__':
    print(generate_reference_manual())
