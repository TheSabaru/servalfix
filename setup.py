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
    name="servalfix",
    license='MIT',
    author="Capuchino",
    version="2.3.4.11.1",
    author_email="chocolabienid@gmail.com",
    description="Library for AminoApps. Discord - https://discord.gg/7NmhxQBmET",
    url="https://github.com/TheSabaru/servalfix",
    packages=find_packages(),
    long_description=long_description,
    install_requires=requirements,
    keywords=[
        'aminoapps',
        'servalfix',
        'servalfix',
        'serval',
        'serval-bot',
        'narvii',
        'amino',
        'api',
        'python',
        'python3',
        'python3.x',
        'servalfix.py',
        'serval-amino',
        'capuchino'
    ],
    python_requires='>=3.6',
)
