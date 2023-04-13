from setuptools import setup, find_packages

setup(
    name='dns',
    version='0.1.4',
    description='A command to query all DNS records for a (sub)domain.',
    author='Sander Bongers',
    author_email='sander@bonge.rs',
    url='https://github.com/sanderbongers/dns',
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
    ],
    entry_points={
        'console_scripts': ['dns=bin.dns:dns'],
    },
)
 