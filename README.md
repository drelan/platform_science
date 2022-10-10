# Python Behave: Local Setup
 behave is behaviour-driven development, Python style. behave uses tests written in a natural language style, backed up by Python code.
 behave mainly operated on two main directories: feature files which basically is a test suite having multiple test cases and a 
 steps directory which has python step implementation for the scenarios.

## Pipenv
1. Install Python 3.10.x by going to https://www.python.org/downloads/release/python-3107/ and downloading the Mac compatible download
2. Install [Pipenv](https://docs.pipenv.org/)
3. Run `pipenv install` (this will install python virtual environment)
4. Pipfile has behave, requests and allure-behave packages which will get installed.
  

## REPORTS
1. Ensure you have allure-behave package installed (previous step)
2. Run `brew install allure`

## RUNNING TESTS
1. `behave` command will run all the feature files with no allure report generated.
2. `behave <feature file> —tags=smoke` will run a specific feature file with test cases having specified tag (in this case: smoke)
3. `behave -f allure_behave.formatter:AllureFormatter -o <allure_report_folder>` will generate reports in Json format in specified Allure Report folder.
4. `allure serve <allure_report_folder>` will kick off a browser server instance and convert JSON format to HTML reports with graphs, logs etc.