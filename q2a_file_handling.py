"""
DTS 216 - Question 2a
Read a text file, count the number of words, and write the result to another
file. Handle exceptions when the file does not exist.
"""


def count_words(input_filename, output_filename):
    try:
        with open(input_filename, "r") as infile:
            content = infile.read()
            word_count = len(content.split())

        with open(output_filename, "w") as outfile:
            outfile.write(f"The file '{input_filename}' contains {word_count} words.\n")

        print(f"Success! Word count ({word_count}) written to '{output_filename}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found. Please check the file name and try again.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    # Create a sample input file to demonstrate a successful run
    with open("sample_input.txt", "w") as f:
        f.write("Python is an easy to learn, powerful programming language. "
                "It has efficient high level data structures and a simple "
                "but effective approach to object oriented programming.")

    print("--- Attempt 1: Reading an existing file ---")
    count_words("sample_input.txt", "word_count_result.txt")

    print("\n--- Attempt 2: Reading a file that does not exist ---")
    count_words("nonexistent_file.txt", "word_count_result.txt")
