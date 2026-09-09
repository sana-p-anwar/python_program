def lcm(x,y):
    if x>y:
        greator = x
    else:
        greator=y
    while True:
        if greator%x==0 and greator%y==0:
            lcm=greator
            break
        greator+=1
    return lcm
print(lcm(3,6))