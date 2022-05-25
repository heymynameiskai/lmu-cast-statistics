# Documentation of api.py
#### constants
- `AUTH_COOKIE` Authentification Cookie for LMU Cast, importet from keys.py
- `API_ROOT`
- `HEADERS` all api calls are sending this default headers, including the `auth_cookie`
- `PLAYLIST_ROOT` root of public playlist URLs
&nbsp;
&nbsp;
&nbsp;


## `apicall( endpoint )`
#### Arguments
`endpoint` Endpoint of API that is to be called, e.g. `"/playlists"`

#### Process
Method tries to call API and checks HTTP-Status-Code of response

#### Return
- If HTTP-Status-Code is 200, method returns content of response
- If HTTP-Status-Code is not 200, method prints out error message and quits
&nbsp;
&nbsp;
&nbsp;



## `clean_playlist_item( playlist_item )`
#### Arguments
`playlist_item` JSON-object as returned by LMU-Cast-API, for example when calling `/playlists/<playlist_id>`. Note: this function takes a **single** item only, not a list of playlist-items like returned by `/playlists`.

#### Process
- Method removes all unnecessary values from playlist item.
- Method adds public url of playlist to item

#### Return
```yaml
{
  'id': '', # LMU-Cast id of playlist
  'name': '', # public name of playlist
  'iTunes_author': '', 
  'iTunes_owner_name': '', 
  'export_format_ids': ['online', 'audio_only', 'high_quality'], # MAYBE supported playlist formats ?
  'allowed_format_ids': ['online', 'audio_only', 'high_quality'], # MAYBE formats published ?
  'updated_at': '', 
  'created_at': '', 
  'clips_count': '', # number of videos in playlist 
  'url': '' # public url to playlist
}
```
&nbsp;
&nbsp;
&nbsp;



## get_total_hits_online( `total_hits_by_format` )
#### Arguments
`total_hits_by_format` excerpt of json as returned by API_endpoint `/playlist_statistics/<playlist_id`
```yaml
# API is returning this
{
  'clip': {
    'title': <title_of_video>,
    'id': 0
  },
  'total_hits_by_format': [ # we need this element for method
    {
      'format': 'online',
      'total_hits': 215
    },
    {
      'format': 'audio_only',
      'total_hits': 12
    },
    {
      'format': 'high_quality',
      'total_hits': 102
    }
  ],
  'daily_hits_by_format': [
    {
      'format': 'online',
      'daily_hits': { ... }
    }
  ]
}
```

#### Process & Return
Method finds number of hits for requested format, e.g. online, and returns integer.
&nbsp;
&nbsp;
&nbsp;





## get_all_playlist( )
***AB HIER ÜBERARBEITEN*** 

_Returns all playlists of user logged in._

**Request**
```http
GET "https://cast.itunes.uni-muenchen.de/api/v1/playlists"
```

**Response**
```yaml
{
  'status': <http_status_code>,
  'content': {
      0: { # = playlist of user
          'id': <playlist_id>,
          'name': <playlist_name>
      },
      ...
  }
}
```
&nbsp;
&nbsp;
&nbsp;



## getPlaylistAttributes( `playlist_id` )
_Gets metadata of playlist by playlist id._

**Arguments**
- `playlist_id` LMU-Cast playlist_id

**Request**
```http
GET "https://cast.itunes.uni-muenchen.de/api/v1/playlists/<playlist_id>"
```

**Response**
```yaml
{
  'status': <http_status_code>,
  'content': {
      'id': <playlist_id>,
      'name': <playlist_name>,
      ... (many more) # uncleaned response of LMU Cast
  }
}
```
&nbsp;
&nbsp;
&nbsp;




## getStatisticsByPlaylist( `playlist_id` )
_Returns number of hits by format for each video in playlist._

**Arguments**
- `playlist_id` LMU-Cast playlist_id

**Request**
```http
GET "https://cast.itunes.uni-muenchen.de/api/v1/playlist_statistics/<playlist_id>"
```

**Response**
```yaml
{
  'status': <http_status_code>,
  'content': {
      0: { # = video in playlist
          'id': <video_id>,
          'name': <video_name>,
          'hits_online': Int,
          'hits_video': Int,
          'hits_audio': Int
      },
      ...
  }
}
```
&nbsp;
&nbsp;
&nbsp;
