"""
This sample demonstrates a simple skill built with the Amazon Alexa Skills Kit.
The Intent Schema, Custom Slots, and Sample Utterances for this skill, as well
as testing instructions are located at http://amzn.to/1LzFrj6

For additional samples, visit the Alexa Skills Kit Getting Started guide at
http://amzn.to/1LGWsLG
"""


import random

# --------------- Custom response logic ---------------------


def get_something():
    """
    Return a simple answer Alexa will give the user
    :return: string containing the answer
    """
    speech_output = "I say whatever I please"
    return speech_output


def get_quote(subject):
    quote_dict = {"education": ["Quote one", "Quote two", "Quote 3"]}
    if subject in quote_dict:
        valid_answers = quote_dict[subject]
        speech_output = random.choice(valid_answers)
    else:
        speech_output = "I don't know much about " + str(subject) + " yet"
    return speech_output


def get_person_fact(person_name):
    """
    Finds a fact about a name
    """
    if person_name.lower() == 'catherine':
        speech_output = 'catherine works on voice technology'
    if person_name.lower() == 'charlotte':
        speech_output = 'something about charlotte'
    if person_name.lower() == 'conor':
        speech_output = 'something about conor'
    elif person_name.lower() == 'feminist internet':
        speech_output = 'something about feminist internet'
    else:
        speech_output = 'i don\'t know much about ' + person_name
    return speech_output


def intent_handler(intent, session):
    """
    Collects values to generate an Alexa response
    by calling custom logic based on the intent name
    """
    session_attributes = {}
    should_end_session = True
    reprompt_text = "i didn't get that please repeat"

    if intent['name'] == 'saySomethingIntent':
        speech_output = get_something()
    elif intent['name'] == 'giveMeQuoteIntent':
        subject = intent['slots']['Subject']['value']
        speech_output = get_quote(subject)
    elif intent['name'] == 'personalFactIntent':
        person_name = intent['slots']['Person']['value']
        speech_output = get_person_fact(person_name)
    else:
        # this shouldn't occur unless we omit the implementation of some intent
        should_end_session = True
        speech_output = "hmm not sure how to deal with your request"
    return build_response(session_attributes, build_speechlet_response(
        intent['name'], speech_output, reprompt_text, should_end_session))

# --------------- Helpers that build all of the responses ---------------------


def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': "SessionSpeechlet - " + title,
            'content': "SessionSpeechlet - " + output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }


def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }


# --------------- Functions that control the skill's behavior -----------------

def get_welcome_response():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    session_attributes = {}
    card_title = "Welcome"
    speech_output = "Welcome to my first Alexa skill"
    # If the user either does not reply to the welcome message or says
    # something that is not understood, they will be prompted again with this
    # text.
    reprompt_text = "Hi there!"
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def handle_session_end_request():
    card_title = "Session Ended"
    speech_output = "Thank you for trying this skill. " \
                    "Have a nice day! "
    # Setting this to true ends the session and exits the skill.
    should_end_session = True
    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))


# --------------- Events ------------------


def on_session_started(session_started_request, session):
    """ Called when the session starts """

    print("on_session_started requestId=" +
          session_started_request['requestId'] +
          ", sessionId=" + session['sessionId'])


def on_launch(launch_request, session):
    """ Called when the user launches the skill without specifying what they
    want
    """

    print("on_launch requestId=" + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # Dispatch to your skill's launch
    return get_welcome_response()


def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """

    print("on_intent requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    # Dispatch to your skill's intent handlers
    if intent_name == "AMAZON.HelpIntent":
        return get_welcome_response()
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    else:
        return intent_handler(intent, session)


def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.

    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # add cleanup logic here


# --------------- Main handler ------------------

def lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """
    print("event.session.application.applicationId=" +
          event['session']['application']['applicationId'])

    """
    Uncomment this if statement and populate with your skill's application ID
    to prevent someone else from configuring a skill that sends requests to
    this function.
    """
    # if (event['session']['application']['applicationId'] !=
    #         "amzn1.echo-sdk-ams.app.[unique-value-here]"):
    #     raise ValueError("Invalid Application ID")

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])
