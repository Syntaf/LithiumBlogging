CSRF_ENABLED = True
SECRET_KEY = 'gmoney'

OPENID_PROVIDERS = [
		{ 'name': 'Google', 'url': 'https://www.google.com/account/o8/id'},
		{ 'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
		{ 'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
		{ 'name': 'MyOpenID', 'url': 'https://www.myopenid.com' }]
