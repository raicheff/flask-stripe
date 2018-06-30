#
# Flask-Stripe
#
# Copyright (C) 2017 Boris Raicheff
# All rights reserved
#


from setuptools import find_packages, setup


setup(
    name='Flask-Stripe',
    version='0.1.0',
    description='Flask-Stripe',
    author='Boris Raicheff',
    author_email='b@raicheff.com',
    url='https://github.com/raicheff/flask-stripe',
    install_requires=('flask', 'six', 'stripe'),
    packages=find_packages(),
)


# EOF
