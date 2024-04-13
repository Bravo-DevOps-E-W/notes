class User:
    all_posts = []
    
    def __init__(self, name, email, address, license):
        self.name = name
        self.email = email
        self.address = address
        self.license = license
        self.posts = []
        
        
    def add_post(self, post):
        self.posts.append(post)
        User.all_posts.append(post)
        return self.posts
    
    def delete_post(self, post):
        if post in User.all_posts:
            User.all_posts.remove(post)
        if post in self.posts:
            self.posts.remove(post)
    
    @property
    def get_user_posts(self):
        return self.posts
    
    
    
# user1 = User("Bobby Hill", 'Bobbysellspropane@gmail.com', '123 Propane Lane', 'T12-555-1337')

# print(user1.get_user_posts)
# user1.add_post("King Bobby, to you")
# user1.add_post("BOBBY RUNNNNN")
# print(user1.get_user_posts)
