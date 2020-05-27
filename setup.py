from setuptools import setup

setup(
    name="ramble-rixx-de",
    author="Tobias Kunze",
    author_email="r@rixx.de",
    url="https://github.com/rixx/ramble.rixx.de",
    packages=["scripts"],
    entry_points="""
        [console_scripts]
        posts=scripts.cli:cli
    """,
    install_requires=[
        "click",
        "inquirer==2.6.*",
        "python-frontmatter==0.5.*",
        "unidecode==1.1.*",
    ],
)
