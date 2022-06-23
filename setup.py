from setuptools import find_packages, setup

setup(
    name="promclient-py",
    version="0.0.1",
    author="Bader AlAttar",
    description="Prometheus Client",
    python_requires=">=3.10",
    packages=find_packages(),
    package_data={
        "": ["*"],
    },
    install_requires=[
        "requests",
        "click",
        "matplotlib",
    ],
    extras_require={
        "dev": [
            "black",
            "isort",
            "mypy",
            "types-requests",
        ],
    },
    entry_points={
        "console_scripts": [
            "prom=promclient.cli:cli",
        ],
    },
)
