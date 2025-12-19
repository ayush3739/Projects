import random
import images
import data
import os
#checking if it is changing in the github or not
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

print(images.logo)
i=0
def greater(A, B):
    return 'A a' if A > B else 'B b'
score=0
print(images.logo)
item_a = random.choice(data.data)
while True :
    item_b = random.choice(data.data)

    while item_b == item_a:
        item_b = random.choice(data.data)

    print(f"Compare A: {item_a['name']}, {item_a['description']}, from {item_a['country']}.")
    print(images.vs)
    print(f"Compare B: {item_b['name']}, {item_b['description']}, from {item_b['country']}.")
    A = item_a['follower_count']
    B = item_b['follower_count']
    
    choose=input("Who has more followers?  Type 'A' or 'B' :")
    correct=greater(A,B)
    clear()
    if choose in correct:
        score+=1
        i+=1
        item_a = item_a if correct == 'A' else item_b
    else:
        print(f"sorry that's wrong .final score {score}")
        break
    print(f"Your current score:{score}\n")
    
    
#clear the screen between rounds
