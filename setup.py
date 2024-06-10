from setuptools import setup

setup(
    name="mypycli",
    version="0.1.0",
    packages=["mypycli"],
    entry_points={
        "console_scripts": [
            "mypycli=mypycli.__main__:main"
        ]
    }
)