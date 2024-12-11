# openapi_client.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_album**](DefaultApi.md#get_album) | **GET** /album/{id} | 
[**get_artist**](DefaultApi.md#get_artist) | **GET** /artist/{id} | 
[**get_artist_albums**](DefaultApi.md#get_artist_albums) | **GET** /artist/{id}/albums | 
[**get_artist_radio**](DefaultApi.md#get_artist_radio) | **GET** /artist/{id}/radio | 
[**get_artist_top_tracks**](DefaultApi.md#get_artist_top_tracks) | **GET** /artist/{id}/top | 
[**get_playlist**](DefaultApi.md#get_playlist) | **GET** /playlist/{id} | 
[**get_playlist_tracks**](DefaultApi.md#get_playlist_tracks) | **GET** /playlist/{id}/tracks | 
[**get_related_artists**](DefaultApi.md#get_related_artists) | **GET** /artist/{id}/related | 


# **get_album**
> Album get_album(id)





### Example


```python
import openapi_client
from openapi_client.models.album import Album
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
    except Exception as e:
        print("Exception when calling DefaultApi->get_album: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**Album**](Album.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_artist**
> List[Artist] get_artist(id)





### Example


```python
import openapi_client
from openapi_client.models.artist import Artist
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
        api_response = api_instance.get_artist(id)
        print("The response of DefaultApi->get_artist:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_artist: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**List[Artist]**](Artist.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_artist_albums**
> Albums get_artist_albums(id)





### Example


```python
import openapi_client
from openapi_client.models.albums import Albums
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
        api_response = api_instance.get_artist_albums(id)
        print("The response of DefaultApi->get_artist_albums:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_artist_albums: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**Albums**](Albums.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_artist_radio**
> Tracks get_artist_radio(id)





### Example


```python
import openapi_client
from openapi_client.models.tracks import Tracks
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
        api_response = api_instance.get_artist_radio(id)
        print("The response of DefaultApi->get_artist_radio:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_artist_radio: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**Tracks**](Tracks.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_artist_top_tracks**
> TopTracks get_artist_top_tracks(id)





### Example


```python
import openapi_client
from openapi_client.models.top_tracks import TopTracks
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
        api_response = api_instance.get_artist_top_tracks(id)
        print("The response of DefaultApi->get_artist_top_tracks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_artist_top_tracks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**TopTracks**](TopTracks.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_playlist**
> Playlist get_playlist(id)





### Example


```python
import openapi_client
from openapi_client.models.playlist import Playlist
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
        api_response = api_instance.get_playlist(id)
        print("The response of DefaultApi->get_playlist:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_playlist: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**Playlist**](Playlist.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_playlist_tracks**
> PlaylistTracks get_playlist_tracks(id, index=index)





### Example


```python
import openapi_client
from openapi_client.models.playlist_tracks import PlaylistTracks
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
    index = 56 # int |  (optional)

    try:
        api_response = api_instance.get_playlist_tracks(id, index=index)
        print("The response of DefaultApi->get_playlist_tracks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_playlist_tracks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **index** | **int**|  | [optional] 

### Return type

[**PlaylistTracks**](PlaylistTracks.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_related_artists**
> Artists get_related_artists(id)





### Example


```python
import openapi_client
from openapi_client.models.artists import Artists
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
        api_response = api_instance.get_related_artists(id)
        print("The response of DefaultApi->get_related_artists:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_related_artists: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**Artists**](Artists.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

