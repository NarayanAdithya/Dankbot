from distutils.core import setup
from setuptools import find_packages

with open('requirements_dev.txt') as req:
    requirements = req.readlines()

setup(
    name='dankbot',         
    packages=find_packages(),
    version='0.1',      # Start with a small number and increase it with every change you make
    license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    description='All in one bot to manage your dankmemer account. Easy automaton for grinding money and collectables.',  # Give a short description about your library
    author='Adithya Narayan',                   # Type in your name
    author_email='narayanadithya1234@gmail.com',      # Type in your E-Mail
    entry_points={'console_scripts': ['dankbot = dankbot.dankcli:run_bot']},
    url='https://github.com/NarayanAdithya/Dankbot',   # Provide either the link to your github or to your website
    download_url='https://github.com/NarayanAdithya/Dankbot/archive/refs/tags/v_0.1-beta.tar.gz',    # I explain this later on
    keywords=['Discord', 'Automation', 'DankBot', 'Dank Memer'],   # Keywords that define your package best
    install_requires=requirements,
    classifiers=[
        'Development Status :: 4 - Beta',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers, Discord Users',      # Define that your audience are developers
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',  
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9'
    ],
)
