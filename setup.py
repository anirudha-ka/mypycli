from setuptools import setup

from mypycli import __app_name__, __version__

setup(
    name=__app_name__ if __app_name__ else "mypycli",
    version=__version__ if __version__ else "0.2.0",
    packages=[f"{__app_name__}"],
    entry_points={
        "console_scripts": [
            f"{__app_name__}={__app_name__}.__main__:main"
        ]
    }
)