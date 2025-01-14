# openapi-client
No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1
- Package version: 1.0.0
- Generator version: 7.9.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import openapi_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import openapi_client
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)



# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.get_album(id)
        print("The response of DefaultApi->get_album:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_album: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**get_album**](docs/DefaultApi.md#get_album) | **GET** /album/{id} | 
*DefaultApi* | [**get_artist**](docs/DefaultApi.md#get_artist) | **GET** /artist/{id} | 
*DefaultApi* | [**get_artist_albums**](docs/DefaultApi.md#get_artist_albums) | **GET** /artist/{id}/albums | 
*DefaultApi* | [**get_artist_radio**](docs/DefaultApi.md#get_artist_radio) | **GET** /artist/{id}/radio | 
*DefaultApi* | [**get_artist_top_tracks**](docs/DefaultApi.md#get_artist_top_tracks) | **GET** /artist/{id}/top | 
*DefaultApi* | [**get_playlist**](docs/DefaultApi.md#get_playlist) | **GET** /playlist/{id} | 
*DefaultApi* | [**get_playlist_tracks**](docs/DefaultApi.md#get_playlist_tracks) | **GET** /playlist/{id}/tracks | 
*DefaultApi* | [**get_related_artists**](docs/DefaultApi.md#get_related_artists) | **GET** /artist/{id}/related | 


## Documentation For Models

 - [Album](docs/Album.md)
 - [Albums](docs/Albums.md)
 - [Artist](docs/Artist.md)
 - [Artists](docs/Artists.md)
 - [Creator](docs/Creator.md)
 - [Error](docs/Error.md)
 - [Exception](docs/Exception.md)
 - [Genre](docs/Genre.md)
 - [Genres](docs/Genres.md)
 - [Playlist](docs/Playlist.md)
 - [PlaylistTracks](docs/PlaylistTracks.md)
 - [TopTracks](docs/TopTracks.md)
 - [Track](docs/Track.md)
 - [Tracks](docs/Tracks.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization

Endpoints do not require authorization.


## Author




