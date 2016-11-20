#
# Flask-Stripe
#
# Copyright (C) 2014 Boris Raicheff
# All rights reserved
#


import logging

from flask import Response, current_app, request
from stripe import Event

from .signals import namespace


TEST_EVENT_ID = 'evt_00000000000000'


logger = logging.getLogger('Flask-Stripe')


def webhooks():
    """
    https://stripe.com/docs/webhooks
    https://stripe.com/docs/api#event_types
    ---
    https://www.petekeen.net/stripe-webhook-event-cheatsheet
    """
    event_id = request.get_json().get('id')
    logger.info('event_id=%s', event_id)

    if event_id != TEST_EVENT_ID:
        event = Event.retrieve(event_id)
        signal = namespace.signal(event.type)
        signal.send(current_app._get_current_object(), object=event.data.object)
        logger.info('event=%s', event)

    return Response(status=202)  # ACCEPTED


# EOF
