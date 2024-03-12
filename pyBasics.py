print("Hello World")
t = 7
b = 0
while b < t:
    print(b)
    b+=1

#print("Hello")

names = ["Muna", "Bube", "Moses"]

def greetings(name_list, room_num):
    for name in name_list:
        print(f"Welcome {name}")
        print(f"You are in room {room_num}")
    print(f"There are {len(name_list)} people in this room")

    if len(name_list) < 5:
        print("You are in a small room")
    else:
        print("You are in a normal room")

greetings(names, 3)
