# import python modules
import requests

# import local modules
import keys

# =============================================
#                  CONSTANTS
# =============================================
AUTH_COOKIE = keys.auth_cookie
API_ROOT = "https://cast.itunes.uni-muenchen.de/api/v1"
HEADERS = {
    'Cookie': AUTH_COOKIE,
    'Content-Type': 'application/json',
    'Accept-Language': 'de-DE,de;q=0.9'
}
PLAYLIST_ROOT = "https://cast.itunes.uni-muenchen.de/vod/playlists/"


# =============================================
#               HELPER FUNCTIONS
# =============================================
# general call-function
def apicall(endpoint):
    try:
        response = requests.get(API_ROOT + endpoint, headers=HEADERS)
        status = response.status_code

        if status == 200:
            return response.json()
        else:  # HTTP Code not 200 --> quit program
            print("Oops! HTTP-Code: " + str(status))
            quit()
    except Exception as e:  # Call did not work --> quit program
        print("Oops! " + str(e))
        quit()


# strip all that unused LMU-Cast data
def clean_playlist_item(playlist_item):
    del playlist_item['playlist_id']
    del playlist_item['user_id']
    del playlist_item['protection']
    del playlist_item['spectators']
    del playlist_item['course_ids']
    del playlist_item['enable_watermark']
    del playlist_item['searchable']
    del playlist_item['custom_css']
    del playlist_item['deleted']
    del playlist_item['custom_poster_url']
    del playlist_item['header_url']
    del playlist_item['footer_url']
    del playlist_item['intro_url']
    del playlist_item['outro_url']
    del playlist_item['rss_quicktime_url']
    del playlist_item['embed_url']
    del playlist_item['iTunes_icon_name']
    del playlist_item['iTunes_icon_url']
    del playlist_item['iTunes_description']
    del playlist_item['iTunes_complete']
    del playlist_item['iTunes_keywords']
    del playlist_item['iTunes_category']
    del playlist_item['iTunes_language']
    del playlist_item['producers']
    del playlist_item['iTunes_email']
    del playlist_item['iTunes_explicit']
    del playlist_item['iTunes_publish_date']
    del playlist_item['iTunes_category_code']
    del playlist_item['required_faculties']
    del playlist_item['from_lmucast']
    del playlist_item['rss_feeds']
    del playlist_item['owner']

    playlist_item['name'] = clean_string(playlist_item['name'])
    playlist_item['url'] = PLAYLIST_ROOT + playlist_item['id'] + ".html"
    return playlist_item


def clean_string(string: str):
    # add chars that are crashing the export and need to be replaced (not the most elegant way... but german Umlaute need to stay!)
    string = string.replace('–', '-')
    string = string.replace('/', '-')
    string = string.replace('\\', '-')
    string = string.replace('\x84', '')
    string = string.replace(':', ' - ')
    string = string.replace('|', '-')
    string = string.replace('\t', '-')
    return string


# get number of hits for specific format form cluttered LMU-Cast statistics response
def get_total_hits_online(total_hits_by_format):
    for h in total_hits_by_format:
        if h['format'] == 'online':
            return h['total_hits']
    return 0


def get_total_hits_audio(total_hits_by_format):
    for h in total_hits_by_format:
        if h['format'] == 'audio_only':
            return h['total_hits']
    return 0


def get_total_hits_video(total_hits_by_format):
    for h in total_hits_by_format:
        if h['format'] == 'high_quality':
            return h['total_hits']
    return 0


# =============================================
#                   GETTERS
# =============================================
# get all playlists of current user
def get_all_playlists():
    playlists = apicall("/playlists")
    for p in playlists:
        p = clean_playlist_item(p)
    return playlists


# get playlist attributes by playlist id
def get_single_playlist(playlist_id):
    return clean_playlist_item(apicall("/playlists/" + playlist_id))


def get_playlist_total_hits(playlist_id):
    hits = {}
    videos = apicall("/playlist_statistics/" + playlist_id)
    for v in videos:
        hits[v['clip']['id']] = {
            'title': clean_string(v['clip']['title']),
            'hits_online': get_total_hits_online(v['total_hits_by_format']),
            'hits_video': get_total_hits_video(v['total_hits_by_format']),
            'hits_audio': get_total_hits_audio(v['total_hits_by_format'])
        }

    return hits


# print(apicall("/playlists/8gf2lxFd0Z"))
# print(get_single_playlist('8gf2lxFd0Z'))
