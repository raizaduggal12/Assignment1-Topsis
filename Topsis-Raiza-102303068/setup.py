from setuptools import setup, find_packages

setup(
    name="Topsis-Raiza-102303068",
    version="1.0.0",
    author="Raiza Duggal",
    author_email="raiza@example.com",
    description="TOPSIS implementation for multi-criteria decision making",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pandas"
    ],
    entry_points={
        "console_scripts": [
            "topsis=topsis_raiza_102303068.topsis:main"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires=">=3.7"
)
