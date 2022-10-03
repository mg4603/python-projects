try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup



config = {
    "description": "A project demonstrate advanced user input",
    "author": "mg4603",
    "url": "URL to get it at",
    "download_url": "Where to download it",
    "author_email": "mgeo4603@gmail.com",
    "version": "0.1",
    "install_requires": ['nose'],
    "packages": ["ex48"],
    "scripts":  [],
    "name": "ex48"
}


if __name__ == "__main__":
    setup(**config)