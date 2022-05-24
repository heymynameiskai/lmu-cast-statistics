# LMU Cast Statistics Generator

## Requirements & Installation
...

## Usage
...


# api.py
All API-Calls are sending this header:
```yaml
{
  'Cookie': <auth_cookie>,
  'Content-Type': 'application/json',
  'Accept-Language': 'de-DE,de;q=0.9'
}
```
Make shure you have added your `auth_cookie` to `keys.py`.
&nbsp;
&nbsp;
&nbsp;



## getPlaylists( )
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
GET 'https://cast.itunes.uni-muenchen.de/api/v1/playlists/<playlist_id>'
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




## getStatisticsByPlaylist( `playlist_id` )
_Returns number of hits by format for each video in playlist._

**Arguments**
- `playlist_id` LMU-Cast playlist_id

**Request**
```http
GET 'https://cast.itunes.uni-muenchen.de/api/v1/playlist_statistics/<playlist_id>'
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
