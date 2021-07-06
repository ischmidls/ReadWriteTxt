# Author: Izak Schmidlkofer
# Date(s): 2021
# Description: class TxtFile represents a text file;


class TxtFile:
    """
    Represents a text file
    Attributes: file_name: string
    Methods: f()
    """

    def __init__(self, file_name='test.txt'):
        """Returns a text file object"""

        self.file_name = file_name
        self.file_list = []

    def text_list(self):
        """
        Read file to list

        Takes None
        Returns None
        """

        with open(self.file_name, 'r') as file:
            for line in file:
                self.file_list.append(line.strip())

    def f(self):
        """
        Takes
        Returns
        """

        return

    def write_text(self):
        """
        Write list to file

        Takes None
        Returns None
        """

        with open("new_text.txt", 'w') as file:
            for line in self.file_list:
                file.write(f"{line}\n")


def main():
    """
    The program calls this function when run as a script.
    It is for basic testing.
    """

    name_input = input("Type text file name: ")
    text_file = TxtFile(name_input)

    try:
        text_file.text_list()
        text_file.write_text()
    except FileNotFoundError:
        pass
    else:
        print('done')


if __name__ == "__main__":
    main()
