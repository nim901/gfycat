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
    def __init__(self, debug=False):
        super(gfycat, self).__init__()
        self.debug = debug

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

    def upload(self, param):
        import random,string
        randomString = ''.join(random.choice
            (string.ascii_uppercase + string.digits) for _ in range(5))
        url="upload.gfycat.com"
        res = self.__fetch(url,
            "/transcode/%s?fetchUrl=%s" % (randomString, param))
        if "error" in res.json:
            raise ValueError("%s" % res.json["error"])
        return gfycatUpload(res, self.debug)

    def more(self, param):
        url="gfycat.com"
        res = self.__fetch(url, "/cajax/get/%s" % param)
        if "error" in res.json["gfyItem"]:
             raise ValueError("%s" % self.json["gfyItem"]["error"])
        return gfycatMore(res, self.debug)

    def check(self, param):
        url="gfycat.com"
        res = self.__fetch(url, "/cajax/checkUrl/%s" % param)
        if "error" in res.json:
             raise ValueError("%s" % self.json["error"])
        return gfycatCheck(res, self.debug)

class gfycatUtils(object):
    """
    W.I.P
    """
    def __init__(self, param, json, debug=False):
        super(gfycatUtils, self).__init__()
        self.debug = debug
        self.res = param
        self.js = json

    def raw(self):
        return self.res.raw

    def json(self):
        return self.js

    def get(self, what):
        if not what in self.js:
            return "Sorry, couldn't find that."
        return self.js[what]

    def formated(self, empty=False):
        raise NotImplementedError


class gfycatUpload(gfycatUtils):
    """
    W.I.P
    """
    def __init__(self, param, debug=False):
        super(gfycatUpload, self).__init__(param, param.json, debug)
        self.debug = debug
        self.res = param
        self.js = param.json

class gfycatMore(gfycatUtils):
    """
    W.I.P
    """
    def __init__(self, param, debug=False):
        super(gfycatMore, self).__init__(param, param.json["gfyItem"], debug)
        self.debug = debug
        self.res = param
        self.js = param.json["gfyItem"]

    def redditLink(self):
        raise NotImplementedError

class gfycatCheck(gfycatUtils):
    """
    W.I.P
    """
    def __init__(self, param, debug=False):
        super(gfycatCheck, self).__init__(param, param.json)
        self.debug = debug
        self.res = param
        self.js = param.json
