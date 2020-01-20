"""
This is a numpy reader/ writer module.
"""
# import standard modules
import numpy
# help(numpy)

# import custom modules
from serializers.serialize_template import Serializer

# define private variables
__version__ = "1.0.0"

# define class variables
Serializer.SERIALIZER_TYPE = "npy"


class SerializeFile(Serializer):
    def __init__(self):
        # get the input data
        Serializer.__init__(self)
        self.DATA_TYPE = "dictionary"

    def read(self, f_name=""):
        """
        read the numpy file.
        :param f_name: <str> file input name.
        :return: <bool> True for success. <bool> False for failure.
        """
        success = Serializer.read(self, f_name=f_name)

        if not success:
            raise IOError("[No File] :: There is no file to read from.")
        try:
            rdata = numpy.load(self.OUTPUT_PATH, encoding='bytes', allow_pickle=True)
            self.READ_DATA = rdata.tolist()
            return True
        except ValueError:
            return False

    def write(self, f_output="", f_data=""):
        """
        writes the numpy file.
        :param f_output: <str> custom file output name.
        :param f_data: <str> data to write.
        :return: <bool> True for success. <bool> False for failure.
        """
        Serializer.write(self, f_output=f_output, f_data=f_data)

        try:
            numpy.save(self.OUTPUT_PATH, self.INTERPRETED_INPUT_DATA)
            self.print_file_size()
            return True
        except ValueError:
            return False
