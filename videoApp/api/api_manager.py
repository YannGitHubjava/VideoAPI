from videoApp.api import omdbAPI, vimeoAPI
import pprint


class API_Manager:
    def __init__(self):
        self.clients = [
            omdbAPI.Omdb_Movie(),
            vimeoAPI.vimeo_Movie()]


    def search(self,query):
        '''
           :param query: takes string querry from the user
           :type  str : data type is string
           :return : dictionary of OMDB and VIMEO object
           :rtype: dict

           '''

        api_response_list = []

        for api_client in self.clients:
            search_result = api_client.search(query)
            api_response_list.append(search_result)


        return \
            { 'OMDB' : api_response_list[0],
              'VIMEO': api_response_list[1]

              }

#Start Debug

if __name__=="__main__":

    '''For testing purpose only'''

    test = input("Type value: ")
    clients = API_Manager()
    client_search_results = clients.search(test)
    pprint.pprint(client_search_results, indent=4)

#End debug