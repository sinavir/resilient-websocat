from setuptools import setup

setup(
    name='rwebsocat',
    version='1.0',
    packages=['rwebsocat'],
    install_requires=[
        'websockets',
    ],
    entry_points={
        'console_scripts': [
            'rwebsocat = rwebsocat:main',
        ]
    }
)
