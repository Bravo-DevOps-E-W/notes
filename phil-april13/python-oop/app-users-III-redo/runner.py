from users.FreeUser import Free_User
from users.PremiumUser import Premium_User

user1 = Free_User('Bobby Hill', 'bobbysellspropane@gmail.com', '123 Propane Lane', 'T12-555-1337')
user2 = Premium_User('Wendy Testaburger', 'wendylovesstan@hotmail.com', '777 Main St', 'C1-555-444-2315')

print(user1.all_posts)

print(user1.add_post('Bobby One'))
print(user2.add_post('hey there from wendy'))
print(user1.all_posts)
print(user2.add_post('Wendy is cool'))
print(user2.add_post('Premium lifestyle'))
print(user2.add_post('How great'))

print(user1.add_post('How does this work?'))
print(user1.add_post('Whats going on?'))
print(user1.add_post('I do not want to pay'))

print(user1.add_post('well im done with this app'))
print(user2.add_post('Bobby doesnt know what hes talking about'))
print(user2.add_post('Charcoal is better anyways'))

print("All of Bobbtys posts as a fremium user:")
print(user1.get_user_posts)

print("All of wendys posts as a premium user:")
print(user2.get_user_posts)

print("And all posts look like:")
print(user1.all_posts)

print("With poor Bobby only getting to make 2 posts as a Free_User")



