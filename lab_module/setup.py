from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='devices_rxm',
      version='0.1',
      description=readme(),
      author='RX-M Trainer',
      author_email='trainer@rxm.com',
      scripts=['bin/device'],
      license='MIT',
      packages=['devices'],
      zip_safe=False)