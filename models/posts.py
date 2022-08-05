class Post(object):

    def __init__(self):
        self.id = None
        self.title = None
        self.content = None
        self.userId = None

    def setId(self, id):
        self.id = id

    def getId(self):
        return self.id

    def setTitle(self, title):
        self.title = title

    def getTitle(self):
        return self.title

    def setContent(self, content):
        self.content = content

    def getContent(self):
        return self.content

    def setUserId(self, userId):
        self.userId = userId

    def getUserId(self):
        return self.userId