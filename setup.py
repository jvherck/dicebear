from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

__version__ = "0.2.4"
DESCRIPTION = "A python API wrapper for DiceBear's avatar generating API."

setup(
    name="dicebear",
    version=__version__,
    author="jvherck",
    author_email="<jvh.discord@gmail.com>",
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=['requests', 'urllib3'],
    keywords=['python', 'dicebear', 'avatar', 'generating', 'API', 'wrapper', 'image', 'svg'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Other Audience",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "License :: OSI Approved :: MIT License",
        "Topic :: Artistic Software",
        "Topic :: Games/Entertainment",
        "Topic :: Multimedia :: Graphics"
    ]
)
