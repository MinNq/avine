from setuptools import setup

setup(
    name='AffineVi',
    url='https://github.com/MinNq/affinevi',
    author='Minh Nguyen',
    author_email='nguyenquangminhptnk@gmail.com',
    packages=['affinevi'],
    install_requires=['numpy', 'matplotlib'],
    version='0.1',
    license='MIT',
    description='AffineVi - a module for visualization of affine transformations in 2-d Euclidean space',	
    long_description=open('README.txt').read(),
)
