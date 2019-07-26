from setuptools import setup

setup(
    name="vinnie",
    version="0.0.1",
    py_modules=["vinnie"],
    install_requires=["Click==7.0", "semver==2.8.1", "GitPython==2.1.11"],
    tests_require=["pytest==5.0.1", "pytest-sugar==0.9.2", "pytest-cov==2.7.1"],
    entry_points="""
        [console_scripts]
        vinnie=vinnie.cli:cli
    """,
)
