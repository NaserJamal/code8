from setuptools import setup, find_packages

setup(
    name='test8',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'openai',
    ],
    entry_points={
        'console_scripts': [
            'test8=test8:main',
        ],
    },
)