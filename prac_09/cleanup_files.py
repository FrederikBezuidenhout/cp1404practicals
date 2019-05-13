"""
CP1404/CP5632 Practical
Demos of various os module examples
"""

import os


def main():
    print("Starting directory is: {}".format(os.getcwd()))
    os.chdir('Lyrics')
    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))

    for directory_name, subdirectories, filenames in os.walk('.'):
        print("Directory:", directory_name)
        print("\tcontains subdirectories:", subdirectories)
        print("\tand files:", filenames)
        print("(Current working directory is: {})".format(os.getcwd()))

        for filename in filenames:
            new_name = get_fixed_filename(filename)
            print("Renaming {} to {}".format(filename, new_name))


def get_fixed_filename(filename):

    filename = filename.replace(".TXT", ".txt")
    new_name = ''
    position = len(new_name)
    for letter in filename:
        if letter == ' ':
            letter = '_'
        if letter.isupper() and new_name[position - 1:].islower():
            new_name += '_'
        elif letter.isupper() and new_name[position - 1:].isupper():
            new_name += '_'
        new_name += letter
    return new_name


main()
