from setuptools import setup, config

if __name__=="__main__":
    setup(
        name = 'OnPremiseDataPipeline',
        version = 1.0,
        author = 'hao-dang',
        author_email = 'haodang2311@gmail.com',

        install_requires = config.read('setup.cfg')['install_requires'],
    )