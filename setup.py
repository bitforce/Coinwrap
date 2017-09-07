from setuptools import setup


setup(
    name='cmcwrap',
    version='0.0.7',
    packages=['cmcwrap'],
    author='Brandon Johnson',
    license=open('./LICENSE', 'r').read(),
    install_requires=['requests', 'pytest'],
    long_description=open('./README.md', 'r').read(),
    author_email='brandon.johnson.official@gmail.com',
    keywords=['coinmarketcap', 'cryptocurrency', 'wrapper'],
    url='https://github.com/bitforce/wrapper-py-coinmarketcap',
    description='Python wrapper created for https://coinmarketcap.com API',
    download_url='https://github.com/bitforce/wrapper-py-coinmarketcap/archive/1.0.1.tar.gz',
    classifiers=[
        'Natural Language :: English',
        'Intended Audience :: Developers',
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 2.7']
)
