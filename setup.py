from setuptools import setup

setup(
    name='Avine',
    url='https://github.com/MinNq/avine',
    author='Minh Nguyen',
    author_email='nguyenquangminhptnk@gmail.com',
    packages=['avine'],
    install_requires=['numpy', 'matplotlib'],
    version='0.1',
    license='MIT',
    description='Avine - a module for visualization of affine transformations in 2-d Euclidean space',	
    long_description=open('README.txt').read(),
)
