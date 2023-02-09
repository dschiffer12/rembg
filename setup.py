import os
import pathlib
import sys
import versioneer
sys.path.append(os.path.dirname(__file__))
from setuptools import find_packages, setup



here = pathlib.Path(__file__).parent.resolve()

long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="rembg",
    description="Remove image background",
    long_description=long_description,
    long_description_content_type="text/markdown",

    )


