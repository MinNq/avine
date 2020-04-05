from setuptools import setup

setup(
    name='Affine',
    url='https://github.com/MinNq/affine',
    author='Minh Nguyen',
    author_email='nguyenquangminhptnk@gmail.com',
    packages=['affine'],
    install_requires=['numpy', 'matplotlib'],
    version='0.1',
    license='MIT',
    description='Affine - a module for visualization of affine transformations in 2-d Euclidean space',	
    long_description=open('README.txt').read(),
)