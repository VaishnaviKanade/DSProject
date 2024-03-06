from setuptools import find_packages 
from setuptools import setup
from typing import List

HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    '''
       get the requiremts from the requirements.txt
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

setup(
    name='MLProject',
    version='0.0.1',
    author='Vaishnavi Kanade',
    author_email='vaishnavikanade2003@gmail.com',
    # install_requires=['pandas','seaborn','numpy']
    install_requires=get_requirements('requirements.txt')
    )