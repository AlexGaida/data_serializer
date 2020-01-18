"""
This is a template reader/ writer class.
"""
# import standard modules
import pprint as pprint
import csv
import re
import ast

# import custom modules
import paths

# define global variables
INPUT_DATA_FILE = paths.INPUT_DATA_FILE
OUTPUT_FILE_STR = paths.OUTPUT_FILE_STR
OUTPUT_FILE_PATH = paths.OUTPUT_PATH
RG_PATTERN = re.compile(r'"(.*?)"')


class Serializer:
    GET_DATA = ["address", "phone1"]
    DATA_TYPE = 'dictionary'
    INTERPRETED_INPUT_DATA = None
    READ_DATA = None

    def __init__(self, serial_type=""):
        if not self.SERIALIZER_TYPE:
            raise ValueError("[Parameter SERIALIZER_TYPE is empty.]")
        if serial_type:
            self.SERIALIZER_TYPE = serial_type
        self.OUTPUT_PATH = paths.join([OUTPUT_FILE_PATH, OUTPUT_FILE_STR + '.' + self.SERIALIZER_TYPE])
        self.OUTPUT_HTML_PATH = paths.join([OUTPUT_FILE_PATH, OUTPUT_FILE_STR + '_' + self.SERIALIZER_TYPE + '.html'])

    def get_data(self):
        """
        get the data.
        :return: <str> serialized data. <bool> False for failure.
        """
        if self.DATA_TYPE == "list":
            self.INTERPRETED_INPUT_DATA = self.interpret_input_file(ls=True)
            return True
        if self.DATA_TYPE == "dictionary":
            self.INTERPRETED_INPUT_DATA = self.interpret_input_file(dictionary=True)
            return True
        return False

    def serialize_data_repr(self, data=None):
        """
        serialize the data by converting into string repr.
        :return: <str> serialized data. <bool> False for failure.
        """
        if data:
            self.READ_DATA = data
        if self.READ_DATA:
            new_data = repr(self.READ_DATA)
            if "]," in new_data:
                new_data = new_data.replace("],", "],\n")
            if ")," in new_data:
                new_data = new_data.replace("),", "),\n")
            if "}," in new_data:
                new_data = new_data.replace("},", "},\n")
            self.READ_DATA = new_data
            return True
        return False

    def serialize_data_ppformat(self, data=None):
        """
        serialize the data by converting into string pformat.
        :return: <str> serialized data. <bool> False for failure.
        """
        if data:
            self.READ_DATA = data
        if self.READ_DATA:
            return pprint.pformat(self.READ_DATA, indent=4, depth=1)
        return False

    def deserialize_data(self, str_data=""):
        """
        de-serialize the data from a string into data.
        :param str_data: <str> string formatted data.
        :return: <data> returns the data object. <bool> False for failure.
        """
        if not str_data:
            return False
        return ast.literal_eval(str_data)

    def interpret_input_file(self, dictionary=False, ls=False):
        """
        reads the input file and converts it in dictionary data format. Use only: Name, Address, Phone Number.
        :param dictionary: <bool> return in dictionary data format.
        :param ls: <bool> return in dictionary data format.
        :return: <bool> True for success. <bool> False for failure.
        """
        chk_file = paths.check_file(INPUT_DATA_FILE)

        if not chk_file:
            raise IOError("[Input Data File Error] :: Doesn't exist.")

        # initialize the dictionary variable
        dict_data = {}
        ls_data = []

        # collect data into a dictionary memory variable
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
                    if dictionary:
                        dict_data[name] = {}
                        for k, v in zip(keys, data):
                            if k in self.GET_DATA:
                                dict_data[name][k] = v
                    if ls:
                        person = [name]
                        for k, v in zip(keys, data):
                            if k in self.GET_DATA:
                                person.append(v)
                        ls_data.append(tuple(person))
        if dict_data:
            print("[Data] :: Dictionary.", len(dict_data))
            return dict_data
        if ls_data:
            print("[Data] :: List.", len(ls_data))
            return ls_data

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
        return True

    def display(self, f_input="", dsp_type=1):
        """
        display the file contents onto the command line.
        :param f_input: <str> file input name.
        :param dsp_type: <int>, 1, 2 display type: print the string or write to html for viewing.
        :return: <bool> True for success. <bool> False for failure.
        """
        # overwrite the file name input
        if f_input:
            self.OUTPUT_PATH = f_input

        # read the file contents
        success = self.read(self.OUTPUT_PATH)
        if not success:
            return False

        self.serialize_data_repr()

        # print to the command line
        if dsp_type == 1:
            print(self.READ_DATA)

        if dsp_type == 2:
            self.write_html()
        return True

    def write_html(self):
        """
        Writes the html document for nice viewing.
        :return: <bool> True for success. <bool> False for failure.
        """
        lines = self.deserialize_data(self.READ_DATA)
        message = "<html>\n"
        message += "<head>{} Data</head>".format(self.SERIALIZER_TYPE)
        message += "<body>"

        if isinstance(lines, (str, unicode)):
            message += "<p>{}</p>".format(lines)

        if isinstance(lines, (list, tuple)):
            for info in lines:
                # message += "<p>Name: {}, Phone: {}, Address: {}</p>".format(*info)
                message += "<p>{}</p>".format(info)

        if isinstance(lines, dict):
            for name, info in lines.items():
                message += "<p>{}: ".format(name)
                values = ""
                for k, v in info.items():
                    values += "{}: {}, ".format(k, v)
                message += "{}</p>".format(values)
        message += "</html>"

        with open(self.OUTPUT_HTML_PATH, 'wb') as html_write:
            html_write.write(message)
            html_write.close()
        return True

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
        self.get_data()
        return True
