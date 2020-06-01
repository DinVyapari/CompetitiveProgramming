#Magic! Do not touch.
======================================================
X=list
Y=list2
sort list acc to list 2/to match sorted(list 2)
X_new=[x for y, x in sorted(zip(Y, X))]
======================================================
zip(list1, list2)=({l1[0], l2[0]}, {l1[1], l2[1]},......)
======================================================
Keymax = max(dictname, key=dictname.get)
MaxOccuringElem = (max(set(list)), key=list.count)
======================================================
lis=[str[x:y] for x, y in combinations(range(len(str)+1),r=2)]
gives list of substrings
======================================================
sum(map(int, input())) //gives sum of digits of input!
int(string, base)
========================================================
Mode of list gives most frequent element
list(set(listname)) //using set gives list with duplicates removed
listname.del(index)
listname.remove(elementname)
===========================================================
import time
Epoch=Thu Jan  1 00:00:00 1970
time.gmtime(seconds) gives GMT time tuple
time.localtime(seconds) gives local time tuple
time.ctime(seconds) gives local time formatted
time.asctime(time.gmtime(seconds)) gives GMT time formatted
============================================================
print('Python is\r123456') why not 123456 is
len type id
try except else finally
stringname.isnumeric() will return True or False
round=(int(avg*100))/100 #truncates to two decimal points
n[::-1] reverses string n
isinstance(object, classinfo) returns true or false
return and global
break pass continue
append and extend
abs(m-n) #absolute value
=================================
m,n=input().split()
m,n=map(int,input().split())
m,n=list(map(int,input().split()))
=================================
sep and end
min max count sum sort
math.gcd(a, b) or Euclid's Alg or Recursion        '
===========================
print(*n, sep=' ')
print(' '.join(n))
print(n[x], end=' ') x in range
===========================
input().strip()
f, *l = input().split() //f is first input, other inputs in list l
*n, = input().split()
