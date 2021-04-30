csv = 'Eric,John,Michael,Terry,Graham,TerryG,Brian'
friends_list = []
friends = csv.split(',')

for friend in friends:
    friends_list.append(friend)

print(friends_list)