# LMU Cast Statistics Generator

## Requirements & Installation
...

## Usage
...


# api.py

## getPlaylists( )
_Returns all playlists of user logged in._

**Request**
```shell
GET https://cast.itunes.uni-muenchen.de/api/v1/playlists
```

**Response**
```json
{
  "status": <http_status_code>,
  "content": {
      0: {
          'id': <playlist_id>,
          'name': <playlist_name>
      }
  }
}
```
```JSON
{
 "name": 12,
 "bornOn": "1957-01-05",
 "bornIn": "http://www.scotland.org#"
}
```



## getPlaylistAttributes( `playlist_id` )
_Returns all playlists of user logged in._

**Arguments**
- `playlist_id` LMU-Cast playlist_id

**Request**
```http
GET https://cast.itunes.uni-muenchen.de/api/v1/playlists
```

**Response**
```yaml
{
  'status': <http_status_code>,
  'content': {
      0: {
          'id': <playlist_id>,
          'name': <playlist_name>
      }
  }
}
```
