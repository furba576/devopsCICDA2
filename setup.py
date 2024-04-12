from setuptools import setup, find_packages

setup(
    name='task_manager',
    version='1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'task_manager = task_manager:main'
        ]
    },
    install_requires=[],
    tests_require=['pytest'],
)
