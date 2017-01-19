from setuptools import setup


setup(
    name='Flask-Stripe',
    version='0.1.0',
    description='Flask-Stripe',
    author='Boris Raicheff',
    author_email='b@raicheff.com',
    url='https://github.com/raicheff/flask-stripe',
    install_requires=['flask', 'six', 'stripe'],
    packages=['flask_stripe'],
)
