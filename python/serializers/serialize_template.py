"""
This is a template reader/ writer class.
"""
# import standard modules
import pprint as pprint
import csv
import re

# import custom modules
import paths

# define global variables
INPUT_DATA_FILE = paths.INPUT_DATA_FILE
OUTPUT_FILE_STR = paths.OUTPUT_FILE_STR
OUTPUT_FILE_PATH = paths.OUTPUT_PATH

RG_PATTERN = re.compile(r'"(.*?)"')


class Serializer:
    GET_DATA = ["address", "phone1"]
    SERIALIZER_TYPE = ""
    INTERPRETED_INPUT_DATA = {}

    def __init__(self):
        if not self.SERIALIZER_TYPE:
            raise ValueError("[Parameter SERIALIZER_TYPE is empty.]")
        self.INTERPRETED_INPUT_DATA = self.interpret_input_file()
        self.OUTPUT_PATH = paths.join([OUTPUT_FILE_PATH, OUTPUT_FILE_STR + '.' + self.SERIALIZER_TYPE])
        self.OUTPUT_HTML_PATH = paths.join([OUTPUT_FILE_PATH, OUTPUT_FILE_STR + '_' + self.SERIALIZER_TYPE + '.html'])
        self.READ_DATA = None

    def interpret_input_file(self):
        """
        reads the input file and interprets it for serializing. Use only: Name, Address, Phone Number.
        :return: <bool> True for success. <bool> False for failure.
        """
        chk_file = paths.check_file(INPUT_DATA_FILE)

        if not chk_file:
            raise IOError("[Input Data File Error] :: Doesn't exist.")

        # initialize the dictionary variable
        dict_data = {}

        # collect data into a dictionary variable
        with open(INPUT_DATA_FILE, 'rU') as f_csv:
            csv_data = csv.reader(f_csv, delimiter=' ', quotechar='|')
            for idx, row in enumerate(csv_data):
                if idx == 0:
                    row_str = ', '.join(row)
                    row_list = RG_PATTERN.findall(row_str)
                    keys = row_list[2:]
                elif idx > 0:
                    nrow_str = ', '.join(row)
                    nrow_list = RG_PATTERN.findall(nrow_str)
                    name = ' '.join(nrow_list[:2])
                    data = nrow_list[2:]
                    dict_data[name] = {}
                    for k, v in zip(keys, data):
                        if k in self.GET_DATA:
                            dict_data[name][k] = v
        return dict_data

    def read(self, f_name=""):
        """
        read the file.
        :param f_name: <str> file input name.
        :return: <bool> True for success. <bool> False for failure.
        """
        # overwrite the file name input
        if f_name:
            self.OUTPUT_PATH = f_name

        if not paths.check_file(self.OUTPUT_PATH):
            return False
        return False

    def display(self, f_input=""):
        """
        display the file contents onto the command line.
        :param f_input: <str> file input name.
        :return: <bool> True for success. <bool> False for failure.
        """
        print("displaying from template")
        # overwrite the file name input
        if f_input:
            self.OUTPUT_PATH = f_input

        # read the file contents
        data = self.read(self.OUTPUT_PATH)
        if not data:
            return False
        pprint.pprint(data)
        return True

    def write_html(self):
        """
        Writes the serialized file on the html document for display.
        :return: <bool> True for success. <bool> False for failure.
        """
        data = self.read()
        message = """<html>
        <head></head>
        <body><p>{data}</p></body>
        </html>""".format(data=data)

        with open(self.OUTPUT_HTML_PATH, 'wb') as html_write:
            html_write.write(message)
            html_write.close()

    def write(self, f_output="", f_data=""):
        """
        writes the file.
        :param f_output: <str> file output name.
        :param f_data: <str> data to write.
        :return: <bool> True for success. <bool> False for failure.
        """
        if f_output:
            self.OUTPUT_PATH = f_output
        if not paths.check_dir(self.OUTPUT_PATH):
            return False
