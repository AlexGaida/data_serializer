"""
Perform unit testing on the serializers.
"""

# import standard modules
import unittest
import imp

# import custom modules
import paths

# define private variables
__version__ = "1.0.0"

# define global variables
SERIALIZERS = paths.find_serializers(names=1)
ALT_SERIALIZERS = paths.find_serializers(names=1, alternative=1)
SERIALS_DICT = {}


def init_modules():
    """
    Initialize the modules for usage.
    :return:
    """
    for serial_type in SERIALIZERS:
        serializer_name = "serialize_" + serial_type

        try:
            fp, pathname, description = imp.find_module(serializer_name, [paths.SERIALIZER_PATH])
            serializer_module = imp.load_module(serializer_name, fp, pathname, description)
        except ImportError:
            print("[Module Not Loaded] :: {}".format(serializer_name))
            continue

        # instantiate the chosen serializer file class
        SERIALS_DICT[serial_type] = serializer_module.SerializeFile()

    for serial_type in ALT_SERIALIZERS:
        serializer_name = "serialize_" + serial_type

        try:
            fp, pathname, description = imp.find_module(serializer_name, [paths.ALTERNATIVE_SERIALIZER_PATH])
            serializer_module = imp.load_module(serializer_name, fp, pathname, description)
        except ImportError:
            print("[Module Not Loaded] :: {}".format(serializer_name))
            continue

        # instantiate the chosen serializer file class
        SERIALS_DICT[serial_type] = serializer_module.SerializeFile()


class TestUtils(unittest.TestCase):
    def test_input_file(self):
        self.assertEqual(paths.check_input_data_file(), True)

    def test_serializer_list(self):
        serials = paths.find_serializers(names=1)
        self.assertNotEqual(serials, False)

    def test_alt_serializer_list(self):
        serials = paths.find_serializers(names=1, alternative=1)
        self.assertNotEqual(serials, False)


class TestSerializers(unittest.TestCase):
    def test_unicode_write(self):
        self.assertEqual(SERIALS_DICT['unicode'].write(), True)

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
        self.assertEqual(SERIALS_DICT['alt_pickle'].read(), True)

    def test_alt_yaml_01_read(self):
        self.assertEqual(SERIALS_DICT['alt_01_yaml'].read(), True)

    def test_alt_01_yaml_read(self):
        self.assertEqual(SERIALS_DICT['alt_01_yaml'].read(), True)

    def test_alt_yaml_read(self):
        self.assertEqual(SERIALS_DICT['alt_yaml'].read(), True)


class TestHTMLWrite(unittest.TestCase):
    def test_unicode_HTML(self):
        self.assertEqual(SERIALS_DICT['json'].display(dsp_type=2), True)

    def test_json_HTML(self):
        self.assertEqual(SERIALS_DICT['json'].display(dsp_type=2), True)

    def test_yaml_HTML(self):
        self.assertEqual(SERIALS_DICT['yaml'].display(dsp_type=2), True)

    def test_pickle_HTML(self):
        self.assertEqual(SERIALS_DICT['pickle'].display(dsp_type=2), True)


def perform_tests():
    unittest.main()
