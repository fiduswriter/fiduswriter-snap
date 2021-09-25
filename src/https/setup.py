from setuptools import setup, find_packages


setup(
	name='fiduswriter',
	packages=find_packages(),
	install_requires=[
		'certbot',
		'zope.interface',
	],
	entry_points={
		'certbot.plugins': [
			'webroot = certbot_fiduswriter_plugin.webroot:Authenticator',
		],
	},
)
