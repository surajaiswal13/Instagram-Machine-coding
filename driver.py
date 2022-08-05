import sys
sys.path.append("D:\dunzo")

from controllers.user_controller import UserController
from controllers.post_controller import PostController

from services.user_service import UserService
from services.post_service import PostService

# creating controllers
userController = UserController(UserService())
postController = PostController(PostService())

# Creating Users
user1 = userController.addUser('user1', 'suraj')
user2 = userController.addUser('user2', 'sushant')

post1 = postController.addPost('post1', 'AmazingPost', 'cnaiodcndicsidncisdnci', 'user1')

print(post1)