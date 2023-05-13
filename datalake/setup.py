from setuptools import find_packages, setup

setup(
    name="datalake",
    packages=find_packages(exclude=["datalake_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud",
        "duckdb",
        "pandas",
        "sqlescapy",
        "lxml",
        "html5lib"
    ],
    extras_require={"dev": ["dagit", "pytest", "localstack","awscli","awscli-local" ]},
)
