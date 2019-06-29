from setuptools import setup, find_packages

def long_description():
    with open("README.md") as infile:
        return infile.read()

def license():
    with open("LICENSE") as infile:
        return infile.read()

setup(
    name="GCloudPyProxy",
    version="0.9rc3",
    packages=find_packages(),
    author="Tomas Votava",
    author_email="info@tomasvotava.eu",
    description="This package provides proxy class for calling gcloud commands directly from Python.",
    keywords="gcp google cloud platform gcloud python proxy",
    url="https://github.com/tomasvotava/gcloud-pyproxy",
    project_urls={
        "Bug Tracker": "https://github.com/tomasvotava/gcloud-pyproxy/issues",
        "Documentation": "https://github.com/tomasvotava/gcloud-pyproxy/blob/master/README.md",
        "Source Code": "https://github.com/tomasvotava/gcloud-pyproxy"
    },
    classifiers=[
        "License :: OSI Approved :: MIT License"
    ],
    long_description=long_description(),
    download_url="https://github.com/tomasvotava/gcloud-pyproxy",
    license=license()
)

