try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup



config = {
    "description": "A text based adventure game",
    "author": "mg4603",
    "url": "URL to get it at",
    "download_url": "Where to download it",
    "author_email": "mgeo4603@gmail.com",
    "version": "0.1",
    "install_requires": ['nose'],
    "packages": ["ex43"],
    "scripts":  [],
    "name": "ex43"
}


if __name__ == "__main__":
    setup(**config)