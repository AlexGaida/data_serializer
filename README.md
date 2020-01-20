# Data Serializer

Serialize a set of names and addresses. Write it in any format.

This is a command line python tool that serialises/ deserialises from a file of personal data (personal_data.csv).
The data must output (name, address, phone number).
In at least 2 formats (JSON, YAML, pickle), and display it in at least 2 different ways, preferrably in a HTML file output.
The developer must have these support options in the tool:

*to add support for additional storage formats.
*to query a list of currently supported formats.
*to supply an alternative reader/writer for one of the supported formats.

## Definition of a Serializer
To serialize is to convert from a data object (tuple, list, dict) to a string object (str, unicode) and then storing this information into a file.


### Plan

![Plan](/plan.pdf)

### Prerequisites
* numpy

Open a windows or linux command prompt, and drag this file through and run the commands:

```
...\data_serializer\python\main.py
```

## Running the program

There are two ways to operate this tool, the first option is by using the 6 arguments, one at a time:
```
  -h, --help            show this help message and exit
  --all	{0, 1}	     Run all available supported and alternate serializers.
  --run	{0, 1}	     Run the program inside a loop.
  --type {json, pickle, yaml, numpy, unicode}
                        This is the serializer data type parameter.
  --display {1,2,3}     When true, display the output serialized file. 1: print on command-line. 2: open webbrower. 3: open notepad.
  --query {0,1}         When true, display all supported serializers.
  --alt {alt_01_yaml, alt_pickle, alt_yaml, alt_yaml_01}
                        When this is supplied, alternative serializers are
                        used instead.
  --tests {0,1}         Run unittest on all available serializers. This
                        procedure will be timed.
```

And the tool can be run inside a loop, accepting these arguments:
all, type, display, query, alt, tests, quit, exit
```
..data_serializer\python\main.py --run 1
```

### serializing data
To deseralize the personal_data.csv file and to serealize it, only one argument is needed at a time: type and alt.

To serialize using pickle.
```
main.py --type pickle
```

To serialize using alternative pickle.
```
main.py --type alt_pickle
```

### displaying data
To display the serialized data, two arguments must be supplied: type (str) and display (int). The tools has three options of displaying data:
1. printing the data on the command line.
2. opening a web browser to show data.
3. opening a notepad.

This tool writes serialized data in separate files located in the output folder.

To display a json serialized file:
```
main.py --display 2 --type json
```

To display an alternative json serialized file:
```
main.py --display 2 --alt alt_json
```

### managing serializers
To manage and create additional serializers, inside the python folder, there are two additional folders:

The supported serializer folder:

* ..\data_serializer\python\serializers

The alternative serializer folder:

* ..\data_serializer\python\alternative_serializers


### serializer template
To create a new serializer module, all other serializer modules are sourcing from this base class serializer python file:
```
..\data_serializer\python\serializers\serialize_template.py
```

Two important variables needs to be taken into consideration:
* SERIALIZER_TYPE : this is the variable that determines the extension name of the serializer. Names can include numbers. eg "json", "json_01", "02_doodly"
* DATA_TYPE : this is the data type used to de-serialize the personal_data.csv file. Options are: list and dictionary.

### unittests

The testing module is located here:

```
..\data_serializer\python\tests.py
```
run the testing sets by entering:
```
main.py --test 1
```


## Authors

* **Alexei Gaidachev** - *Initial work*


## License

This project is free to view and use for anyone.
