import math

one = 2
two = 7
three = 6
four = 5
five = 4
six = 3
seven = 2



print("Enter your bith month in numbers e.g feb = 02 and dec = 12: ")
month = int(input())

print("Enter your bith year: ")
year = int(input())
print("Enter the last 4 digits of your NRIC(E.g 321A): ")
last4 = input()


last4ls = list(last4)
letter = last4ls[3].upper()
# print(letter)

yearls = [(year//(10**i))%10 for i in range(math.ceil(math.log(year, 10))-1, -1, -1)]

oners = yearls[2] * one
twors = yearls[3] * two
fivers = int(last4ls[0]) * five
sixrs = int(last4ls[1]) * six
sevenrs = int(last4ls[2]) * seven

sum1 = oners + twors + int(fivers) + int(sixrs) + int(sevenrs)
# print(oners , twors , int(fivers) , int(sixrs) , int(sevenrs))
# print("sum1" , sum1)

if yearls[0] == 1 or 2:
    if letter == 'J':
        remainder = 0
    if letter == 'Z':
        remainder = 1
    if letter == 'I':
        remainder = 2
    if letter == 'H':
        remainder = 3
    if letter == 'G':
        remainder = 4
    if letter == 'F':
        remainder = 5 
    if letter == 'E':
        remainder = 6
    if letter == 'D':
        remainder = 7
    if letter == 'C':
        remainder = 8
    if letter == 'B':
        remainder = 9
    if letter == 'A':
        remainder = 10

# print(remainder)
# totalsum = sum + remainder
# print (totalsum)





list11 = [11,22,33,44,55,66,77,88,99,110,121,132,143,154,165,176,187,198]
sumlist = []
for i in list(list11):
    i = i - sum1
    i = i+remainder
    if i >=0:
        sumlist.append(i)

sumlisttotal = []
list11 = [11,22,33,44,55,66,77,88,99,110,121,132,143,154,165,176,187,198]
sumlisttotal = []
for i in list(list11):
    i = i+remainder
    if i >=0:
        sumlisttotal.append(i)

# print("sumlist",sumlist)
# print("mod11 + 7 sumlisttotal" , sumlisttotal)


test1 = []
test3 = []
for sum in sumlist:
    for i in range(sum):
        x = three * i 
        for j in range(sum):
            y = four * j
            if x + y == sum:
                # print(sum)
                test1.append(i)
                test1.append(j)
                test3.append(sum)
                # print (i , j)
# print("i,j list" , test1)

for u in test1:
    if u >= 10:
        index = test1.index(u)
        if index % 2 == 0:
        
            test1.pop(index)
            test1.pop(index)
        else :
            test1.pop(index)
            test1.pop(index-1)

# print("i,j list after pop" , test1)

# using list comprehension
listToStr = ''.join([str(elem) for elem in test1])
 
# print(listToStr)



n = 2
tlist = [listToStr[i:i+n] for i in range(0, len(listToStr), n)]
# tlist = int(tlist.sort())
tlist =sorted(tlist)
# print("tlist before pop" , tlist)


for i in range(0, len(tlist)):
    tlist[i] = int(tlist[i])


ttlist = []
for i in tlist:
    if i < 50:
        ttlist.append(i)

# print("tlist after pop" , ttlist)


test2 = []
for sum in sumlist:
    for h in sumlisttotal:
        if sum + sum1== h:
            # print("Answer", h)
            test2.append(h)
# print(test2)



choose = (month / 12) * len(ttlist)

# print("choose number" , round(choose))


# if month == 1 or month == 2:
#     digit1 = test1[0]
#     digit2 = test1[1]
# if month == 3 or month == 4 or month == 5:
#     digit1 = test1[2]
#     digit2 = test1[3]
# if month == 6 or month == 7 or month == 8:
#     digit1 = test1[4]
#     digit2 = test1[5]
# if month == 9 or month == 10 or month == 11:
#     digit1 = test1[6]
#     digit2 = test1[7]
# if month == 12:
#     digit1 = test1[8]
#     digit2 = test1[9]

if round(choose) >=1:
    finans = round(choose)-1
    
finans = ttlist[finans]

if yearls[0] == 1:
    letter  = "S"
else: 
    letter = "T"

# print(test1[4] , test1[5])
# print("digits " , digit1 , digit2)
# print("Month" , month)
nric = letter + str(yearls[2]) + str(yearls[3]) + str(finans) + str(last4)

print("My best guess of your NRIC is: " , nric)