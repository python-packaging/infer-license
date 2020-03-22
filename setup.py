from setuptools import setup

setup(
    use_scm_version=True,
    entry_points={"console_scripts": ["infer_license = infer_license.cmdline:main"]},
)
