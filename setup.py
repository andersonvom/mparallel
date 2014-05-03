from setuptools import setup, find_packages  # noqa


setup(
    name='mparallel',
    version='0.0.1',
    packages=find_packages(),
    author="Anderson Mesquita",
    author_email="andersonvom@gmail.com",
    description=("A minimalist tool to run multiple parallel tasks in Python"),
    long_description=open('README.rst').read(),
    license="MIT",
    url="https://github.com/andersonvom/mparallel",
    keywords=("python parallel mparallel simple minimalist thread threaded "
              "concurrent task runner"),
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Development Status :: 3 - Alpha"
    ]
)
