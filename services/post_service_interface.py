import abc

class PostServiceInterface(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def addPost(self, id, title, content, userId):
        pass