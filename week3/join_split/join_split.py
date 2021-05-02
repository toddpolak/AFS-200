csv = 'Eric,John,Michael,Terry,Graham:TerryG;Brian'

print('csv: ', csv)

friends1 = csv.split(',')

print('friends1: ', friends1)

friends_list = friends1[:4]

friends2 = friends1[4]

print('friends2: ', friends2)

friends3 = friends2.split(':')

print('friends3: ', friends3)

friends_list.append(friends3[0])

friends4 = friends3[1].split(';')

print('friends4: ', friends4)

for elem in friends4:
    friends_list.append(elem)

print('friends_list: ', friends_list)