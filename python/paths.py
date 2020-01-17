"""
Get the path names for this project.
Check if file names and directories are valid.
"""

# import standard modules
import os
import os.path as path

# define global variables
IGNORE_FILES = ["serialize_template.py", "__init__.py"]

MODULE_PATH = __file__
MODULE_DIR = os.path.dirname(__file__)
OUTPUT_PATH = path.join(MODULE_DIR, os.pardir, "output")
SERIALIZER_PATH = path.join(MODULE_DIR, 'serializers')
ALTERNATIVE_SERIALIZER_PATH = path.join(MODULE_DIR, 'alternative_serializers')

INPUT_DATA_FILE = path.join(MODULE_DIR, os.pardir, "personal_data.csv")
OUTPUT_FILE_STR = "personal_data"


def check_input_data_file():
    """
    Checks the input data file for discrepancies.
    :return: <bool> True for acceptable use. <bool> False for cannot use file.
    """
    return check_file(INPUT_DATA_FILE)


def find_serializers(files=False, names=False, alternative=False):
    """
    finds serializers.
    :return: <list> supported serializer list. <bool> False for failure.
    """
    if alternative:
        serials = filter(lambda x: '.pyc' not in x, os.listdir(ALTERNATIVE_SERIALIZER_PATH))
    else:
        serials = filter(lambda x: '.pyc' not in x, os.listdir(SERIALIZER_PATH))
    if not serials:
        return False
    if files:
        return filter(lambda x: x not in IGNORE_FILES, serials)
    if names:
        return [x.split('.')[0].split('_')[-1] for x in serials if x not in IGNORE_FILES]


def join(args):
    """
    join path names.
    :param args: <tuple>, <list> path strings.
    :return: <str> joined path.
    """
    return path.join(*args)


def check_file(f_path=""):
    """
    checks the path name validity.
    :param f_path: <str> file path name.
    :return: <bool> True for success. <bool> False for failure.
    """
    return path.isfile(f_path)


def check_dir(f_path=""):
    """
    checks the path directory validity.
    :param f_path: <str> file path name.
    :return: <bool> True for success. <bool> False for failure.
    """
    # check if an extension is in the file path parameter
    if "." in f_path:
        f_path = path.dirname(f_path)
    return path.isdir(f_path)
