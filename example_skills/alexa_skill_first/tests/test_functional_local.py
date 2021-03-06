'''This is just an automation of the commandline testing we can do with test_lambda_function
We only test a single fake event. This test is mostly an example on howto use lambda.utils
and existing test cases to automate functionality testing of AWS Lambda skill

lambda_utils.generate_testevents() generates Alexa test events
which we can inject into the lambda skill.
'''

import os
from .. import lambda_function
from FirstAlexaSkills import lambda_utils

cur_dir = os.path.dirname(os.path.realpath(__file__))


def test_event():
    ref = 'I say whatever I please'
    alexa_event_template = lambda_utils.get_eventtemplate_fn()
    alexa_event_data = os.path.join(cur_dir, 'data', 'lambda_test_data.json')
    event_list = lambda_utils.generate_testevents(alexa_event_data, alexa_event_template)
    event = event_list[1]
    context = None
    res = lambda_function.lambda_handler(event, context)
    res_output_speech = res["response"]["outputSpeech"]["text"]
    assert res_output_speech == ref
