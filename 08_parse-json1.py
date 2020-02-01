import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
orig = "Quito"
dest = "Ambato"
key = "GiznN7QdIXi6wX1gAg3vYabfGXQOQ4WP"
url = main_api+urllib.parse.urlencode({"key":key,"from":orig,"to":dest})

json_data = requests.get(url).json()
print(json_data)