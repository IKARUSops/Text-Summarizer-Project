import setuptools

with open("README.md","r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "Text-Summarizer-Project"
AUTHOR_USER_NAME = "IKARUSops"
SRC_REPO = "textsummarizer"
AUTHOR_EMAIL = "sharif.md.omar.faruq1@gmail.com"
PACKAGE_ROOT = "src/textsummarizer/src"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for NLP app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker" : f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"
    },
    package_dir={"": PACKAGE_ROOT},
    packages=setuptools.find_packages(where=PACKAGE_ROOT)
)