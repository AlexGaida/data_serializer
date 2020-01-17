"""
This is a json reader/ writer module.
"""
# import standard modules
import cPickle as pickle

# import custom modules
from serializers.serialize_template import Serializer

# define class variables
Serializer.SERIALIZER_TYPE = "pickle"


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
        Serializer.read(self, f_name=f_name)

        with open(self.OUTPUT_PATH, 'rb') as pickle_data:
            try:
                rdata = pickle.loads(pickle_data)
                pickle_data.close()
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

        with open(self.OUTPUT_PATH, 'wb') as pickle_data:
            try:
                pickle.dump(self.INTERPRETED_INPUT_DATA, pickle_data)
                pickle_data.close()
                return True
            except ValueError:
                return False