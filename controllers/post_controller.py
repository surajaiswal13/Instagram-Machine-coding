class PostController(object):

    def __init__(self, postService):
        self.postService = postService

    def addPost(self, id, title, content, userId):
        return self.postService.addPost(id, title, content, userId)
