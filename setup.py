from setuptools import setup

setup(
    name='flask-latency',
    version='0.1',
    url='http://github.com/closeio/flask-latency',
    license='MIT',
    description='Simulate latency in a Flask development environment',
    platforms='any',
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
    packages=[
        'flask_latency',
    ],
)
