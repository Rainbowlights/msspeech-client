from setuptools import setup

setup(
    name='msspeech_client',
    python_requires='>=3.6.0',
    version='1.0',
    author='Descriptwer',
    author_email='descriptwer@descriptwer.com',
    packages=['msclient'],
    license='LICENSE.txt',
    description='Client MS Speech Bing',
    install_requires=['websockets', 'asyncio', 'requests'],
    entry_points={
        'console_scripts': [
            'msspeech = msclient.__main__:main'
        ]
    },
    keywords=['audio', 'msbing', 'speech', 'text', 'client'],
    classifiers=[
        "Development Status :: 1 - Production/Stable",
        "Environment :: Console",
        "Programming Language :: Python",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Client ASR",
        "Topic :: Utilities",
        "License :: OSI Approved :: Apache Software License"
    ]
)
