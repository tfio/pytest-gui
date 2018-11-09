'''
Module for creating a project and running main Loop
'''

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

from view import MainWindow
from model import UnittestProject


def main_loop(Model=UnittestProject):
    '''Run the main loop of the app.
    '''
    # Set up the root Tk context
    root = Tk()

    # Construct an empty window
    view = MainWindow(root)

    # Load the project model
    view.project = view.load_project(root, Model)

    # Run the main loop
    view.mainloop()

if __name__ == "__main__":
    main_loop()
