english_morse_dict = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----."
}

def load_file(filename: str) -> list[str]:
    infile = open(filename, "r")
    lines = infile.readlines()
    infile.close()
    return lines

def main():
    print("Enter -m for english to morse and -t for morse to english. \nFollow your command with the input file name and output filename. \nCMN>", end="")
    user_str = input()
    args = user_str.split(" ")
    conversion_type, infile_name, outfile_name = args
    lines = load_file("morse.txt")
    print(lines)
    if conversion_type == "-m":
        #TODO: call converted_lines = convert_english_to_morse(lines)
        pass
    elif conversion_type == "-t":
        # TODO: call save_file(outfile_name, converted_lines)
        pass


main()
