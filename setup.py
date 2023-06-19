from setuptools import setup

setup(
    name='ImageStickyNote',
    version='1.0',
    author='Haitham Ghaida',
    author_email='haitham.ghaida@outlook.com',
    description='Display an image as a stickynote on the desktop',
    py_modules=['ImageStickyNote'],
    entry_points={
        'console_scripts': [
            'ImageStickyNote = ImageStickyNote:main',
        ],
    },
)

