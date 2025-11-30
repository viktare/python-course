# guest list
guest_list = ['Mirko', 'Silvia', 'Marco']
# print invitation to the guests
def invite(guest: str):
    return f"Hi {guest.title()}, you have been invited to the dinner at my place tomorrow evening. Greetings"

for guest in guest_list:
    print(invite(guest))

# one guest can't make it, print him
refused_guest = guest_list.pop(0)
print(f"Unfortunately, {refused_guest.title()} won't be able to make it to the dinner. We should invite someone else..")

# invite someone else at his place, re send invitations
guest_list.append("Veronika")

def remember_dinner(guest: str):
    print(f"Hi {guest.title()}, just a reminder that the dinner starts at 8PM!")

for guest_to_remind in guest_list:
    remember_dinner(guest_to_remind)

guest_list.append("Mattia")

guest_list.insert(0, "Massi")

guest_list.insert(4, "Stefania") 

test = [0, 1, 3]
test.append(12)
print(test)