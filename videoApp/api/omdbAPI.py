'''
VideoAPI set up from www.omdbapi.com
returns a json doc every time a search querry is entered
with all movie information such as:
    *Title
    *Cast
    *Director
    *Year
    *Poster
'''

import requests
import pprint



class Omdb_Movie:

    def __init__(self):
        pass

    def search(self,name):

        url = "http://www.omdbapi.com/?s="
        url += name
        url += "&r=json"

        omdb_API = requests.get(url)


        video = omdb_API.json()

        video_result = video['Search']

        movie_result = []

        for item in video_result:

            if item['Poster'] != 'N/A':

                title = item['Title']
                image_url = item['Poster']
                movie_result.append({'Title': title, 'Image': image_url})


        return movie_result

if __name__ == "__main__":
    test = input("Type a value: ")
    client = Omdb_Movie()
    client_result = client.search(test)
    pprint.pprint(client_result)