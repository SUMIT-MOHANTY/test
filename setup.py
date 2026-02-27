from setuptools import setup, find_packages

setup(
    name='flask-api-template',
    version='1.0.0',
    description='Flask REST API Template',
    author='Development Team',
    packages=find_packages(),
    install_requires=[
        'flask>=2.3.0',
        'python-dotenv>=1.0.0',
        'pyyaml>=6.0',
        'sqlalchemy>=2.0.0',
        'flask-sqlalchemy>=3.0.0',
    ],
    python_requires='>=3.9',
)
