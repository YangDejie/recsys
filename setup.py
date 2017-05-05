import os.path
try:
    from setuptools import setup, Extension
except ImportError:
    from distutils.core import setup, Extension

VERSION = "0.1"

setup(
    name = "recsys",
    version = VERSION,
    description="A simple recommender system using MovieLens",
    author='idejie',
    author_email='i@idejie.com',
    maintainer='idejie',
    maintainer_email='i@idejie.com',
    license = "http://www.gnu.org/copyleft/gpl.html",
    platforms = ["any"],    
    url="http://github.com/yangdejie/recsys",
    package_dir={'recsys':'recsys'},
    packages=['recsys', 'recsys.algorithm', 'recsys.datamodel', 'recsys.evaluation', 'recsys.utils'],
    install_requires = ["numpy", "scipy", "divisi2", "csc-pysparse"],
)
