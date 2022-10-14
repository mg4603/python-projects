try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

if __name__ == "__main__":
    setup(**config)