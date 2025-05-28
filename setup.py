import setuptools # type: ignore

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

__version__ = "0.0.0"

REPO_NAME = "detectionClassifier"
AUTHOR_USER_NAME = "chandra sekhar"
SRC_REPO = "detectionClassifier"
AUTHOR_EMAIL = "email"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for detectionClassifier",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # url=f""
    # project_urls={

    # },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
)
