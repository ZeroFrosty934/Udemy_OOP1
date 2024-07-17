class User:   # class name
    active_users = 0       #class attributes

    @classmethod           #class method
    def display_active_users(cls):
            return f"There are currently {cls.active_users} active users"
    @classmethod
    def from_string(cls, data_str):
        first, last, age = data_str.split(",")
        return cls(first, last, int(age))


    def __init__(self, first, last, age):   #The __init__ method.
        self.first = first # Name attribute
        self.last = last
        self.age = age
        User.active_users += 1

    def __repr__(self):
        return f"{self.first} is {self.age}"

    # Instance methods.
    def logout(self):
        User.active_users -= 1
        return f"{self.first} has logout"

    def full_name(self):
        return f"{self.first} {self.last}"

    def initials(self):
        return f"{self.first[0]}.{self.last[0]}"

    def likes(self, thing):
        return f"{self.first} likes {thing}"

    def is_senior(self):
        return self.age >= 65

    def birthday(self):
        self.age += 1
        return f"Happy Birthday {self.age}th, {self.first}"

#user1 = User("Joe", "Many", 22)
#user2 = User("Blanca", "Grey", 66)
# print(user2.full_name())
# print(user1.likes("Ice cream")) #Ice cream = arguments
# print(user2.initials())
# print(user1.initials())
#
# print(user2.is_senior())
# print(user1.age)
# print(user1.birthday())
# print(user1.age)

# print(User.active_users)
# user1 = User("Joe", "Many", 22)
# user2 = User("Blanca", "Grey", 66)
# print(User.active_users)
# print(user2.logout())
# print(User.active_users)

# user1 = User("Joe", "Many", 22)
# user2 = User("Blanca", "Grey", 66)
# print(User.display_active_users())
# user1 = User("Joe", "Many", 22)
# user2 = User("Blanca", "Grey", 66)
# print(User.display_active_users())

# tom = User.from_string("Tom,Jones, 89")
# print(tom.full_name())
# print(tom.birthday())

j = User("Julia", "Sams", 25)
j = str(j)
print(j)






