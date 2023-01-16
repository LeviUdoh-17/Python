class User:
    def __init__(self, user_id, username):
        # An attribute is what the object has, while an object is what an object can do
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User("001", "Angela")
user_2 = User("002", "Jack")
print(user_1.id, user_1.username)