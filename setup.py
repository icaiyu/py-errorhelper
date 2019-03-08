# encoding: utf-8
from setuptools import setup
with open("README.md",encoding='utf-8') as f:
	long_description = f.read()

setup(name='errorhelper',
	version='0.1.6',
	py_modules=['errorhelper',],
	description="A tool for python beginer to understand exception or error in Chinese. 一款帮助中国python初学者看懂错误的工具",
	long_description=long_description,
	long_description_content_type="text/markdown",
	author_email="icaiyu@163.com",
	url="https://github.com/icaiyu/py-errorhelper",
	auther="cy",
	license="MIT",
	zip_safe=False
)
