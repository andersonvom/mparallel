from setuptools import setup, find_packages  # noqa


setup(
    name='parallel',
    version='0.0.1',
    packages=find_packages(),
    author="Anderson Mesquita",
    author_email="andersonvom@gmail.com",
    description=("A minimalist way to parallelize tasks in Python"),
    long_description=open('README.rst').read(),
    license="MIT",
    url="https://github.com/andersonvom/python-parallel",
    keywords="python parallel simple thread threaded concurrent task runner",
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Development Status :: 3 - Alpha"
    ]
)
