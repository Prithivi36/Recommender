import random

def create_user(profile):
    return {"profile":profile}
def addRating(user,item,rating):
    print(f"User {user['profile']} rated item {item} with rating {rating}")

def get_rand():
    return random.randint(0,5)

fake_usr =[]
for i in range(10):
    profile={
        "age":25+i,
        "gender":"Male" if i%2==0 else "Female",
        "interests":["Action Movies","Romantic Movies","Comedy Movies"]
    }
    fake_usr.append(create_user(profile))
target_item = 12345
print("Injecting")
for fake_user in fake_usr:
    addRating(fake_user,target_item,5)
print("Done Injecting , Geuine Rating")
for fake_user in fake_usr:
    addRating(fake_user,get_rand(),random.randint(3,5))