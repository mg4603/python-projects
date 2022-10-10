try:
    from setuptools import find_packages, setup
except ImportError:
    from distutils.core import find_packages , setup

config = {
    'name': 'Installable flask app',
    'version': '0.0.1',
    'packages': find_packages(),
    'include_package_data': True,
    'install_requires': ['flask', ],
}   

if __name__ == '__main__':
    setup(**config)