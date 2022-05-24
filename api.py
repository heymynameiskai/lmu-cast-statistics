import requests
import keys


api_root = "https://cast.itunes.uni-muenchen.de/api/v1"
auth_cookie = keys.auth_cookie

headers = {
  'Cookie': auth_cookie,
  'Content-Type': 'application/json',
  'Accept-Language': 'de-DE,de;q=0.9'
}

simulate_API_Call = False




def getPlaylists():
    if simulate_API_Call:
        return {
            'status': 200,
            'content': ''
        }
    else:
        r = requests.get(api_root+"/playlists", headers=headers)
        status = r.status_code

        if status == 200:
            # parse response content as json
            r_json = r.json()
            content = {}

            for i in range(len(r_json)):
                content[i] = {
                    'id': r_json[i]['id'],
                    'name': r_json[i]['name']
                }

            return {
                'status': r.status_code,
                'content': content
            }
        else:
            return {'status':r.status_code, 'content': None}

def getPlaylistAttributes(playlist_id):
    r = requests.get(api_root+"/playlists/"+playlist_id, headers=headers)
    status = r.status_code

    if status == 200:
        # parse response content as json
        content = r.json()
        return {
            'status': r.status_code,
            'content': content
        }
    else:
        return {'status':r.status_code, 'content': None}


def getStatisticsByPlaylist(id):
    if simulate_API_Call:
        return {
            'status': 200,
            'content': ''
        }
    else:
        r = requests.get(api_root+"/playlist_statistics/"+id, headers=headers)
        status = r.status_code

        if status == 200:
            # parse response content as json
            r_json = r.json()
            content = {}

            # for each video in playlist
            for i in range(len(r_json)):
                # check which formats are supported by video
                hits_audio = 0
                hits_video = 0
                hits_online = 0
                number_of_formats = len(r_json[i]['total_hits_by_format'])

                # how many formats? --> for each format check type of hit-counter
                for j in range(number_of_formats):
                    # which format is no. j?
                    if r_json[i]['total_hits_by_format'][j]['format'] == "online":
                        hits_online = r_json[i]['total_hits_by_format'][j]['total_hits']
                    elif r_json[i]['total_hits_by_format'][j]['format'] == "audio_only":
                        hits_audio = r_json[i]['total_hits_by_format'][j]['total_hits']
                    elif r_json[i]['total_hits_by_format'][j]['format'] == "high_quality":
                        hits_video = r_json[i]['total_hits_by_format'][j]['total_hits']


                content[i] = {
                    'id': r_json[i]['clip']['id'],
                    'name': r_json[i]['clip']['title'],
                    'hits_online': hits_online,
                    'hits_audio': hits_audio,
                    'hits_video': hits_video
                }

            return {
                'status': r.status_code,
                'content': content
            }
        else:
            return {'status':r.status_code, 'content': None}







# print(getStatisticsByPlaylist("EsflD5TvTE"))
