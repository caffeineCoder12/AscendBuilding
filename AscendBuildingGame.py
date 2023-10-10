'''A computer game to ascend a building with a specified number of floors. 
You have three different facilities for each floor to reach the top: 
the elevator (1), the escalator (2), and walking up the stairs (3). 
Each facility has its own scoring rule. Assume the initial score is zero.

• Elevator (1): Score increments to the next even number. 

• Escalator (2): Score increments to the next odd number. 

• Walk (3): Score increments to the next prime number. 

Write an algorithm and python code to display the score to ascend a building.
'''

def even(n):
    ev = []
    a = 2
    for i in range(n):
        ev.append(a)
        a += 2
    return ev

def odd(n):
    od = []
    a = 1
    for i in range(n):
        od.append(a)
        a += 2
    return od

def prime(n):
    pr = []
    num = 2
    while len(pr) < n:
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            pr.append(num)
        num += 1
    return pr

score = 0
n = int(input())
primeLst = prime(n)
oddLst = odd(n)
evenLst = even(n)

for i in range(n):
    facility = int(input())
    
    if facility == 1:
        first = evenLst.pop(0)
        score += first
        print("evenList",evenLst)
        print(score,"even")
        
    elif facility == 2:
        first = oddLst.pop(0)
        score += first
        print("oddList",oddLst)
        print(score,"odd")

    elif facility == 3:
        first = primeLst.pop(0)
        score += first
        print("primeList",primeLst)
        print(score,"prime")

    else:
        continue
print(score)