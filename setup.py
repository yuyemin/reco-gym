import os

from setuptools import setup

cwd = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'requirements.txt')
with open(cwd) as f:
    dependencies = list(map(lambda x: x.replace("\n", ""), f.readlines()))

setup(
    name='reco-gym',
    url='https://github.com/yuyemin/reco-gym.git',
    description='POMDP recommendation system framework for MovieLens data set',
    install_requires=dependencies,
    packages=['gym_recommendation'],
)
