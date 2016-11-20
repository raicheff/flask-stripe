from setuptools import setup


setup(
    name='flask-stripe',
    version='0.1.0',
    description='Flask-Stripe',
    author='Boris Raicheff',
    author_email='b@raicheff.com',
    url='https://github.com/raicheff/flask-stripe',
    install_requires=['flask', 'stripe'],
    packages=['flask_stripe'],
)
