# LMU Cast Statistics Generator

## Requirements & Installation


## Usage



# Documentation
## api.py

### getPlaylists( )
_Returns all playlists of user logged in._

**Request**
```http
GET <api_root>/playlists
```

**Response**
```python
return
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



### getPlaylistAttributes( `playlist_id` )
_Returns all playlists of user logged in._

**Arguments**
- `playlist_id` LMU-Cast playlist_id

**Request**
```http
GET <api_root>/playlists
```

**Response**
```python
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
