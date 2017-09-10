from setuptools import setup


setup(
    name='cmcwrap',
    version='0.1.5',
    platforms='osx, linux',
    author='Brandon Johnson',
    license=open('LICENSE').read(),
    packages=['cmcwrap', 'cmcwrap.test'],
    install_requires=['requests', 'pytest'],
    long_description=open('README.md').read(),
    url='https://github.com/bitforce/cmcwrap',
    author_email='brandon.johnson.official@gmail.com',
    keywords=['coinmarketcap', 'cryptocurrency', 'wrapper'],
    description='Python wrapper created for https://coinmarketcap.com API',
    download_url='https://github.com/bitforce/cmcwrap/archive/1.0.0.tar.gz',
    classifiers=[
        'Natural Language :: English',
        'Intended Audience :: Developers',
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 2.7']
)
