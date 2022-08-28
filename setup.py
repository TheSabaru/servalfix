from setuptools import setup, find_packages

requirements = [
    "requests",
    "websocket-client==1.3.1", 
    "setuptools", 
    "json_minify", 
    "six",
    "aiohttp",
    "pysocks",
    "poetry",
    "websockets"
]

with open("README.md", "r") as stream:
    long_description = stream.read()

setup(
    name="serval.fix",
    license='MIT',
    author="Capuchino",
    version="2.3.4.11",
    author_email="chocolabienid@gmail.com",
    description="Library for AminoApps. Discord - https://discord.gg/7NmhxQBmET",
    url="https://github.com/Minori100/Amino.fix",
    packages=find_packages(),
    long_description=long_description,
    install_requires=requirements,
    keywords=[
        'aminoapps',
        'serval.fix',
        'serval',
        'serval-bot',
        'narvii',
        'amino',
        'api',
        'python',
        'python3',
        'python3.x',
        'serval.fix.py',
        'serval-amino',
        'capuchino'
    ],
    python_requires='>=3.6',
)
