# Data Serializer

Serialize a set of names and addresses. Write it in any format.

This is a command line python tool that serialises/ deserialises from a file of personal data (personal_data.csv).
The data must output (name, address, phone number).
In at least 2 formats (JSON, YAML, pickle), and display it in at least 2 different ways, preferrably in a HTML file output.
The developer must have these support options in the tool:

*to add support for additional storage formats.
*to query a list of currently supported formats.
*to supply an alternative reader/writer for one of the supported formats.


### Prerequisites

Open a windows or linux command prompt, and drag this file through:

```
...\data_serializer\python\main.py
```

## Running the program

There are two ways to operate this tool, the first option is by using the 6 arguments, one at a time:
```
  -h, --help            show this help message and exit
  --run	{0, 1}	   Run the program inside a loop.
  --type {json,pickle,yaml}
                        This is the serializer data type parameter.
  --display {1,2,3}     When true, display the output serialized file. 1: print on command-line. 2: open webbrower.
  --query {0,1}         When true, display all supported serializers.
  --alt {alt_01_yaml,alt_pickle,alt_yaml,alt_yaml_01}
                        When this is supplied, alternative serializers are
                        used instead.
  --tests {0,1}         Run unittest on all available serializers. This
                        procedure will be timed.
```

And the tool can be run inside a loop, accepting these arguments:
type, display, query, alt, tests, quit, exit
```
..data_serializer\python\main.py --run 1
```

### display data
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
