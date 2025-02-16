from setuptools import setup, find_packages


setup(
    name='vieweryolo',
    version='0.1',
    packages=find_packages(),
    install_requires=[  
        'PyQt6',
        'opencv-python',
        'numpy',
        'PyYAML',
    ],
    entry_points={
        'console_scripts': [
            'vieweryolo=vieweryolo.gui:main',
        ],
    },
    long_description=open('README.md').read(),  
    long_description_content_type='text/markdown',
)