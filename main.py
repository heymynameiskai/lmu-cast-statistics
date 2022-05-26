import api
import pdf
import plot

# import pprint
# pp = pprint.PrettyPrinter(indent=4)

def tablePrintHits(playlist_id):
    # 1st: get basic attributes of playlist, like name
    playlist_attributes_status = api.get_single_playlist(playlist_id)['status']
    playlist_attributes = api.get_single_playlist(playlist_id)['content']

    # check if API call worked
    if playlist_attributes_status == 200:
        playlist_name = playlist_attributes['name']
        playlist_url = "https://cast.itunes.uni-muenchen.de/vod/playlists/" + playlist_id + ".html"
        print("\n")
        print(playlist_name)
        print(playlist_url)
        print("\n")
    else:
        print(
            "Error while fetching API. Calling api.getPlaylistAttributes(" + playlist_id + ") returned HTTP-Status-Code: " + playlist_attributes_status)

    # 2nd: get number of hits for each video in playlist
    playlist_hits_status = api.get_playlist_total_hits(playlist_id)['status']
    playlist_hits = api.get_playlist_total_hits(playlist_id)['content']

    # check if API call worked
    if playlist_hits_status == 200:
        print("Video \t\t\t\t\t\t| Online \t| High Quality Video \t| Audio")

        # print hits for each video
        for i in sorted(playlist_hits.keys(), reverse=True):
            print(playlist_hits[i]['name'] + "\t\t" + str(playlist_hits[i]['hits_online']) + "\t\t" + str(
                playlist_hits[i]['hits_video']) + "\t\t\t" + str(playlist_hits[i]['hits_audio']))

        print("\n")
    else:
        print(
            "Error while fetching API. Calling api.getStatisticsByPlaylist(" + playlist_id + ") returned HTTP-Status-Code: " + playlist_attributes_status)
def printAllStatistics():
    playlists = api.get_all_playlists()['content']

    for i in playlists:
        tablePrintHits(playlists[i]['id'])





def printPDF(playlist_id):
    print("Trying to export " + playlist_id + "...")

    playlist_attributes = api.get_single_playlist(playlist_id)
    playlist_name = playlist_attributes['name']
    playlist_url = playlist_attributes['url']
    playlist_hits = api.get_playlist_total_hits(playlist_id)

    pdf.printStatistics(file_name=playlist_name, date='heute', playlist_title=playlist_name, playlist_url=playlist_url, hits=playlist_hits)


def printAllPDF():
    playlists = api.get_all_playlists()
    print("Going to export " + str(len(playlists)) + " PDFs...")

    for i in playlists:
        printPDF(i['id'])


# printAllPDF()
printPDF("JsSFM23oqr")

# plot.plot('hNYTXTtFGq', api.get_playlist_total_hits('hNYTXTtFGq'))