from setuptools import setup

setup(
    name='py_game_of_life',
    version='1.1',
    description='Conway\'s Game of Life Simulation, implemented with pygame',
    long_description="See https://github.com/BodaSadalla98/Cookbook/game_of_live",
    url='https://github.com/BodaSadalla98/Cookbook/game_of_live',
    author='BodaSadalla',
    author_email='boda998@yahoo.com',
    license='GPL-3.0',
    packages=['pygameoflife'],
    entry_points={
        'console_scripts': [
            'py_game_of_life = pygameoflife.__main__:main',
        ],
    },

    zip_safe=False,
    install_requires=[
        'pygame'
    ],
    python_requires='>=3.0',
)