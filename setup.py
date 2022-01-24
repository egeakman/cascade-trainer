import json
import urllib.request
from xml.etree.ElementInclude import include
from setuptools import setup, find_packages


def latest_version(package_name):
    url = f"https://pypi.python.org/pypi/{package_name}/json"
    try:
        response = urllib.request.urlopen(urllib.request.Request(url), timeout=1)
        data = json.load(response)
        versions = data["releases"].keys()
        versions = sorted(versions)
        return ">={}".format(versions[-1])
    except Exception:
        pass
    return ""


with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="cascade-trainer",
    author="Ege Akman",
    author_email="egeakmanegeakman@hotmail.com",
    url="https://github.com/egeakman/cascade-trainer",
    description="An OpenCV based cascade trainer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    version="2022.1.24-9",
    license="AGPLv3",
    download_url="https://github.com/egeakman/cascade-trainer/archive/2022.1.24-9.tar.gz",
    packages=find_packages(where=".", exclude=["tests"]),
    include_package_data=True,
    package_data={"data": ["data/*.*"]},
    zip_safe=False,
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "cascade-trainer=cascade_trainer.train:main",
        ]
    },
    install_requires=[
        f"setuptools{latest_version('setuptools')}",
        f"opencv-python{latest_version('opencv-python')}",
    ],
    keywords=[
        "OpenCV",
        "Cascade",
        "Trainer",
        "CLI",
        "Haar" "Object Detection",
        "Video Processing",
        "Computer Vision",
    ],
    classifiers=[
        "Topic :: Utilities",
        "Topic :: Scientific/Engineering :: Image Recognition",
        "Topic :: Scientific/Engineering",
        "Topic :: Software Development",
        "Programming Language :: Python :: 3 :: Only",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Environment :: Console",
        "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
        "Operating System :: Microsoft :: Windows",
    ],
    project_urls={
        "Homepage": "https://github.com/egeakman/cascade-trainer",
        "Issues": "https://github.com/egeakman/cascade-trainer/issues",
    },
)
