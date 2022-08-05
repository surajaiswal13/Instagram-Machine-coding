from services.post_service_interface import PostServiceInterface
from models.posts import Post

class PostService(PostServiceInterface):

    postDetails = {}
    def addPost(self, id, title, content, userId):
        post = Post()
        post.setId(id)
        post.setTitle(title)
        post.setContent(content)
        post.setUserId(userId)

        self.__class__.postDetails[id] = post

        return post