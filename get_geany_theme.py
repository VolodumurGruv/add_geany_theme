# visit https://geany.org/download/themes/ and chose a theme
# it works for linux
# where themes located at ~/.config/geany/colorschemes/

from requests import get
from os import path, access, W_OK

home_path = input("Write your home path:\n")
schemes_path = ".config/geany/colorschemes"
full_path = path.join(home_path, schemes_path)

def put_theme(name, data):
	try:
		with open(f"{full_path}/{name}.conf", 'xt') as theme:
			theme.write(data)
	except Exception as err:
		print(err)

if access(full_path, W_OK):
	print('''visit https://geany.org/download/themes/
	and pick up a github link of desired theme''')
	
	url = input("Paste the url of desired theme:\n")
	is_name = input("Do you want to set up the name of scheme (yes/no)?\n")
	data = get(url).text
	name = ''
	
	if is_name.lower() == "yes":
		name = input("Set up the name:\n")

		
	if name:
	    put_theme(name, data)
	else:
		name = data[data.find("name=") + 5 : data.find("name=") + 25].split('\n')[0].lower()
		
		put_theme(name, data)
else:
	print('''check your home path, it should start with /\n
	or you don't have a premision to write in that directory'''	)
