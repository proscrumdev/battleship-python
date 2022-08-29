[![Build status](https://dev.azure.com/APS-SD-Stewards/APS-SD/_apis/build/status/proscrumdev.battleship-python-CI)](https://dev.azure.com/APS-SD-Stewards/APS-SD/_build/latest?definitionId=16)

# Torpydo - Battleship Python
A simple game of Battleship, written in Python. The purpose of this repository is to serve as an entry point into coding exercises and it was especially created for scrum.orgs Applying Professional Scrum for Software Development course (www.scrum.org/apssd). The code in this repository is unfinished by design.

# Getting started

This project requires Python 3.6 or newer. To prepare to work with it, pick one of these
options:

## Linux and macOS

Create and activate a [virtual environment][venv]. This assumes python3 is
already installed.

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
export PYTHONPATH=.
```

If you stop working on this project, close your shell, and return later, make
sure you run the `source bin/venv/activate` command again.

[venv]:https://docs.python.org/3/library/venv.html

## Windows

[Download][pywin] and install Python 3.6 for Windows. Make sure python is on
your `PATH`. Open a command prompt:

```commandline
python -m venv venv
venv\Scripts\activate.bat
pip install -r requirements.txt
set PYTHONPATH=.
```

[pywin]:https://www.python.org/downloads/windows/

## Docker

If you don't want to install anything Python-related on your system, you can
run the game inside Docker instead.

### Build the Docker Image

```bash
docker build -t torpydo .
```

### Run a Docker Container from the Image

```bash
docker run -it --env PYTHONPATH=/torpydo -v ${PWD}:/torpydo torpydo bash
```

# Launching the game

```bash
python -m torpydo

# alternatively:
python torpydo/battleship.py
```

# Running the Tests

```
nose2 -v
behave
```

to run with coverage:
```
nose2 -v --with-coverage --coverage ./torpydo
```

to run and store the test results for further examination (e.g. build pipeline)
```
nose2 --v --junit-xml --junit-xml-path xunit.xml
behave --junit
```

Run behave tests with coverage:
```
https://stackoverflow.com/a/37447392/736079
```

# Telemetry data
This application is collecting telemetry data with Microsoft Application Insights.
For more details see https://docs.microsoft.com/en-us/azure/azure-monitor/app/opencensus-python.

To send the telemetry data to a specific instance of Application Insights, the connection string has to be adjusted in telemetryclient.py

