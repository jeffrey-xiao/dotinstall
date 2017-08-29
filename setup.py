from distutils.core import setup

setup(
    name='dotinstall',
    packages=[
        'dotinstall',
        'dotinstall.plugins',
        'dotinstall.installer',
        'dotinstall.util',
    ],
    install_requires=[
        'PyYAML',
    ],
    version='0.6.0',
    description='Command-line tool to help install and setup your dotfiles.',
    author='Jeffrey Xiao',
    author_email='jeffrey.xiao1998@gmail.com',
    url='https://github.com/jeffrey-xiao/dotinstall',
    download_url='https://github.com/jeffrey-xiao/dotinstall/archive/0.6.0.tar.gz',
    keywords=['dotfiles', 'commandline'],
    classifiers=[],
    entry_points={
        'console_scripts': [
            'dotinstall=dotinstall.dotinstall:main',
        ],
    },
)
