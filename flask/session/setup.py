try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

config = {
    'name': 'Session Flask app',
    'version': '0.0.1',
    'packages': find_packages(),
    'include_package_data': True,
    'install_requires': [
        'flask',
    ],
    'description': 'Flask app to implement session'
}

if __name__ == "__main__":
    setup(**config)