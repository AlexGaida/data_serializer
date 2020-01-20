"""
Get the path names for this project.
Check if file names and directories are valid.
"""

# import standard modules
import os
import re
import os.path as path

# define private variables
__version__ = "1.0.0"

# define global variables
IGNORE_FILES = ["serialize_template.py", "__init__.py"]
SERIALIZER_NAMES = ["serialize"]
MODULE_PATH = __file__
MODULE_DIR = os.path.dirname(__file__)
OUTPUT_PATH = path.join(MODULE_DIR, os.pardir, "output")
SERIALIZER_PATH = path.join(MODULE_DIR, 'serializers')
ALTERNATIVE_SERIALIZER_PATH = path.join(MODULE_DIR, 'alternative_serializers')

INPUT_DATA_FILE = path.join(MODULE_DIR, os.pardir, "personal_data.csv")
OUTPUT_FILE_STR = "personal_data"


def __convert_bytes(num):
    """
    this function will convert bytes to MB.... GB... etc
    """
    num = num.st_size
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0


def check_file_size(file_name=""):
    """
    checks the file size of the file name supplied.
    :param file_name: <str> file name.
    :return: <str> file size.
    """
    if check_file(file_name):
        file_info = os.stat(file_name)
        return __convert_bytes(file_info)
    return False


def find_output_files():
    """
    finds all the output files.
    :return:
    """


def check_input_data_file():
    """
    checks the input data file for discrepancies.
    :return: <bool> True for acceptable use. <bool> False for cannot use file.
    """
    return check_file(INPUT_DATA_FILE)


def find_serializers(files=False, names=False, alternative=False):
    """
    finds serializers.
    :return: <list> supported serializer list. <bool> False for failure.
    """
    # return only the nice file names
    if alternative:
        serials = filter(
            lambda x: '.pyc' not in x and '.py' in x and '__init__' not in x, os.listdir(ALTERNATIVE_SERIALIZER_PATH)
        )
    else:
        serials = filter(
            lambda x: '.pyc' not in x and '.py' in x and '__init__' not in x, os.listdir(SERIALIZER_PATH)
        )

    if not serials:
        return False

    # filters the the unecessary files from list
    if files:
        return filter(lambda x: x not in IGNORE_FILES, serials)

    # strips the files of the ".py" and "serialize_" strings from the file names
    if names:
        ret_names = []
        for serial in serials:
            if serial in IGNORE_FILES:
                continue
            serial = serial.replace('.py', '')
            for accepted_name in SERIALIZER_NAMES:
                if accepted_name in serial:
                    nice_name = re.sub(accepted_name+'_', '', serial)
            ret_names.append(nice_name)
        return ret_names
    return False


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
