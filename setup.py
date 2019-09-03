import setuptools


setuptools.setup(
    name="pipenv-hello-world",
    version="0.0.1",
    author="Canonical LTD",
    author_email="snapcraft@lists.snapcraft.io",
    description="A simple hello-world in python using pipenv",
    entry_points={ 'console_scripts': ['pipenv-hello-world=hello:main'] },
    packages=setuptools.find_packages(),
)
