import pickle
with open("tracks.pkl", "rb") as file:
    results = pickle.load(file)

item_list = list(results.items())

print(len(item_list[1][1]))
# print(item_list[1][1][0]['track']['name'])
# print(item_list[1][1][0]['track']['album']['artists'][0]['name'])
# print(item_list[1][1][1]['track']['album']['name'])