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
    def __init__(self, param, debug=False):
        import random,string
        super(gfycat, self).__init__()
        self.debug = debug
        url="upload.gfycat.com"
        randomString = ''.join(random.choice
            (string.ascii_uppercase + string.digits) for _ in range(5))
        self.res = self.__fetch(url,
            "/transcode/%s?fetchUrl=%s" % (randomString,param))
        if "error" in self.res.json:
            raise ValueError("%s" % self.res.json["error"])

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

    def raw(self):
        return self.res.raw

    def json(self):
        return self.res.json

    def get(self,what):
        if not what in self.res.json:
            return "Sorry, couldn't find that."
        return self.res.json[what]
