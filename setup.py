from setuptools import setup, find_packages

VERSION = '0.0.0'
DESCRIPTION = 'module designed to make your data preprocessing experience easier'
with open("README.md") as description:
    LONG_DESCRIPTION = description.read()

# Setting up
setup(
    name="irdatacleaning",
    version=VERSION,
    author="Islander Robotics (William McKeon)",
    author_email="<IslanderRobotics@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=["pandas","matplotlib","PyQt5","scikit-learn","IslanderDataPreprocessing"],
    keywords=['python',"machine Learning", "Artificial Intelligence","Data Science","Data Cleaning"],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3"
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8"
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Topic"::"Machine Learning",
        "Topic"::"Data Cleaning"
        "Topic":: "Data Science"
    ]
)
