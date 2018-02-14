coins=21
player=1
s=0
print("Number is coins : ",coins)
while True:
    print("Player",player,"enter number of coins from 1 to 3")
    while True:
        p=str(input("1 or 2 or 3 coins?"))
        if p.isdigit()==True:
           
         s=int(p)
        if s in [1,2,3] and s<coins:
            break
        print("illegal coins must be from 1 to 3")    
    coins=coins-s
    print(coins)
    if coins==1:
        print("the winner is player",player)
        break
    if player==1:
              player=2
    elif player==2:
              player=1
