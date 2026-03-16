### create setup.py file for the project
from setuptools import setup, find_packages

### create function to import packages from requirements.txt file
def get_requirements(file_path:str) -> list[str]:
    requirements = []
    with open(file_path, 'r') as file_obj:
        requirements = file_obj.readlines()
        ### replace /n with empty string
        requirements = [req.replace('\n', '') for req in requirements]
        ### remove -e . from requirements

        if '-e .' in requirements:
            requirements.remove('-e .')
        
    return requirements

setup(
    name='mlprojectkn',
    version='0.1',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
    description='A machine learning project for classification',
    author='Sudhanshu',
    author_email='sudhanshu@example.com'
)   