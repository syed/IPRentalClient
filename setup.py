from distutils.core import setup

setup(
    name='IPRentalClient',
    version='0.1',
    author='Syed M Ahmed',
    author_email='syed1.mushtaq@gmail.com',
    packages=['iprental'],
    url='http://iprental.com',
    license='LICENSE.txt',
    description='simple IPRental Client to get proxies',
    long_description=open('README.txt').read(),
    install_requires=[
        "suds",
    ],
)