gfycatuploader
==========

A very simple module that allows you to

    1. upload a gif to gfycat from a remote location
    2. upload a gif to gfycat from the local machine
    3. query the upload url
    4. query an existing gfycat link
    5. query if a link is already exist

## Usage:

### upload a file:
uploading a file from remote is very easy:

```python
upload = gfycat().upload("i.imgur.com/lKi99vn.gif")
```

or the longer version:

```python
upload = gfycat()
upload = upload.upload("i.imgur.com/lKi99vn.gif")
```

you can also upload a file from your local machine (for this you will have to use the requests module):

```python
upload = gfycat().uploadFile(r"C:\not\funny\sample.gif")
```

Then, you will be able to access the returning result via:

```Python
print upload.json()
print upload.raw()
print upload.formated()
print upload.get("someValue")
```

the result of the last 2 prints will be:

```python
print upload.formated()

    "webmUrl": "http://zippy.gfycat.com/SimilarEmbellishedBinturong.webm",
    "gfyname": "SimilarEmbellishedBinturong",
    "gfyName": "SimilarEmbellishedBinturong",
    "mp4Url": "http://zippy.gfycat.com/SimilarEmbellishedBinturong.mp4",
    "frameRate": 1,
    "gifWidth": 374,
    "gifSize": 378641,
    "gifUrl": "http://zippy.gfycat.com/SimilarEmbellishedBinturong.gif",
    "gfysize": 368876
    
print upload.get("webmUrl")

    http://zippy.gfycat.com/SimilarEmbellishedBinturong.webm
```

### query an existing gfycat link:
you can query an existing link in order to get more details:
```python
query = gfycat().more("gfycatName")
```

Then, you will be able to access the returning result via (the same as above):

```Python
print query.json()
print query.raw()
print query.formated()
print query.get("someValue")
```

the result of the last 2 prints will be:

```python
print query.formated()

    "frameRate": 25,
    "height": 252,
    "nsfw": "0",
    "sar": null,
    "webmUrl": "http://zippy.gfycat.com/SharpExcellentAbalone.webm",
    "redditId": "27ondd",
    "redditIdText": "flying_through_an_iceberg",
    "gifUrl": "http://giant.gfycat.com/SharpExcellentAbalone.gif",
    "userName": "anonymous",
    "gfyNumber": "394955002",
    "subreddit": "gfycats",
    "gfyName": "SharpExcellentAbalone",
    ...
    
print upload.get("redditIdText")

    flying_through_an_iceberg
```
### query if a link is already exist:
this will be used if you want to quickly see if a link is already known to gfycat:

```python
check = gfycat().check("i.imgur.com/lKi99vn.gif")
```

Then, you will be able to access the returning result via (same as above):

```Python
print check.json()
print check.raw()
print check.formated()
print check.get("someValue")
```

the result of the last 2 prints will be:

```python
print check.formated()

    "webmUrl": "http://zippy.gfycat.com/ScaryGrizzledComet.webm",
    "gfyName": "ScaryGrizzledComet",
    "mp4Url": "http://zippy.gfycat.com/ScaryGrizzledComet.mp4",
    "frameRate": 1,
    "gfyUrl": "http://gfycat.com/ScaryGrizzledComet",
    "urlKnown": true,
    "gifUrl": "http://zippy.gfycat.com/ScaryGrizzledComet.gif"
    
print check.get("urlKnown")

    True
```

### TODO:
- Finish formated() function
- Tests

Please note that although this module is working, there might still be some issues with it. if you find anything, please let me know! 
