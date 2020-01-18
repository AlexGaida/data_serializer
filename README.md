# data_serializer
Serialize a set of names and addresses. Write it in any format.

This is a command line python tool that serialises/deserialises from a text file of personal data (given in the same location of folder).
The data must output (name, address, phone number).
In at least 2 formats (JSON, YAML, pickle), and display it in at least 2 different ways, preferrably in a HTML file output.
The developer must have these support options in the tool:

to add support for additional storage formats.
to query a list of currently supported formats.
to supply an alternative reader/writer for one of the supported formats.

Tool Description:

usage: main.py [-h] [--type {json,pickle,yaml}] [--display {1,2,3}]
               [--query {0,1}]
               [--alt {alt_01_yaml,alt_pickle,alt_yaml,alt_yaml_01}]
               [--tests {0,1}]

Let's serialize this data file.

optional arguments:
  -h, --help            show this help message and exit
  --type {json,pickle,yaml}
                        This is the serializer data type parameter.
  --display {1,2,3}     When true, display the output serialized file.
  --query {0,1}         When true, display all supported serializers.
  --alt {alt_01_yaml,alt_pickle,alt_yaml,alt_yaml_01}
                        When this is supplied, alternative serializers are
                        used instead.
  --tests {0,1}         Run unittest on all available serializers. This
                        procedure will be timed.