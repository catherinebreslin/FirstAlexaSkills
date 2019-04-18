FirstAlexaSkills - A Python package for learning first steps with Alexa skills
==============================================================================

.. image:: http://img.shields.io/pypi/v/FirstAlexaSkills.svg
    :target: https://pypi.python.org/pypi/FirstAlexaSkills

.. image:: https://travis-ci.org/means-to-meaning/FirstAlexaSkills.svg?branch=master
    :target: https://travis-ci.org/means-to-meaning/FirstAlexaSkills

.. image:: https://readthedocs.org/projects/firstalexaskills/badge/?version=latest
        :target: http://firstalexaskills.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

Welcome to the wonderful world of Alexa interactions! Do you have great ideas for teaching Alexa new skills? There are only two steps to make a third-party skill using the `Alexa Skills Kit`_:

* creating an Alexa skill (ASK) which will convert your speech into intents (think of them as events for now) which you define - by associating utterances (sentences) to intents. For more details, take a look at the `official ASK starter guide`_.
* creating an `AWS Lambda`_ function or a web service that will receive the intents from Alexa. This package uses AWS Lambda functions because they are ideal for simple functions - `low cost`_ and zero infrastructure maintainance. You can find the official documentation `here`_. If you are interested in a web service approach to ASK with Python, then you should definitely try John Wheeler's great `flask-ask package`_.

You can install ``FirstAlexaSkills`` with:

.. code-block:: console

    $ pip install firstalexaskills

You will also need to setup credentials to use AWS Lambda from to console and a developer account to create an Alexa skill. For more details, see the `installation guide`_.

Here is all it takes to create, upload, test, modify, re-upload and re-test your first AWS Lambda skill function with AlexaFirstSkills:

.. code-block:: console

    $ mkdir alexa_development
    $ unpack_example_skills # unpacks Alexa skill examples to ./example_skills
    $ cd example_skills # Explore the Alexa skills in this directory
    $ cd alexa_skill_first # Once ready, create your own AWS Lambda function
    $ create_lambda_function --function-name skill_first --dir .
    Function succesfully created!
    AWS Lambda function ARN: arn:aws:lambda:your_aws_region:your_account_id:function:skill_first
    $ test_lambda_function --function-name skill_first --test-data tests/data/lambda_test_data.json
    ... test output ...
    $ idle lambda_function.py # modify the skill
    $ update_lambda_function --function-name skill_first --dir . # update function in the cloud
    $ test_lambda_function --function-name skill_first --test-data tests/data/lambda_test_data.json
    ... test updated output ...

You can install ``FirstAlexaSkills`` with:

    .. code-block:: console

        $ pip install FirstAlexaSkills

You will also need to setup credentials to use AWS Lambda from to console and a developer account to create an Alexa skill. For more details, see the `installation guide`_.

The package contains example Alexa skills, utilities and `tutorials`_ that will guide you from simply getting the Echo to reply, to setting your home temperature using the IoT device of your choice. Most importantly though, it allows you to develop locally, sync your local Lambda function to the cloud and immediately test it using a fake Alexa event in one button press. Something that might come in handy when building your own skills later.

New to programming, or Python? Checkout the `15 minute mini-intro`_!
If you are thinking of setting up a hackathon to develop some new third-party Alexa skills, this `guide`_ has you covered!

Discussion
~~~~~~~~~~

If you run into any issues you can file them in the `issue tracker`_.

History
~~~~~~~~~~
This package was first developed by Vlastimil Pis at Amazon (Cambridge UK) as part of an outreach program to teach programming skills to teenagers. Its original location is https://github.com/means-to-meaning/FirstAlexaSkills/


.. _`Alexa Skills Kit`: https://developer.amazon.com/alexa-skills-kit
.. _`official ASK starter guide`: https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/getting-started-guide
.. _`AWS Lambda`: https://aws.amazon.com/lambda/details/
.. _`low cost`: https://aws.amazon.com/lambda/pricing/
.. _`here`: https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/developing-an-alexa-skill-as-a-lambda-function
.. _`flask-ask package`: https://github.com/johnwheeler/flask-ask
.. _`installation guide`: https://github.com/means-to-meaning/FirstAlexaSkills/tree/master/docs/installation.rst
.. _`tutorials`: https://github.com/means-to-meaning/FirstAlexaSkills/tree/master/docs/tutorials.rst
.. _`15 minute mini-intro`: https://github.com/means-to-meaning/FirstAlexaSkills/tree/master/docs/python_intro.rst
.. _`guide`: https://github.com/means-to-meaning/FirstAlexaSkills/tree/master/docs/hackathon_setup.rst
.. _`issue tracker`: https://github.com/means-to-meaning/FirstAlexaSkills/issues
