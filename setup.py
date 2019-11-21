from setuptools import setup

setup(
    use_scm_version=True,
    install_requires=["dataclasses >= 0.7; python_version < '3.7'",],
    entry_points={"console_scripts": ["infer_license = infer_license.cmdline:main"]},
)
