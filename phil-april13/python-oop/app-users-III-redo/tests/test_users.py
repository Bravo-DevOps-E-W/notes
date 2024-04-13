import os 
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))

parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))

#Add parent directory to beginning of sys.path list
sys.path.insert(0, parent_dir)


from users.FreeUser import Free_User
from users.PremiumUser import Premium_User
import unittest


class TestUsers(unittest.TestCase):
    
    def setUp(self):
        self.bobby = Free_User("Bobby Hill", "bobbysellspropane@gmail.com", "123 Propane Lane", "T2-555-212-1337")
        self.wendy = Premium_User("Wendy Testaburger", "wendylovesstan@hotmal.com", "717 Main St", "C2-355-444-2516")
    
    def test_bobby_single_post(self):
        bobby = self.bobby
        
        single_post = bobby.add_post("Looks like a post to me")
        self.assertEqual(len(single_post), 1)
        
    def test_bobby_two_posts(self):
        bobby = self.bobby
        
        posts = bobby.add_post("Looks like a post to me")
        posts = bobby.add_post("Bobby is on fire with the posts")
        self.assertEqual(len(posts), 2)
    
    def test_premium_promotion(self):
        bobby = self.bobby
        posts = bobby.add_post("Looks like a post to me")
        posts = bobby.add_post("Bobby is on fire with the posts")
        errorMsg = bobby.add_post("Looks like a post to me")
        
        validationMsg = "You have reached your post limit. Buy Premium for only 99.99 a month for your first 30 days"
        
        
        self.assertEqual(len(bobby.get_user_posts), 2)
        self.assertEqual(errorMsg, validationMsg)
    
    def test_wendy_multiple_posts(self):
        """
        Checks that post increases in length for each post being made by a user
        """
        wendy = self.wendy
        posts = wendy.add_post("Wonder Woman Wendy")
        self.assertEqual(len(posts), 1)
        posts = wendy.add_post("Nothing special here")
        self.assertEqual(len(posts), 2)
        posts = wendy.add_post("Wow for only 99.99 I can't believe it")
        self.assertEqual(len(posts), 3)
        posts = wendy.add_post("Bobby should have listened")
        self.assertEqual(len(posts), 4)
    
    def test_all_posts(self):
        bobby = self.bobby
        wendy = self.wendy
        
        # Create 3 posts from bobby, only the first two should be valid
        bobby_posts = bobby.add_post("First one from bobby")
        
        bobby_posts = bobby.add_post("Last valid one from bobby")
        
        bobby_posts = bobby.add_post("This would of worked if Bobby just bought Premium")
        
        # Making 4 posts frrom Wendy
        wendy_posts = wendy.add_post("Showing off the power")
        wendy_posts = wendy.add_post("Wendy is on fire")
        wendy_posts = wendy.add_post("she makes posts multiple times a day")
        wendy_posts = wendy.add_post("Carrying Stan on her back")
        
        ## Expect that All posts contains 6 valid posts
        self.assertEqual(len(bobby.all_posts), 6)
        ## Expect that Wendy has 4 posts
        self.assertEqual(len(wendy.get_user_posts), 4)
        ## Expect that bobby has 2 posts
        self.assertEqual(len(bobby.get_user_posts), 2)
        
    def test_delete_post(self):
        bobby = self.bobby
        
        posts = bobby.add_post("Bobby Hill")
        posts = bobby.add_post("Didn't mean to type that")
        bobby.delete_post("Bobby Hill")
        self.assertEqual(len(bobby.get_user_posts), 1)
        posts = bobby.add_post("I am figuring it out now")
        self.assertEqual(len(posts), 2)
        bobby.delete_post("I am figuring it out now")
        bobby.delete_post("Didn't mean to type that")
        self.assertEqual(len(bobby.get_user_posts), 0)
        
    def test_delete_invalid(self):
        wendy = self.wendy
        
        wendy_post = wendy.add_post("Do not delete please")
        
        wendy.delete_post("Do not delete please.")
        
        self.assertEqual(len(wendy.get_user_posts), 1)
        
        wendy_post = wendy.add_post("It is important to spell things write")
        
        wendy.delete_post("It is important to spell things right")
        
        self.assertEqual(len(wendy.get_user_posts), 2)
        
        
    
        
     

if __name__ == '__main__':
    unittest.main()


