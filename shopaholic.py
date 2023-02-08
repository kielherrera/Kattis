def solve(x,price):
    
    price.sort()
    if x == 1 or x == 2:
        return 0
    else:
        total = 0
        count = 0
    
        for i in range(x-1,-1, -1):
            count +=1

            if count == 3:
                count = 0
                total = total + price[i]

    return total        
            
        

x = int(input())
price = list(map(int,input().strip().split(" ")))



print("{}".format(solve(x,price)))
