from setuptools import setup

setup(
    use_scm_version=True,
    python_requires=">=3.6",
    install_requires=["dataclasses >= 0.7; python_version < '3.7'",],
    entry_points={"console_scripts": ["infer_license = infer_license.cmdline:main"]},
    include_package_data=True,
)
