#
# Flask-Stripe
#
# Copyright (C) 2017 Boris Raicheff
# All rights reserved
#


import logging

import stripe

from .routes import webhooks


logger = logging.getLogger('Flask-Stripe')


class Stripe(object):
    """
    Flask-Stripe

    Refer to http://flask-stripe.readthedocs.org for
    more details.

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
            blueprint.add_url_rule('/stripe', 'stripe', webhooks, methods=['POST'])


# EOF
