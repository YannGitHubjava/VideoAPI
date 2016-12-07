import requests
import vimeo
from videoApp.keys import keys as k
import pprint
import re


class vimeo_Movie:
    def __init__(self):

        self.v = vimeo.VimeoClient(
            token= k.vimeo_access_token ,
            key= k.vimeo_client_identifier,
            secret= k.vimeo_client_secret
            )


    def search(self, name):

        url = "https://api.vimeo.com/videos?query="
        url += name

        vimeo_API = self.v.get(url)


        video = vimeo_API.json()

        video_data = video['data']

        video_list = []

        count = 3
        for item in video_data:

            if count >= 0 :

                vimeo_link = item['link']
                vimeo_name = item['name']
                vimeo_image = item['pictures']['sizes'][0]['link']


                video_result = {'name': vimeo_name,
                                'link': vimeo_link,
                                'image': vimeo_image
                                }

                video_list.append(video_result)

                count -= 1

            else:
                break


        #return video_list

        return \
            {
                'Vimeo': video_list

            }
#TODO unittesting

if __name__=="__main__":
    query = input("Enter value:")
    video = vimeo_Movie()
    result = video.search(query)
    pprint.pprint(result, indent=4)

