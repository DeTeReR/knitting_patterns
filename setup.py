from distutils.core import setup

setup(
	name='knitting_patterns',
	version='0.0.1',
	packages=['src.knitting'],
	url='https://github.com/DeTeReR/knitting_patterns',
	license='MIT License  Copyright (c) 2016',
	author='Daniel Royde',
	author_email='danielroyde@gmail.com',
	description='A package for generating knitting patterns from images.',
	install_requires=[
		'pillow',
	],
)
