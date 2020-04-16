# COVID19-VA
Ingestion, visualization, and querying tool based on Covid-19 Virginia cases.

## Development & Setup

Create some sort of virtual environment before you install `covid` the CLI tool.
Covid is the standardized tool that can be used to utilize Virginia Coronvirus data
by ingesting, visualizing, and querying it.

#### Activate Virtual Environment
```sh
# Activate your virtual enviroment!
# In the root of the project / repository
$ cd covid19-va/
$ python3 -m venv env
$ source env/bin/activate
```

#### Install Covid CLI Tool
```sh
# Install the dataio cli tool
# In the root of the project / repository
$ cd covid19-va/
$ pip install --editable .
```

The `--editable` flag will allow for you to make edits to code without having to
re-run `pip install ...` locally.

#### Validate The Install
Run `covid --verison` to verify the installation was successful.
```sh
$ covid --version
covid version: v0.1.0
```

#### Showing The Tool Capabilities
Run `covid` to learn what the tool does and the commands you can run with it.
```sh
$ covid

Usage: covid [OPTIONS] COMMAND [ARGS]...

  Covid is a tool to run data ingestion, visualize the data, and run basic queries
  on the data.

Options:
  --home DIRECTORY  Project folder to operate on.
  -v, --verbose     Enables verbose mode.
  --version         Print the current version of bessy.
  --help            Show this message and exit.

Commands:
  fetch      Fetch the Virginia Covid-19 case data.
  ingest     Ingest the Virginia Covid-19 case data.
  list       List the Virginia Covid-19 case data.
  visualize  Visualize the Virginia Covid-19 case data.
```

#### Fetching Virginia Covid-19 Dataset
The data that is being used for this tool comes from the [Virginia Department of Health](http://www.vdh.virginia.gov/coronavirus/). The best thing about using this dataset is that they update it daily. In order to get the data locally, `covid` has a command that allows you to fetch the dataset so you can get the most updated one.
```sh
$ covid fetch
```