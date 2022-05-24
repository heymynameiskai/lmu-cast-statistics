# import requests
import api
import pprint
pp = pprint.PrettyPrinter(indent=4)



# def pretty(dict):
#     for i in range(len(dict)):
#         print(dict[i]['name'])
#
#
# pretty(api.getPlaylists()['content'])
# print(api.getPlaylists()['content'])
#
# # pp.pprint(api.getStatisticsByPlaylist('KOQc5Np5UQ'))
# s = api.getStatisticsByPlaylist('rP0Z8pqxN8')['content']
# # s_sorted = sorted(s, key=lambda x: s[x]['id'])
# # pp.pprint(s_sorted)
# # pp.pprint(sorted(s, reverse=True))
# for i in sorted(s.keys(), reverse=True):
#     print(s[i]);




def tablePrintHits(playlist_id):
    # 1st: get basic attributes of playlist, like name
    playlist_attributes_status = api.getPlaylistAttributes(playlist_id)['status']
    playlist_attributes = api.getPlaylistAttributes(playlist_id)['content']

    # check if API call worked
    if playlist_attributes_status == 200:
        playlist_name = playlist_attributes['name']
        playlist_url = "https://cast.itunes.uni-muenchen.de/vod/playlists/"+playlist_id+".html"
        print("\n")
        print(playlist_name)
        print(playlist_url)
        print("\n")
    else:
        print("Error while fetching API. Calling api.getPlaylistAttributes("+playlist_id+") returned HTTP-Status-Code: "+playlist_attributes_status)


    # 2nd: get number of hits for each video in playlist
    playlist_hits_status = api.getStatisticsByPlaylist(playlist_id)['status']
    playlist_hits = api.getStatisticsByPlaylist(playlist_id)['content']

    # check if API call worked
    if playlist_hits_status == 200:
        print("Video \t\t\t\t\t\t| Online \t| High Quality Video \t| Audio")

        # print hits for each video
        for i in sorted(playlist_hits.keys(), reverse=True):
            print(playlist_hits[i]['name']+"\t\t"+str(playlist_hits[i]['hits_online'])+"\t\t"+str(playlist_hits[i]['hits_video'])+"\t\t\t"+str(playlist_hits[i]['hits_audio']));

        print("\n")
    else:
        print("Error while fetching API. Calling api.getStatisticsByPlaylist("+playlist_id+") returned HTTP-Status-Code: "+playlist_attributes_status)





def printAllStatistics():
    playlists = api.getPlaylists()['content']

    for i in playlists:
        tablePrintHits(playlists[i]['id'])


# tablePrintHits("rP0Z8pqxN8")
printAllStatistics()
