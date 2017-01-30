#
# Flask-Stripe
#
# Copyright (C) 2017 Boris Raicheff
# All rights reserved
#


import logging

import stripe

from flask import Response, request
from six.moves.http_client import OK
from stripe import Event

from .signals import namespace


logger = logging.getLogger('Flask-Stripe')


# https://stripe.com/docs/ips
STRIPE_IPS = (
    '54.187.174.169',
    '54.187.205.235',
    '54.187.216.72',
    '54.241.31.99',
    '54.241.31.102',
    '54.241.34.107',
)

TEST_EVENT_ID = 'evt_00000000000000'


class Stripe(object):
    """
    Flask-Stripe

    https://pypi.python.org/pypi/flask-stripe

    https://flask-stripe.readthedocs.io

    :param app: Flask app to initialize with. Defaults to `None`
    """

    def __init__(self, app=None, blueprint=None):
        if app is not None:
            self.init_app(app, blueprint)

    def init_app(self, app, blueprint=None):
        stripe_key = app.config.get('STRIPE_SECRET_KEY')
        if stripe_key is None:
            logger.warning('STRIPE_SECRET_KEY not set')
            return
        stripe.api_key = stripe_key

        if app.debug:
            stripe.verify_ssl_certs = False

        if blueprint is not None:
            blueprint.add_url_rule('/stripe', 'stripe', self.handle_webhook, methods=('POST',))

    def handle_webhook(self):
        """
        https://stripe.com/docs/webhooks
        https://stripe.com/docs/api#event_types
        ---
        https://www.petekeen.net/stripe-webhook-event-cheatsheet
        """
        event_id = request.get_json().get('id')
        logger.info('event_id=%s', event_id)

        if event_id == TEST_EVENT_ID:
            return Response(status=OK)

        event = Event.retrieve(event_id)
        namespace.signal(event.type).send(self, object=event.data.object)
        logger.info('event=%s', event)

        return Response(status=OK)

    def __getattr__(self, name):
        return getattr(stripe, name)


# EOF
