import json

# Load the followers and following lists from JSON text file to Python dictionaries
followers = open(r'''D:\Work\Programming\New folder\followers_and_following\followers.json''', "r")
following = open(r'''D:\Work\Programming\New folder\followers_and_following\following.json''', "r")
followers_loaded = json.load(followers)
following_loaded = json.load(following)
# The relationships_followers attribute contains a list of dictionaries
# where each dict has an attribute called string_list_data 
# string_list_data contains a list of one dictionary which has an attribute called value, which is the username
follower_temp_dicts = followers_loaded["relationships_followers"]
# The relationships_following attribute contains a list of dictionaries
# where each dict has an attribute called string_list_data 
# string_list_data contains a list of one dictionary which has an attribute called value, which is the username
following_temp_dicts = following_loaded["relationships_following"]

# Creating the list of followers, list of strings of usernames
list_followers = []
for i in follower_temp_dicts:
    for j in i["string_list_data"]:
        list_followers = list_followers + [j["value"]]
list_followers = sorted(list_followers)

# Creating the list of following, list of strings of usernames
list_following = []
for i in following_temp_dicts:
    for j in i["string_list_data"]:
        list_following = list_following + [j["value"]]
list_following = sorted(list_following)

print("\nNo of followers " + str(len(list_followers)))
print("No of following " + str(len(list_following)) + "\n")

print("The difference in following and followers is: ")
diff = list(set(list_following) - set(list_followers))
for i in diff:
    print(i)
print()
