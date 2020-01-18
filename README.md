# data_serializer
Serialize a set of names and addresses. Write it in any format.

This is a command line python tool that serialises/deserialises from a text file of personal data (given in the same location of folder).
The data must output (name, address, phone number).
In at least 2 formats (JSON, YAML, pickle), and display it in at least 2 different ways, preferrably in a HTML file output.
The developer must have these support options in the tool:

to add support for additional storage formats.
to query a list of currently supported formats.
to supply an alternative reader/writer for one of the supported formats.


-----------------------------------------------
############# Tool Description ################
-----------------------------------------------
For clarity purposes, I've separated the serializers into two different folders:
All supported serializers are located in the folder: ..data_serializer\python\serializers
All alternative serializers are located in the folder: ..data_serializer\python\alternative_serializers

All the serializers are sourcing from the base class module ..data_serializer\python\serializers\serialize_template.py
So separate modules could be built by sourcing from that template. 
Only thing in consideration are the class variables: 
self.DATA_TYPE = "dictionary"			# change this to output "dictionary" and "list" data type.
Serializer.SERIALIZER_TYPE = "pickle"	# 

-----------------------------------------------
############### Tool Commands #################
-----------------------------------------------
usage: main.py [-h] [--type {json,pickle,yaml}] [--display {1,2,3}]
               [--query {0,1}]
               [--alt {alt_01_yaml,alt_pickle,alt_yaml,alt_yaml_01}]
               [--tests {0,1}]

Let's serialize this personal_data.csv file.

optional arguments:
  -h, --help            show this help message and exit
  --type {json,pickle,yaml}
                        This is the serializer data type parameter.
  --display {1,2,3}     When true, display the output serialized file. 1: print on command-line. 2: open webbrower.
  --query {0,1}         When true, display all supported serializers.
  --alt {alt_01_yaml,alt_pickle,alt_yaml,alt_yaml_01}
                        When this is supplied, alternative serializers are
                        used instead.
  --tests {0,1}         Run unittest on all available serializers. This
                        procedure will be timed.
						