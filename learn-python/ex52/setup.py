try:
    from setuptools import find_packages, setup
except ImportError:
    from distutils.core import find_packages, setup

config = {
    'name': 'ex52',
    'version': '0.0.1',
    'description': 'Ex43 game refactored to use a web ui',
    'package': find_packages(),
    'include_package_data': True,
    'install_requires': [
        'flask',
    ],
    'author': 'mg4603',
}

if __name__ == '__main__':
    setup(**config)