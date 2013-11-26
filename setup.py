from setuptools import setup, find_packages

setup(
    name='w3c_ebnflexer',
    packages=find_packages(),
    entry_points="""
[pygments.lexers]
w3c_ebnflexer = w3c_ebnflexer:W3CEbnfLexer
"""
)
