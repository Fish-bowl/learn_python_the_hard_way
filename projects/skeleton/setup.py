try: 
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'Derscription' : 'My Project',
	'Author' : 'Max Whitaker',
	'url' : 'url to get it at',
	'download_url' : 'were to download',
	'author_email' : 'symbolt.ap@gmail.com',
	'version' : '0.1',
	'install requires' : ['nose'],
	'packages' : ['NAME'],
	'scripts' : [],
	'name' : 'projectname'
}

setup(**config)


