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

greetings(names, 3)
