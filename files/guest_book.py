running = True
guests = []
while running:
    name = input('Could you please provide your name? ')
    if name == 'q':
        running = False
    else:
        print(f"Thank you {name}!")
        guests.append(name)

with open('guest_book.txt', 'a') as file_object:
    for guest in guests:
        file_object.write(guest + '\n')
