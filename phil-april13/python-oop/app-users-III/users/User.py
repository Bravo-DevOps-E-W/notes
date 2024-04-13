## User will be our Base Class, that FreeUser and PremiumUser will inherit from

### This will grant FreeUser and PremiumUser access to all of the User class attributes and methods

### In FreeUser and PremiumUser, we will demonstrate how we are able to override methods we inherit from User



class User:
    #Creating a class variable to track all_posts
    all_posts = []
    def __init__(self, name, email, address, license, is_premium=False):
        self.name = name
        self.email = email
        self.address = address
        self.license = license
        self.posts = []
        self.is_premium = is_premium
        
    def create_post(self, post):
        if not self.is_premium and len(self.posts) >= 2:
            print("You have reached your post limit. Buy premium to create more posts")
            return ""
        self.posts.append(post)
        User.all_posts.append(post)
        
    def delete_post(self, post):
        if post in User.all_posts:
            User.all_posts.remove(post)
        if post in self.posts:
            self.posts.remove(post)
            
    def get_user_posts(self):
        return self.posts
    
    def get_all_posts(self):
        return User.all_posts
    
    

    
# user1 = User('Bobby Hill', 'bobbysellspropane@gmail.com', '123 Propane Lane', 'T12-555-1337')
# user2 = User('Wendy Testaburger', 'wendylovesstan@hotmail.com', '777 Main St', 'C1-555-444-2145', True)

# print(user1.name)
# print(user1.posts)
# user1.create_post("Hooray Bobby")
# print(user1.get_user_posts())
# user2.create_post("Wendys Is living the good life")
# user2.create_post("Wendys Is bored")
# user2.create_post("Wendys Is hungry")
# user2.create_post("Wendys Is tired")
# user2.create_post("Wendys Is excited")
# print(user1.get_all_posts())

# user1.create_post("So how does this work?")
# user1.create_post("Wait was that a post?")
# user1.create_post("So I need money now?")
# user1.create_post("Thats not fair")

# print("user1 posts:")
# print(user1.get_user_posts())
# print()
# print("user2 posts:")
# print(user2.get_user_posts())
# print()
# print("Getting all posts using user2")
# print(user2.get_all_posts())



