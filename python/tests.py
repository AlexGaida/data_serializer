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

serials_dict = {}
for serial_type in SERIALIZERS:
    serializer_name = "serialize_" + serial_type
    fp, pathname, description = imp.find_module(serializer_name, [paths.SERIALIZER_PATH])
    serializer_module = imp.load_module(serializer_name, fp, pathname, description)

    # instantiate the chosen serializer file class
    serials_dict[serial_type] = serializer_module.SerializeFile()


for serial_type in ALT_SERIALIZERS:
    serializer_name = "serialize_alt_" + serial_type
    fp, pathname, description = imp.find_module(serializer_name, [paths.ALTERNATIVE_SERIALIZER_PATH])
    serializer_module = imp.load_module(serializer_name, fp, pathname, description)

    # instantiate the chosen serializer file class
    serials_dict['alt_' + serial_type] = serializer_module.SerializeFile()


class TestSerializers(unittest.TestCase):
    def test_json_write(self):
        self.assertEqual(serials_dict['json'].write(), True)

    def test_yaml_write(self):
        self.assertEqual(serials_dict['yaml'].write(), True)

    def test_pickle_write(self):
        self.assertEqual(serials_dict['pickle'].write(), True)

    def test_json_read(self):
        self.assertEqual(serials_dict['json'].read(), True)

    def test_yaml_read(self):
        self.assertEqual(serials_dict['yaml'].read(), True)

    def test_pickle_read(self):
        self.assertEqual(serials_dict['pickle'].read(), True)

    def test_alt_pickle_write(self):
        self.assertEqual(serials_dict['alt_pickle'].write(), True)

    def test_alt_pickle_read(self):
        self.assertEqual(serials_dict['alt_pickle'].read(), True)


def perform_tests():
    unittest.main()
