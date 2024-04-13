from users.User import User
from users.FreeUser import Free_User
from users.PremiumUser import Premium_User


user1 = Free_User('Bobby Hill', 'bobbysellspropane@gmail.com', '123 Propane Lane', 'T2-555-1337')
user2 = Premium_User('Wendy Testaburger', 'wendylovesstan@hotmail.com', '777 Main St', 'C1-555-444-2145')

print(User.all_posts)

user1.create_post("Bobby One")
print(user1.get_user_posts())

user2.create_post("Cool Wendy")
print(user2.get_user_posts())

# Check all posts
print(User.all_posts)

user2.create_post("Wow cool app")
user2.create_post("Love the features")
user2.create_post("Premium was so worth it")
user2.create_post("only 99.99 per month?")
user2.create_post("Don't listen to Bobbby")

print(user2.get_user_posts())

user1.create_post("Wendy how does this work?")
print(user1.create_post("What happened"))
print(user1.create_post("What do I do"))
print(user1.create_post("What do I don't like this app"))

print(User.all_posts)


