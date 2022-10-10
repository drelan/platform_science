"""
Feature file is like a test suite which can have various test cases (which we call Scenarios).
And the Gherkin format test steps present in feature file --> have step definition in this step implementation python file.
"""
import requests
from behave import *
from payload import *


# context variable is global so as to make all variables of this method available to other methods
@given('the room dimensions, dirt patches co-ordinates, initial hoover position and driving instructions')
def step_impl(context):
    context.url = 'http://localhost:8080/v1/cleaning-sessions'
    context.headers = {'Content-Type': 'application/json'}
    context.payload = hoover_payload()


@when('we execute navigate the imaginary robotic hoover service')
def step_impl(context):
    context.response = requests.post(context.url, json=context.payload, headers=context.headers)
    print(context.response.json())


@then('we get the final robotic hoover position and number of patches cleaned')
def step_impl(context):
    context.expected_response = {'coords': [1, 3],
                                 'patches': 2
                                 }
    assert context.response.headers['Content-Type'] == 'application/json;charset=UTF-8'
    assert context.response.json() == context.expected_response


@then('status code of response should be {statuscode:d}')
def step_impl(context, statuscode):
    assert context.response.status_code == statuscode


@given('the room dimensions, dirt patches co-ordinates, initial hoover position with incorrect endpoint')
def step_impl(context):
    context.url = 'http://localhost:8080/v1/cleanng-sessions'
    context.headers = {'Content-Type': 'application/json'}
    context.payload = hoover_payload()
