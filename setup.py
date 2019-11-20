from setuptools import setup


def parse_version():
    with open("infer_license/__init__.py") as f:
        for line in f:
            if line.startswith("__version__"):
                return line.split()[-1].strip("\"'")

setup(
    version=parse_version(),
    python_requires=">=3.6",
    install_requires=["dataclasses >= 0.7; python_version < '3.7'",],
)

