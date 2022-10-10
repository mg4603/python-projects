try:
    from setuptools import find_packages, setup
except ImportError:
    from distutils.core import find_packages, setup


if __name__ == '__main__':
    setup(**config)