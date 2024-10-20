from setuptools import setup, find_packages

setup(
    name="ResponsiveWiz",
    version="0.1",
    author="Ved Patel",
    author_email="talk2ved11@gmail.com",
    description="A tool for making your website responsive",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/ved-patel226/ResponsiveWiz",
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "selenium",
        "termcolor",
        "tqdm",
        "pillow",
        "flask",
        "flaskwebgui",
        "flask_socketio",
        "matplotlib",
    ],
    include_package_data=True,
    package_data={
        '': ['src/responsiveWiz/data/responsiveOptions.json'],  # Include the JSON file
    },
)
