'''You are asked to ensure that the first and last names of people begin with a capital letter in their passports. For example, alison heck should be capitalised correctly as Alison Heck.'''

def solve(s):
    
    ans = s.split(' ')
    ans1 = (((i.capitalize() for i in ans)))
    return ' '.join(ans1)

'''Q2)'''

def average(array):
    my_set = set(array)
    avg = sum(my_set)/len(my_set)
    
    return (avg)
         
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)

    '''Q3)'''

    import textwrap

def wrap(string, max_width):
    return textwrap.fill(string, max_width)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

    '''Q4)'''

    a = "abcdefghijklmnopqrstuvwxyz"
def print_rangoli(size):
    
    lines = []
    for row in range(size):
        print_ = "-".join(a[row:size])
        lines.append(print_[::-1] + print_[1:])
    width = len(lines[0])
    
    for row in range(size-1, 0, -1):
        print(lines[row].center(width, '-'))
        
    for row in range(size):
        print(lines[row].center(width, '-'))
    # your code goes here

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)


    '''Q5)'''

    from collections import OrderedDict
def merge_the_tools(string, k):
    # your code goes here
    i = 0
    while i < len(string):
        word1 = "".join(OrderedDict.fromkeys(string[i: i+k]))      
        print(word1)
        i = i + k

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

    '''Q6)'''
    from collections import Counter
x = int(input())
y = Counter(map(int, input().split()))
z = int(input())

total = 0
for i in range(z):
    size, rate = map(int, input().split())
    if y[size]: 
        y[size] -= 1
        total += rate
print(total)


'''Q7)'''

for i in range(int(input())):
    try:
        a, b = map(int, input().split())
        print(int(a//b))
    except Exception as e:
        print("Error Code:",e)



''' Q8)'''

import re
n = int(input())
for i in range(0,n):  
    try:
        input_ = input()
        a = (re.compile(input_))
        print(bool(a))
    except re.error:
        print('False')


'''Q9)'''
n = int(input())
s = set(map(int, input().split()))
N = int(input())
for i in range(N):
    cmd = list(map(str, input().split()))
    if cmd[0] == "pop":
        s.pop()
    elif cmd[0] == "remove":
        try:
            s.remove(int(cmd[1]))
        except:
            continue
    elif cmd[0] == "discard":
        try:
            s.discard(int(cmd[1]))
        except:
            continue
print(sum(s))