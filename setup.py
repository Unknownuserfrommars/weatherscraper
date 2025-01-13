from setuptools import setup, find_packages

setup(
    name='weatherscraper',
    version='1.1',
    author='Your Name',
    author_email='unknownuserfrommars@protonmail.com',
    description='A module to scrape weather data from weather.com',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=['Flask', 'requests', 'beautifulsoup4'],
    python_requires='>=3.10',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)