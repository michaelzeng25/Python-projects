i1, i2 = map(int, input().split())

for x in range(i1, i2):
    if(x>1):
        for y in range(2,x):
            if(x%y==0):
                break
        else:
            print(x)