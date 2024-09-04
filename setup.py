from setuptools import setup

setup(name='dev_aberto_thiagohpr',
      version='0.1',
      packages=['dev_aberto'],
      install_requires=[
        'requests==2.32.3',
        'urllib3==2.2.2',
        'setuptools==74.1.1'
        ],
        scripts=['scripts/hello.py']
      )