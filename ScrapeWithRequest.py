import requests
import datetime
import os

today = str(datetime.datetime.now()).split(' ')[0]

sites = {'AllRecipes': 'http://allrecipes.com/recipes/?sort=Newest',
         'Epicurius': 'http://www.epicurious.com/search/?sort=newest&content=recipe',
         'Delish': 'http://www.delish.com/recipes/'}

for name, link in sites.items():
    response = requests.get(link)
    html = response.content

    path = '/home/nolan/Programming/CSC3130_WebProject/HTML/'
    if not os.path.exists(path):
        os.makedirs(path)
    fileName = path + today + '.' + name + '.html'
    outfile = open(fileName, "wb")
    outfile.write(html)
    outfile.close()