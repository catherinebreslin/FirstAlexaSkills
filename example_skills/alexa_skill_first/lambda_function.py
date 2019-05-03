"""
This sample demonstrates a simple skill built with the Amazon Alexa Skills Kit.
The Intent Schema, Custom Slots, and Sample Utterances for this skill, as well
as testing instructions are located at http://amzn.to/1LzFrj6

For additional samples, visit the Alexa Skills Kit Getting Started guide at
http://amzn.to/1LGWsLG
"""


import random

# --------------- Custom response logic ---------------------


maths_quotes = [
    "Arithmetic is being able to count up to twenty without taking off your shoes. Mickey Mouse",
    "I don’t think that everyone should become a mathematician, but I do believe that many students don’t give mathematics a real chance. Maryam Mirxakhani",
    "Do not worry too much about your difficulty in mathematics, I can assure you that mine are still greater. Albert Einstein"
    ]

education_quotes = [
    "One child, one teacher, one book and one pen can change the world. Malala Yousafzai.",
    "A good education can lift you up into a life you never could have imagined. Michelle Obama.",
    "Knowledge is power. Information is liberating. Education is the premise of progress, in every society, in every family. Kofi Annan"
]

success_quotes = [
    "Luck has nothing to do with it because I have spent many, many hours, countless hours, on the court working for my one moment in time, not knowing when it would come. Serera Williams",
    "Success is not final, failure is not fatal. It is the courage to continue that counts. Winston Churchill.",
    "I know of no single formula for success. But over the years I have observed that some attributes of leadership are universal and are often about finding ways of encouraging people to combine their efforts, their talents, their insights, their enthusiasm and their inspiration to work together. Queen Elizabeth the second"
]

science_quotes = [
    "I am among those who think that science has great beauty. Marie Curie.",
    "Kids should be allowed to break stuff more often. That's a consequence of exploration. Exploration is what you do when you don't know what you're doing. That's what scientists do every day. Neil deGrasse Tyson.",
    "Look up at the stars and not down at your feet. Try to make sense of what you see, and wonder about what makes the universe exist. Be curious. Stephen Hawking"
]

travel_quotes = [
    "We're fighting for human advancement, to move the world ahead, for the advancement of human history. Exploration always involves risk. Mae Jemison." 
    "I think you travel to search, and you come back home to find yourself there. Chimamanda Ngozi Adichie",
    "Flying may not be all plain sailing, but the fun of it is worth the price. Amelia Earhart" 
]

def get_something():
    """
    Return a simple answer Alexa will give the user
    :return: string containing the answer
    """
    speech_output = "I say whatever I please"
    return speech_output


def get_quote(subject):
    quote_dict = {
        "maths": maths_quotes,
        "education": education_quotes,
        "success": success_quotes,
        "science": science_quotes,
        "travel": travel_quotes,
    }
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

    if person_name.lower() == 'chimamanda ngozi adichie' or person_name.lower() == 'chimamanda':
        speech_output = "Chimamanda Ngozi Adichie is a feminist author. "
    elif person_name.lower() == 'winston churchill':
        speech_output = "winston churchill was british prime minister from 1940 to 1945 and again from 1951 to 1955."
    elif person_name.lower() == 'amelia earhart':
        speech_output = "amelia earhart was an American aviation pioneer. She was the first female aviator to fly solo across the Atlantic Ocean."
    elif person_name.lower() == 'albert einstein was a physicist who developed the theory of relativity':
        speech_output = "albert einstein"
    elif person_name.lower() == 'kofi annan':
        speech_output = "kofi annan was a Ghanaian diplomat who served as the seventh Secretary-General of the United Nations. Together with the U. N. he received the nobel peace prize in 2001"
    elif person_name.lower() == 'serena williams':
        speech_output = "serena williams is the world's number 1 female tennis player"
    elif person_name.lower() == 'marie curie':
        speech_output = "marie curie was a Polish and naturalized-French physicist and chemist who conducted pioneering research on radioactivity. She was the first woman to win a Nobel Prize, the first person and only woman to win twice, and the only person to win a Nobel Prize in two different sciences"
    elif person_name.lower() == 'mae jemison':
        speech_output = "mae jemison is an American engineer, physician and NASA astronaut. She became the first black woman to travel in space when she served as an astronaut aboard the Space Shuttle Endeavour"   
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
    elif intent['name'] == 'personalFactIntent':
        person_name = intent['slots']['Person']['value']
        speech_output = get_person_fact(person_name)
    elif intent['name'] == 'giveMeQuoteIntent':
        subject = intent['slots']['Subject']['value']
        speech_output = get_quote(subject)
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
