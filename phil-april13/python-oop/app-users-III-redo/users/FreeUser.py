from .User import User

class Free_User(User):
    def __init__(self, name, email, address, license):
        super().__init__(name, email, address, license)
        
    def add_post(self, post):
        if len(self.posts) >= 2:
            # print("You have reached your post limit. Buy Premium for only 99.99 a month for your first 30 days")
            return "You have reached your post limit. Buy Premium for only 99.99 a month for your first 30 days"
        self.posts.append(post)
        User.all_posts.append(post)
        return self.posts
        
        
        