"""
This is a json reader/ writer module.
"""
# import standard modules
import yaml

# import custom modules
from serializers.serialize_template import Serializer

# define class variables
Serializer.SERIALIZER_TYPE = "yaml"
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

        with open(self.OUTPUT_PATH, 'rb') as yaml_data:
            rdata = yaml.load(yaml_data)
            self.READ_DATA = rdata
            yaml_data.close()
            return True

    def write(self, f_output="", f_data=""):
        """
        writes the json file.
        :param f_output: <str> custom file output name.
        :param f_data: <str> data to write.
        :return: <bool> True for success. <bool> False for failure.
        """
        Serializer.write(self, f_output=f_output, f_data=f_data)

        with open(self.OUTPUT_PATH, 'wb') as yaml_data:
            try:
                yaml.dump(self.INTERPRETED_INPUT_DATA, yaml_data)
                yaml_data.close()
                return True
            except ValueError:
                return False
