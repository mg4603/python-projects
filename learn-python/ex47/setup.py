try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup



config = {
    "description": "Project to learn automated testing",
    "author": "mg4603",
    "url": "URL to get it at",
    "download_url": "Where to download it",
    "author_email": "mgeo4603@gmail.com",
    "version": "0.1",
    "install_requires": ['nose'],
    "packages": ["ex47"],
    "scripts":  [],
    "name": "ex47"
}


if __name__ == "__main__":
    setup(**config)