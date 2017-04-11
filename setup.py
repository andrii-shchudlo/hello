
from setuptools import setup, find_packages

setup(
    name = "hello",
    packages = find_packages('src'),
    package_dir = {'': 'src'},
    install_requires = ['setuptools'],
    entry_points = """\
      [console_scripts]
      hello = hello.main:hello
      """
)
