"""
Perform unit testing on the serializers.
"""

# import standard modules
import unittest
import imp

# import custom modules
import paths

# define global variables
SERIALIZERS = paths.find_serializers(names=1)
ALT_SERIALIZERS = paths.find_serializers(alternative=1, names=1)
SERIALS_DICT = {}


def init_modules():
    """
    Initialize the modules for usage.
    :return:
    """
    for serial_type in SERIALIZERS:
        serializer_name = "serialize_" + serial_type
        fp, pathname, description = imp.find_module(serializer_name, [paths.SERIALIZER_PATH])
        serializer_module = imp.load_module(serializer_name, fp, pathname, description)

        # instantiate the chosen serializer file class
        SERIALS_DICT[serial_type] = serializer_module.SerializeFile()

    for serial_type in ALT_SERIALIZERS:
        serializer_name = "serialize_" + serial_type
        fp, pathname, description = imp.find_module(serializer_name, [paths.ALTERNATIVE_SERIALIZER_PATH])
        serializer_module = imp.load_module(serializer_name, fp, pathname, description)

        # instantiate the chosen serializer file class
        SERIALS_DICT[serial_type] = serializer_module.SerializeFile()


class TestSerializers(unittest.TestCase):
    def test_json_write(self):
        self.assertEqual(SERIALS_DICT['json'].write(), True)

    def test_yaml_write(self):
        self.assertEqual(SERIALS_DICT['yaml'].write(), True)

    def test_pickle_write(self):
        self.assertEqual(SERIALS_DICT['pickle'].write(), True)

    def test_json_read(self):
        self.assertEqual(SERIALS_DICT['json'].read(), True)

    def test_yaml_read(self):
        self.assertEqual(SERIALS_DICT['yaml'].read(), True)

    def test_pickle_read(self):
        self.assertEqual(SERIALS_DICT['pickle'].read(), True)

    def test_alt_pickle_write(self):
        self.assertEqual(SERIALS_DICT['alt_pickle'].write(), True)

    def test_alt_pickle_read(self):
        self.assertEqual(SERIALS_DICT['alt_01_yaml'].read(), True)


def perform_tests():
    unittest.main()
