##
 # Simple python gfycat.com url uploader
 #
 # @author      Nimrod Goldrat
 # @website     http://nimrod.goldrat.info
 # @copyright   Nimrod Goldrat 2014
 #
##

from collections import namedtuple

class gfycat(object):
    """This is a very simple module that allows you to
    1. upload a gif to gfycat
    2. query the upload url
    3. query an existing gfycat link
    4. query if a link is already exist
    """
    def __init__(self,param, url="upload.gfycat.com", debug=False):
        import random,string
        super(gfycat, self).__init__()
        randomString = ''.join(random.choice
            (string.ascii_uppercase + string.digits) for _ in range(5))
        self.res = self.__fetch(
            url, "/transcode/%s?fetchUrl=%s" % (randomString,param))

    def __writeDebug(self, what):
        console.log("")
    def __fetch(self,url, param):
        import httplib, json
        conn = httplib.HTTPConnection(url)
        conn.request("GET", param)
        req = conn.getresponse()
        res = req.read()
        conn.close()
        ret = namedtuple("res", "raw json")
        return ret(raw=res, json=json.loads(res))

    def getRaw(self):
        return self.res.raw

    def getJson(self):
        return self.res.json

    def webmUrl(self):
        return self.res.json["webmUrl"]

    def gfyName(self):
        return self.res.json["gfyname"]

    def mp4Url(self):
        return self.res.json["mp4Url"]

    def frameRate(self):
        return self.res.json["frameRate"]

    def gifWidth(self):
        return self.res.json["gifWidth"]

    def gifSize(self):
        return self.res.json["gifSize"]

    def gfysize(self):
        return self.res.json["gfysize"]

    def gifUrl(self):
        return self.res.json["gifUrl"]

    # gfycat lets you choose between those two options, so do I :)
    gfyname = gfyName
