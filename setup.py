from setuptools import setup

setup(
    name='weatherscraper',
    version='1.0.1',
    py_modules=['weatherscraper'],  # Point to the single module
    install_requires=[
        'requests',
        'beautifulsoup4'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10',
)