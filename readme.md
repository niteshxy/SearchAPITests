# Wikimedia API Automation tests

This repo contains automated api tests for Wikimedia api. The tests are written in BDD style gherkin format. The test steps are written in Python and are run with Behave Python library.

## Steps to run
These tests can either be run with Python or can be run in docker as explained below. Checkout this repo on your local machine.

### Steps to run with Python
To run these tests, Python 3.11 should be installed on the machine.

To check the python version run the following command - 

```bash
Python3 --version
```
To run the test run the following commands in root directory of this repo - 
```bash
pip install -r requirements.txt
```
After required packages are installed using above command, run the below command-
```bash
behave
```

You should see a result similar to this - 
```bash
2 features passed, 0 failed, 0 skipped
2 scenarios passed, 0 failed, 0 skipped
6 steps passed, 0 failed, 0 skipped, 0 undefined
Took 0m2.820s
```
### Steps to run with Docker

To run the tests with docker make Docker deamon should be installed on the machine.
Open a terminal, navigate to the root directory and run the below command - 
```bash
docker-compose up
```

## Framework

The tests are written in BDD style format and are present in the .feature file in /Features directory. The step definitions of these features are present in python files in /Steps directory.

There is a TestBase file in /Utilities directory which contains all the global data related to API.
There is a Helpers directory which contains helper functions to be used in step definitions.

