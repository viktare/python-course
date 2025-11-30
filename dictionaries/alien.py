alien_0 = {
    'color': 'green',
    'points': 5
}

alien_1 = {
    'color': 'yellow',
    'points': 10
}

alien_2 = {
    'color': 'blue',
    'points': 15
}

aliens = [alien_0, alien_1, alien_2]

for alien in  aliens:
    print(alien)


users = {
    'aeinstein': {
        'name': 'Albert',
        'surname': 'Einstein',
        'location': 'Princeton'
    },
    'mcurie': {
        'name': 'Marie',
        'surname': 'Curie',
        'location': 'Paris'
    }
}

for username, userinfo in users.items():
    print(f"\nUsername: {username}")
    fullname = f"{userinfo['name']} {userinfo['surname']}"
    location = userinfo['location']

    print(f"\tFull name: {fullname}")
    print(f"\tLocation: {location}")
