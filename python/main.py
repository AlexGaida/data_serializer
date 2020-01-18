"""
Main interactive module for serializing the personal_data.csv data file.
"""

# define standard imports
import argparse
import imp
import webbrowser
import unittest
import os
import subprocess
from sys import platform

# define custom imports
import paths
import tests


# define global variables
SERIALIZERS = paths.find_serializers(names=1)
ALT_SERIALIZERS = paths.find_serializers(alternative=1, names=1)
OUTPUT_PATH = paths.OUTPUT_PATH
INPUT_DATA_FILE = paths.INPUT_DATA_FILE


def run_serializer(serializer_type=""):
    """
    runs the chosen serializer.
    :param serializer_type: <str> serializer type.
    :return: <Class> SerializeFile.
    """
    serializer_name = "serialize_" + serializer_type
    print("[Serializer_Name] :: {}".format(serializer_name))
    if "_alt_" in serializer_name:
        path_name = paths.ALTERNATIVE_SERIALIZER_PATH
    else:
        path_name = paths.SERIALIZER_PATH
    fp, pathname, description = imp.find_module(serializer_name, [path_name])
    serializer_module = imp.load_module(serializer_name, fp, pathname, description)

    # instantiate the chosen serializer file class
    return serializer_module.SerializeFile()


def display_serializer(serializer_class=None):
    """
    display the serializer class
    :param serializer_class:
    :return: <True> for success.
    """
    if serializer_display == 1:
        # display on the command line
        serializer_class.display(dsp_type=1)

    elif serializer_display == 2:
        # open a web browser to display the serialized document
        serializer_class.display(dsp_type=2)
        # webbrowser.open_new_tab(srl_cls.OUTPUT_PATH)
        webbrowser.open_new_tab(serializer_class.OUTPUT_HTML_PATH)

    elif serializer_display == 3:
        # display the serialized document on a notepad
        serializer_class.display(dsp_type=2)
        # webbrowser.open(srl_cls.OUTPUT_HTML_PATH)
        if platform == "win32":
            subprocess.Popen(['notepad.exe', serializer_class.OUTPUT_PATH])
        elif platform in ("linux", "linux2"):
            subprocess.Popen(['gedit', serializer_class.OUTPUT_PATH])
    else:
        serializer_class.write()
    return True


def get_serializer_pretty_names():
    """
    Prettify the naming of available serializers.
    :return: <str> supported serializer lists. <bool> False for failure.
    """
    ret_str = "\n\n------- SUPPORTED SERIALIZERS -------\n"
    ret_str += '\n '.join(SERIALIZERS)
    ret_str += "\n\n------ ALTERNATIVE SERIALIZERS -------\n"
    ret_str += '\n '.join(ALT_SERIALIZERS)
    return ret_str


if __name__ in "__main__":
    """
    Default serializer: JSON.
    """
    parser = argparse.ArgumentParser(description="Let's serialize this data file.")
    parser.add_argument(
        "--type", default="", type=str, choices=SERIALIZERS,
        help="This is the serializer data type parameter.")
    parser.add_argument(
        "--display", default=0, choices=[1, 2, 3], type=int,
        help="When true, display the output serialized file.")
    parser.add_argument(
        "--query", default=0, choices=[0, 1], type=int,
        help="When true, display all supported serializers.")
    parser.add_argument(
        "--alt", default="", type=str, choices=ALT_SERIALIZERS,
        help="When this is supplied, alternative serializers are used instead.")
    parser.add_argument(
        "--tests", default=0, type=int, choices=[0, 1],
        help="Run unittest on all available serializers. This procedure will be timed.")

    args = parser.parse_args()
    serializer_type = args.type
    serializer_query = args.query
    serializer_alt_type = args.alt
    serializer_display = args.display
    serializer_test = args.tests

    if serializer_query:
        print("Running serializer query: ")
        print(get_serializer_pretty_names())

    elif serializer_display:
        if serializer_alt_type:
            print("Displaying chosen serializer: " + serializer_alt_type)
            cls = run_serializer(serializer_type=serializer_alt_type)
        else:
            print("Displaying chosen serializer: " + serializer_type)
            cls = run_serializer(serializer_type=serializer_type)
        display_serializer(serializer_class=cls)

    elif serializer_test:
        print("Running serializer tests: ")
        tests.init_modules()
        suite = unittest.TestLoader().discover(os.path.dirname(tests.__file__), pattern="tests.py")
        unittest.TextTestRunner(verbosity=2).run(suite)

    elif serializer_type:
        print("Running chosen serializer: " + serializer_type)
        cls = run_serializer(serializer_type=serializer_type)
        cls.write()

    elif serializer_alt_type:
        print("Running chosen alternative serializer: " + serializer_alt_type)
        cls = run_serializer(serializer_type=serializer_alt_type)
        cls.write()

    else:
        print("Exiting main.")
