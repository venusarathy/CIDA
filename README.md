A simple CIpher Decoder App(CIDA).

For now Basic terminal is used to display infos.

This project provides a tool to decode and decrypt various encoded or ciphered strings by applying multiple permutations of decoding functions up to three levels of depth.

## Project Structure

- `decoders.py`: Contains all decoding functions.
- `permutations.py`: Handles permutations and processing logic.
- `utils.py`: Utility functions for input handling and output formatting.
- `main.py`: Main script for executing the decoding process.

## Usage

Run the `main.py` script to decode the input string using different permutations of decoding functions.

```bash
python main.py


### Summary

With this modular structure:

- **Scalability**: You can easily add new decoding functions in `decoders.py`.
- **Maintainability**: Each file has a clear responsibility, making the code easier to maintain and debug.
- **Extensibility**: The modular design allows you to extend the functionality (e.g., adding new levels of depth or more complex decoders) without disrupting the existing codebase.


