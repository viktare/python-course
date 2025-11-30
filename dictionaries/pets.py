owner_1 = {
    'name': 'Viktor',
    'surname': 'Stevanovic',
    'city': 'San Zenone degli Ezzelini',
    'address': 'via Antonio Canova'
}

owner_2 = {
    'name': 'Silvia',
    'surname': 'Bordigno',
    'city': 'Mussolente',
    'address': 'via Mussolente 12'
}

pet_1 = {
    'animal': 'cat',
    'name': 'Aki',
    'owner': owner_1
}

pet_2 = {
    'animal': 'dog',
    'name': 'Roberto',
    'owner': owner_2
}

owners = [owner_1, owner_2]
pets = [pet_1, pet_2]

for pet in pets:
    for key, value in pet.items():
        phrase: list = []
        if key == 'animal':
            phrase.append(f"This animal is a {value}")
        if key == 'name':
            phrase.append(f"and its name is {value}.")
        if key == 'owner':
            phrase.append(f"His owner is {value['name']}")
        print('c'.join(phrase))
