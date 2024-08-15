from decoders import hex_to_text, decimal_to_text, octal_to_text, base64_to_text, rot13_to_text, caesar_to_text
from permutations import process_permutations, generate_permutations
from utils import print_banner, get_input_string

if __name__ == "__main__":
    input_str = get_input_string()

    # list of all conversion functions - have to update here when new decoder is added.
    conversion_functions = [
        hex_to_text,
        decimal_to_text,
        octal_to_text,
        base64_to_text,
        rot13_to_text,
        caesar_to_text
    ]

    # First Level: Single function application
    print_banner("First")
    process_permutations(input_str, [(func,) for func in conversion_functions])

    # Second Level: Two-function permutations
    print_banner("Second")
    process_permutations(input_str, generate_permutations(conversion_functions, 2))

    # Third Level: Three-function permutations
    print_banner("Third")
    process_permutations(input_str, generate_permutations(conversion_functions, 3))

