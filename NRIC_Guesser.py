import math
from bisect import bisect_left

one = 2
two = 7
three = 6
four = 5
five = 4
six = 3
seven = 2

yearDict = {2021: 38672, 2020: 38590, 2019: 39279, 2018: 39039, 2017: 39615, 2016: 41251, 2015: 42185, 2014: 42232,
            2013: 39720, 2012: 42663, 2011: 39654, 2010: 37967, 2009: 39570, 2008: 39826, 2007: 39490, 2006: 38317,
            2005: 37492, 2004: 37174, 2003: 37485, 2002: 40760, 2001: 41451, 2000: 46997, 1999: 43336, 1998: 43664,
            1997: 47333, 1996: 48577, 1995: 48635, 1994: 49554, 1993: 50225, 1992: 49402, 1991: 49114, 1990: 51142,
            1989: 47669, 1988: 52957, 1987: 43616, 1986: 38379, 1985: 42484, 1984: 41556, 1983: 40585, 1982: 42654,
            1981: 42250, 1980: 41217, 1979: 40779, 1978: 39441, 1977: 38364, 1976: 42783, 1975: 39948, 1974: 43268,
            1973: 48269, 1972: 49678, 1971: 47088, 1970: 45934, 1969: 44562, 1968: 47241, 1967: 50560, 1966: 54680,
            1965: 55725, 1964: 58217, 1963: 59530, 1962: 58977, 1961: 59930, 1960: 61775}


  

print("Enter your bith month in numbers e.g feb = 02 and dec = 12: ")
month = int(input())

print("Enter your bith year: ")
year = int(input())
print("Enter the last 4 digits of your NRIC(E.g 321A): ")
last4 = input()

totalBirths = yearDict[year]
print('totalBirth: ', totalBirths)

last4ls = list(last4)
letter = last4ls[3].upper()
# print(letter)

yearls = [(year//(10**i))%10 for i in range(math.ceil(math.log(year, 10))-1, -1, -1)]


print("yearls" , yearls)

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
print("tlist before pop" , tlist)

for i in tlist:
    if len(i) == 1:
        n = i+"0"
        tlist.remove(i)
        tlist.append(n)

def remove_duplicates_recursion (dupList, temp):
    if len(dupList) == 0: #condition 0 --> base case
        return dupList
    if dupList[0] in temp: #condition 1
        temp.append(dupList[0])
        return remove_duplicates_recursion(dupList[1:], temp)
    else: #condition 2
        temp.append(dupList[0])
        return [dupList[0]] + remove_duplicates_recursion(dupList[1:], temp)

def remdup(l, dup=None):
	# If has zero or one elements, there are no duplicates.
	if len(l) < 2:
		return l

	# If there's a duplicate to remove, remove it and recurse until ValueError
	# is raised, which means there are none left to remove. Since lists are
	# mutable, we don't have to capture this.
	if dup is not None:
		try:
			l.remove(dup)
			remdup(l, dup)
		except ValueError:
			pass

	# No more duplicates to remove? Then recurse, removing duplicates of the
	# current head!
	return [l[0]] + remdup(l[1:], l[0])

tlist1 = []
tlist =sorted(tlist)
remdup(tlist)
print("tlist after new function to remove duplicates" , tlist)
remove_duplicates_recursion(tlist, tlist1)
print("number list without duplicates", remove_duplicates_recursion(tlist, tlist1))

# for i in range(0, len(tlist)):
#     tlist[i] = int(tlist[i])

print("tlist1" , tlist1)

print(int(str(totalBirths)[:2]))
ttlist = []
for i in tlist1:
    if int(i) <= int(str(totalBirths)[:2]):
        ttlist.append(i)

ttlist =sorted(ttlist)
print("tlist after pop" , ttlist)



ttlist000 = []
for t in ttlist:
    a = t + "000" 
    ttlist000.append(a)

print(ttlist000)
ttlist001 = []
print(remove_duplicates_recursion(ttlist000, ttlist001))

print("Last 4: " , last4)



test2 = []
for sum in sumlist:
    for h in sumlisttotal:
        if sum + sum1== h:
            # print("Answer", h)
            test2.append(h)
# print(test2)



# choose = (month / 12) * len(ttlist)
# print("choose before round" , choose)
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

# if round(choose) >=1:
#     finans = round(choose)-1
    
# finans = ttlist[finans]

# last3num = str(last4)[:3]
# if int(last3num) > int(str(totalBirths)[:-3]):
#     if finans == int(str(totalBirths)[:2]):
#         finans = finans - 1

if yearls[0] == 1:
    letter  = "S"
else: 
    letter = "T"


choose1 = (totalBirths/12) * month
print("totalbirthfirst2" , choose1)
choose1 = choose1 * (1-((month / 12)/2))
print("choose1 after 0.5 algo" , choose1)
# if len(str(round(choose1))) == 5:
#     op = int(str(choose1)[:2])
# else :
#     op = int(str(choose1)[:1])


def take_closest(myList, myNumber):
    """
    Assumes myList is sorted. Returns closest value to myNumber.

    If two numbers are equally close, return the smallest number.
    """
    pos = bisect_left(myList, myNumber)
    if pos == 0:
        return myList[0]
    if pos == len(myList):
        return myList[-1]
    before = myList[pos - 1]
    after = myList[pos]
    if after - myNumber < myNumber - before:
        return after
    else:
        return before

for i in range(0, len(ttlist001)):
    ttlist001[i] = int(ttlist001[i])

finans1 = take_closest(ttlist001, round(choose1))
print(finans1)

if len(str(finans1)) == 1:
    finans1 = str(finans1)
    finans1 = "0" + finans1
# print(test1[4] , test1[5])
# print("digits " , digit1 , digit2)
# print("Month" , month)
nric = letter + str(yearls[2]) + str(yearls[3]) + str(finans1)[:2] + str(last4)

print("My best guess of your NRIC is: " , nric)