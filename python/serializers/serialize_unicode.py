"""
This is a unicode reader/ writer module.
"""
# import custom modules
from serializers.serialize_template import Serializer

# define private variables
__version__ = "1.0.0"

# define class variables
Serializer.SERIALIZER_TYPE = "txt"
Serializer.DATA_TYPE = "list"


class SerializeFile(Serializer):
    def __init__(self):
        # get the input data
        Serializer.__init__(self)

    def read(self, f_name=""):
        """
        read the json file.
        :param f_name: <str> file input name.
        :return: <bool> True for success. <bool> False for failure.
        """
        success = Serializer.read(self, f_name=f_name)
        if not success:
            raise IOError("[No File] :: There is no file to read from.")

        with open(self.OUTPUT_PATH, 'r') as uni_file:
            try:
                rdata = uni_file.readlines()
                uni_file.close()
                self.READ_DATA = rdata
                return True
            except ValueError:
                return False

    def write(self, f_output="", f_data=""):
        """
        writes the json file.
        :param f_output: <str> custom file output name.
        :param f_data: <str> data to write.
        :return: <bool> True for success. <bool> False for failure.
        """
        Serializer.write(self, f_output=f_output, f_data=f_data)
        success = self.serialize_data_repr(self.INTERPRETED_INPUT_DATA)
        if not success:
            raise ValueError("[Serialization Error] :: File not serialized")

        with open(self.OUTPUT_PATH, 'w') as uni_file:
            try:
                uni_file.writelines(self.READ_DATA)
                self.print_file_size()
                return True
            except ValueError:
                return False
