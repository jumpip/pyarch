from setuptools import setup, find_packages
setup(
    name='pyarch',
    version='0.0.1',
    description='Hardware emulation library in python',
    url='https://github.com/mansimarkaur/Hardware_abstraction',
    author='Prachi Manchanda',
    author_email='prachi121096@gmail.com',
    license='MIT',
     classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
    packages=find_packages(),
    install_requires=['pyee','hiatus'],
)
