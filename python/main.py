"""
Main interactive module for serializing the personal_data.csv data file.
versions:
    1.0.0 : release version.
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

# define private variables
__version__ = "1.0.0"

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


def display_serializer(serializer_class=None, serializer_display=0):
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


def run_program(serializer_type="", serializer_alt_type="", serializer_query=0,
                serializer_display=0, serializer_test=0, serializer_all=0):
    """
    Runs the program.
    :param serializer_type: <str> Supported serializers.
    :param serializer_alt_type: <str> Alternative serializers.
    :param serializer_query: <int> 0, 1 Print serializers.
    :param serializer_display: <int> [0: Print, 1: Web Browser, 2: Notepad], Show serializer output.
    :param serializer_test: <int> 0, 1 Run Serializer unit tests.
    :param serializer_all: <int> 0, 1 Run all serializers at once.
    :return: <False> for failure.
    """
    if serializer_all:
        print("Running all available serializers: ")
        for serializer_name in SERIALIZERS + ALT_SERIALIZERS:
            print(serializer_name)
            cls = run_serializer(serializer_type=serializer_name)
            cls.write()

    if serializer_query:
        print("Running serializer query: ")
        print(get_serializer_pretty_names())

    elif serializer_display:
        if serializer_alt_type:
            print("Displaying chosen serializer: " + serializer_alt_type)
            cls = run_serializer(serializer_type=serializer_alt_type)
        elif serializer_type:
            print("Displaying chosen serializer: " + serializer_type)
            cls = run_serializer(serializer_type=serializer_type)
        else:
            print("Please choose a serializer.")
            return False
        display_serializer(serializer_class=cls, serializer_display=serializer_display)

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


def run_program_loop():
    """
    Runs the program on a loop.
    :return: None
    """
    choices = ['all', 'type', 'display', 'query', 'alt', 'tests', 'quit', 'exit']
    parser = argparse.ArgumentParser(prog='Data Serializer', description='Serializing personal data.')
    parser.add_argument('cmd', choices=choices)
    while True:
        user_input = ""
        print("Please provide arguments: {}".format(', '.join(choices)))
        input_str = raw_input("Cmd: ")
        try:
            arguments = parser.parse_args(input_str.split())
        except SystemExit:
            continue

        if arguments.cmd == 'all':
            run_program(serializer_all=1)

        if arguments.cmd == 'type':
            user_input = raw_input("Provide serializer type: ")
            if user_input in SERIALIZERS:
                run_program(serializer_type=user_input)
            else:
                print("[Invalid Name] :: Acceptable serializers:\n{}".format(SERIALIZERS))

        if arguments.cmd == 'alt':
            user_input = raw_input("Provide alternative serializer type: ")
            if user_input in ALT_SERIALIZERS:
                run_program(serializer_alt_type=user_input)
            else:
                print("[Invalid Name] :: Acceptable alternative serializers:\n{}".format(ALT_SERIALIZERS))

        if arguments.cmd == 'display':
            kargs = {}
            user_input = raw_input("Provide integers: [1: Print data, 2: Open browser, 3: Open notepad]")
            user_input = int(user_input)
            if user_input in (1, 2, 3):
                kargs["serializer_display"] = user_input
            else:
                print("[Invalid Display Input] :: Use numbers 1, 2, 3.\n"
                      "[1: Print data, 2: Open browser, 3: Open notepad]")
                return False

            user_input = raw_input("Supported or Alternative serializers? [1, 2]: ")
            user_input = int(user_input)
            if user_input == 1:
                print("Supported Serializers: {}".format(SERIALIZERS))
                serializer_input = raw_input("Provide a serializer name: ")
                if serializer_input in SERIALIZERS:
                    kargs["serializer_type"] = serializer_input
            else:
                print("Alternative Serializers: {}".format(ALT_SERIALIZERS))
                serializer_input = raw_input("Provide a alternate serializer name: ")
                if serializer_input in ALT_SERIALIZERS:
                    kargs["serializer_alt_type"] = serializer_input

            # run the program
            run_program(**kargs)

        if arguments.cmd == 'query':
            run_program(serializer_query=1)

        if arguments.cmd == 'tests':
            run_program(serializer_test=1)

        # get the users' input
        if arguments.cmd in ('quit', 'exit'):
            print("[Escape] :: Exiting program.")
            break


if __name__ in "__main__":
    """
    Run the command-line program.
    """
    parser = argparse.ArgumentParser(description="Let's serialize a data file.")
    parser.add_argument(
        "--run", default=0, type=int, choices=[0, 1],
        help="Run the program on a loop.")
    parser.add_argument(
        "--all", default=0, type=int, choices=[0, 1],
        help="run all serializers.")
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
    serializer_run = args.run
    serializer_type = args.type
    serializer_query = args.query
    serializer_alt_type = args.alt
    serializer_display = args.display
    serializer_test = args.tests
    serializer_all = args.all

    if serializer_run:
        run_program_loop()

    else:
        run_program(serializer_type=serializer_type,
                    serializer_query=serializer_query,
                    serializer_alt_type=serializer_alt_type,
                    serializer_display=serializer_display,
                    serializer_test=serializer_test,
                    serializer_all=serializer_all)

