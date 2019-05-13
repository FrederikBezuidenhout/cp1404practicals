"""
CP1404/CP5632 Practical
Demos of various os module examples
"""

import os


def main():
    print("Starting directory is: {}".format(os.getcwd()))
    os.chdir('Lyrics')
    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))

    try:
        os.mkdir('temp')
    except FileExistsError:
        pass

    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue

        new_name = get_fixed_filename(filename)
        print("Renaming {} to {}".format(filename, new_name))


def get_fixed_filename(filename):
    new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
    return new_name


def fix_camelcase():
    filename = "CamelCase.txt"
    new_name = ''
    new_name += filename[0]
    for letter in filename[1:]:
        if letter.isupper():
            letter = '_' + letter
        new_name += letter
    print(new_name)


fix_camelcase()
#main()
