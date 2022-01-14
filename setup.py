from setuptools import setup
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = "0.0.1"
DESCRIPTION = (
    "This is the package provides direct-stream url and other details about a video"
)

_license = "MIT"
author = "DARKPOISON04"
setup(
    name="audioextractor",
    description="A Module that provides direct-stream url and other details about a video",
    long_description=long_description,
    long_description_content_type="text/markdown",
    version=VERSION,
    packages=["audioextractor"],
    url="https://github.com/Darkpoison04/Audio-Extractor-Py",
    download_url=f"https://github.com/Darkpoison04/Audio-Extractor-Py/archive/v{VERSION}.tar.gz",
    license=_license,
    author=author,
    install_requires=["youtube_dl"],
    keywords=["audioextractor", "discord", "api", "wrapper", "youtube", "discord.py"],
    project_urls={
        "Discord": "https://discord.gg/TXSpYASF4Y",
        "Source": "https://github.com/Darkpoison04/Audio-Extractor-Py",
        "Issue tracker": "https://github.com/Darkpoison04/Audio-Extractor-Py/issues",
    },
    python_requires=">=3.6",
)
