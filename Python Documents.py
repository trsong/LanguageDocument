Python2.0 Documents
By T.R.Song 4/25/2013 Version 1.0
You should open it with notepad++
________________________________________________
Chapter 1: Values,Expressions,Statements
Chapter 2: Functions
Chapter 3: Conditionnals and recursions
Chapter 4: Loops
Chapter 5: Strings
Chapter 6: Lists
Chapter 7: Dictionaries
Chapter 8: Tuples
Chapter 9: Files
Chapter 10: Classes and objects
Appendix:
	string
	list
	dictionary
	math
	tuple
	random
________________________________________________ 
Chapter 1: Values,Expressions,Statements
#sample statements
print "hello world"
type("hello world") #=> <type 'str'>
n = 17
pi = 3.1315926
pw2 = 2**3 #=>8

#Type Conversion
int('32') #=>32
int(3.9999999)#=> 3
int(-2.33333) #=>-2 int() chops off the fraction part
float(2) #=>2.0
str(123) #=>'123'

# Global Variables
myFlag = False
def triggerFunc():
	global myFlag
	myFlag = True
## note: without global, in triggerFunc, python will create a new variable also called myFlag

---------------------------------------------------
Chapter 2: Functions
import math
print math #=>> <module 'math' (built-in)> 
pi = math.pi
sinVal = math.sin(pi)
log10Val = math.log10(100)
sqrVal = math.sqrt(4)
powVal = math.pow(2,3) #=>8

#function defn
def printFunc():
	print "This is a function."

>>> print printFunc
<function printFunc at 0x0000000002773AC8>
>>> type(printFunc)
<type 'function'>
>>> 
## Void fucntion returns value: None
>>> i = printFunc()
This is a function.
>>> print i
None
>>> type(None)
<type 'NoneType'>
>>> 
## None has its own type: NoneType


def addFunc(num1,num2):
	return num1+num2
	
# random function
import random
x = random.random() #generate a random float number from 0<=x<1
xInt = random.randint(0,10) #generate a random integer from 0 to 10 inclusively
t = [1,2,3]
random.choice(t) #choose one elem from the list t
"""random also include distributions like gaussian exponential gamma """
"""Use help random for more functions"""
import math
x = math.floor(random.uniform(0,100)) #uniform on [0,100) 

------------------------------------------------
Chapter 3: Conditionnals and recursions
#Quotient and Remainder
quotient = 7/3  #=> 2
remainder = 7%3 #=> 1

#Boolean Expression
== != > < >= <=
>>> type(True)
<type 'bool'>

not and or
17 and True #=> True

# if condition
if x>0:
	print 'x is positive'
elif x>1000:
	pass # wait until further notice
elif x<0:
	print 'x is negative'
else:
	print 'x is zero'

# Recursion
def countdown(n):
	if n<=0:
		print "END"
	else:
		print n
		countdown(n-1)
		
##Maximum Recursion Depth
def f():
	f()
>>> f()
Traceback (most recent call last):
.....
File "C:\Program Files (x86)\Wing IDE 101 3.2\src\debug\tserver\_sandbox.py", line 2, in f
    if __name__ == '__main__':
RuntimeError: maximum recursion depth exceeded

#I/O
>>>inputStr = raw_input()
I'm a string
>>>print inputStr
I'm a string
>>> inputWithPrompt = raw_input('What r u doing now?\n')
What r u doing now?
shit
>>> print inputPrompt
shit

---------------------------------------------------------------------------
Chapter 4: Loops
#increment
i = 1
i +=1 # !!!!!NOT i++ WONT WORK HERE

#while loop
While True:
	if(i>10):
		break
	else:
		print i

#for loop
for i in range(10):
	print i

--------------------------------------------------------------------------
Chapter 5: Strings
#string operations
myString='a' + 'b' #=> 'ab'
myString= 'a'*3 #=>'aaa'

fruitStr = 'banana'
init = fruitStr[0] #=> b
last = fruitStr[-1] #=> a
length = len(fruitStr) #=> 6
## Also:  fruitStr[-1] == fruitStr[len(fruitStr)-1]
## Warning: Strings are immutable

#Eval string
eval('1+2*3') #=> 7
eval('math.sqrt(4)') #=>2

#iteration through a string
for char in fruitStr:
	print char
	
#substring
A = fruitStr[0:2] #=> 'ba'
B = fruitStr[:2] #=>'ba'
C = fruitStr[1:-1] #=> 'anan'
D = fruitStr[3:] #=>'ana'
E = fruitStr[:] #=> Make a copy of string  'banana'
F = fruitStr[::2] #=> 'bnn' make a copy every other character
G = fruitStr[::-1] #=> 'ananab' every -1 word means Reverse

#string methods
UpperStr = fruitStr.upper()
index = fruitStr.find('a') #=> 1
index = fruitStr.find('x') #=>-1
index = fruitStr.find('b',1,4) #=>-1  find(str,startPosn,endPosn)
"I'm a little nervous.".replace(" ","") #replace /whitespace with ""
 
# in operator
'a' in 'banana' #=> True
'seed' in 'banana' #=> False

# string comparison
'a' == 'a'  #=>True
'A' < 'a'   #=>True ,lexicalgraphically ordered

# string formating operator: %
## Tuples techniques required
>>>myStr = "I've farmed %s for %d hrs, guessing the drop rate is below %g percent" % ('maramusa',3,0.3)
>>>myStr
"I've farmed maramusa for 3 hrs, guessing the drop rate is below 0.3 percent"
## remember; %d for integer; %s for string; %g for float number
>>> pi = '%g' % 3.1415926
>>> pi
'3.14159'

# Debugging 
>>> s = '1 2\t 3\n 4'
>>> print s
1 2	 3
 4
>>> print repr(s) #repr takes an argument and return a string representation of it
'1 2\t 3\n 4'

See Appendix for more
--------------------------------------------------------------------
Chapter 6: Lists
strList = ['a','b','c']
numList = [1,2,3]
myList = ['spam',2.0,5,[10,20]]
empty = []

#List operations
a = [1,2,3]
b = [4,5,6]
c = a + b #=> [1,2,3,4,5,6]
d = a*2 #=> [1,2,3,1,2,3]
a[0] = 2 #=> [2,2,3]
a[1:3] = ['a','b']  #=> [1,'a','b']
>>> a = range(10)
>>> a
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> a[3:4]=[11,11,11,11]
>>> a
[0, 1, 2, 11, 11, 11, 11, 4, 5, 6, 7, 8, 9]

#iteration through a list
for elem in myList:
	print elem

# in operator
1 in a #=> True

# List Methods
a.append('4') #=> a==[1,2,3,4]
## WARNING NOT USE  lst= a.append('4'),which leads to lst== None  
a.extend(b) #=> a==[1,2,3,4,5,6]
t = ['c','b','z','a']
t.sort() #=> t==['a','b','c','z']
t.sort(reverse=True) #=>t==['z','c','b','a']

num = a.pop(1) # => num==2 a==[1,3]
last = a.pop() #=> last=3 a==[1,2]
del a[1] #=> a==[1,3]
del a[1:2] #=> a==[1,3]

>>> b = ['a']*3
>>> b
['a', 'a', 'a']
>>> b.remove('a')
>>> b
['a', 'a']

# lambda, map, filter, and reduce
myAdd = lambda x,y: x+y
map(abs,[-1,-2,3]) #=>[1,2,3]
filter(isupper,['a','A','c']) #=>['A']
reduce(myAdd,[1,2,3],0) #=> 6 

# list and string
t = list('abc') #=> ['a','b','c']
s = 'waiting for ja'.split() #=>['waiting','for','ja']
l = ' '.join(['waiting','for','ja']) #=>'waiting for ja'  join is reverse of split

m = 'spam-spam-spam'.split('-') #=>['spam','spam','spam']
j = '-'.join(['spam','spam','spam']) #=> 'spam-spam-spam'

# Aliasing and reference
>>> a = 'abc'
>>> b = 'abc'
>>> a is b
True
##Since Strings are immutable, a,b reference to the same string doesn't matter

>>> a = [1,2,3]
>>> b=[1,2,3]
>>> a is b
False
##Since lists are mutable, a,b always refer to different objects
## using b = a[:] to make a copy of a

 
# AVOID USING THIS
# a.append([1]) 
# a = a.append(1)
# using a + [1] to append
# t = t + 1
--------------------------------------------------------------------
Chapter 7: Dictionaries
myDic = dict()
myDic['a'] = 1 #=> myDic == {'a':1}

myDic2 = {'one':1,'two':2,'three':3}

# in operations (searching for keys)
'one' is myDic #=> True
1 in myDic #=> False

# Dictionary use, histogram
def histogram(s):
	d = dict
	for c in s:
		if c not in d:
			d[c] = 1
		else:
			d[c] +=1
	return d

# the get method
myDefaultVal = 0
val = myDic.get('two',myDefaultVal) #=> 2
val = myDic.get('six',-1) #=> -1

--------------------------------------------------------------------
Chapter 8: Tuples
#Tuples are immutable
t = 'a','b','c'
t = ('a','b','c')
t[0] #=> 'a' one element is not a tuple
t[1:3] #=>('b','c')

#modify a tuple
t = ('A',)+t[1:] #=>('A','b','c')

# tuple asignment
a, b = 1,2
a,b = b,a #a==2 b==1
email = 'lamourthelove@hotmail.com'
uname,domain = email.split('@')

# tuples and functions
quotient, remainder = divmod(7,3) #divmod is a built-in function
								  #quotient == 2 remainder == 1

def printFunc(*arg)
	print arg
## use * to gather, with * arg can be coverted into one object: tuple
divmod(*(7,3))
## also use * to scatter
## divmod takes exactly two args, not a tuple, need to scatter

#optional parameters
def myMax(a,b=-1)
	return max(a,b)
>>>myMax(1) #=>1
>>>myMax(1,2) #=>2
## optional parameters override the default value
	
# lists and tuples
# Zip Function
>>> s = 'abc'
>>> t=[0,1,2]
>>> zip(s,t)
[('a', 0), ('b', 1), ('c', 2)]

>>> a=[1,2,3]
>>> b=[4,5,6,7]
>>> zip(a,b)
[(1, 4), (2, 5), (3, 6)]

# dictionaries and tuples
>>> d = {'a':0,'b':1,'c':2}
>>> d
{'a': 0, 'c': 2, 'b': 1}
>>>t = d.items()
>>>t
[('a', 0), ('c', 2), ('b', 1)]
>>> dict(t)
{'a': 0, 'c': 2, 'b': 1}

#iteration through  ListOfTuples
for key,val in d.items():
	print key, val
	
# tuples as keys 
#myDict[last,first] = number
myDict = {("song","Tangrui"):85}
for last,first in myDict:
	print first,last,myDict[last,first]

# both lists and tuples are comparable
>>> [1,2,3]<[4,5,6]
True
>>> (1,2,3)<(1,2)
False

--------------------------------------------------------------------
Chapter 9: Files
# Reading / Writing
myFile = open("myfile.txt",'w') # 'w' means in writing mode. (1) if "myfile.txt" does not exist, system create a new one
								# 							 (2) if not, it clears "myfile.txt" and starts fresh.
line1 = "I've farmed the surt for a whole day, but i didn't see any maramusas.\n"
myFile.write(line1)
line2 = "Damn. Ragnarok Odyssey is always stupid. It has such a low item-drop rate.\n"
myFile.write(line2)
myFile.write(str(333)) #Note: write method can only take a string as a parameter. Need to use str() to convert
myFile.close()

# os -- operating system
>>>import os
>>>currentWorkingDirectory = os.getcwd()
>>> print currentWorkingDirectory
'd:\\Programming\\python'
>>>absolutePath = os.path.abspath("myfile.txt")
>>>print absolutePath
'd:\\Programming\\python\\myfile.txt'
>>>os.path.exists("myfile.txt")
True
>>>os.path.isdir('myfile.txt') #check whether is directory
False
>>>os.path.isdir('..')
True
>>> os.listdir(os.getcwd()) #list files in CWD
['documentational Use.py', 'myfile.txt']
>>> os.listdir('.')
['documentational Use.py', 'myfile.txt']
>>> os.listdir('..')
['html', 'HTML documents.html', 'httprequest', 'python', 'Python Documents.py']
>>> os.listdir('/')
['$RECYCLE.BIN', '360\xb0\xb2\xc8\xab\xe4\xaf\xc0\xc0\xc6\xf7\xcf\xc2\xd4\xd8', 'DrRacket', 'Eclipse', 'IELTS', 'KuGou', 'msdownld.tmp', 'Program Files', 'Programming', 'System Volume Information', 'VirtualBox', 'waterloo', '\xd6\xd0\xb9\xfa\xb9\xdd.jpg']

def walk(dir):
	for name in os.listdir(dir):
		path = os.path.join(dir,name) #os.path.join takes a directory and a file name, and join them into a comple path
		
		if os.path.isfile(path): #check whether is file
			print path
		else:
			walk(path)
>>> walk(".")
.\documentational Use.py
.\myfile.txt

# Catching Exceptions
## althou isfile, isdir may help, it always has exceptions
try:
	fin = open('bad_file')
	for line in fin:
		print line
	fin.close()
except:
	print 'Something went wrong.'

# Databases
## DB like dictionary which has key-value pairs in it
import anydbm 		#anydbm is really the name of it, no kidding
db = anydbm.open('hereIsDB.db','c') # 'c' meands to create
## Now, db acts like a dictory
db['a'] = "1"  #Key,Value must be String or None
print db['a']
for key in db:
	print key,db[key]
db.close()

""""Here's the interface """
It has the following interface (key and data are strings):
    
d[key] = data   # store data at key (may override data at
                # existing key)
data = d[key]   # retrieve data at key (raise KeyError if no
                # such key)
del d[key]      # delete data stored at key (raises KeyError
                # if no such key)
flag = key in d # true if the key exists
list = d.keys() # return a list of all existing keys (slow!)


# pickling ;; as stringify and parse in Javascript
## since key,val in anydbm must both be string 
## we can use pickle model to convert other type into string and then change back
>>> import pickle
>>> t = [1,2,3]
>>> s = pickle.dumps(t) #stringifying objects
>>> s
'(lp0\nI1\naI2\naI3\na.' #thou it looks bad
>>> t2 = pickle.loads(s) #parse it back
>>> t2
[1, 2, 3]  
>>> t == t2 #means they have the same value
True
>>> t is t2 #means t2 is a copy of t
False

""" shelve acts like the combination of anydbm and pickle"""
import shelve
help(shelve)
#here's the description
 A "shelf" is a persistent, dictionary-like object.  The difference
    with dbm databases is that the values (not the keys!) in a shelf can
    be essentially arbitrary Python objects -- anything that the "pickle"
    module can handle.  This includes most class instances, recursive data
    types, and objects containing lots of shared sub-objects.  The keys
    are ordinary strings.
	
# Pipes ;;shell in VB
# using window commmand shell as an example
>>> import os
>>> cmd = 'dir'
>>> fp = os.popen(cmd)
>>> fp
<open file 'dir', mode 'r' at 0x00000000026B29C0>
>>> res = fp.read()  # also use for loop + readline, if necessary
>>> res
' \xc7\xfd\xb6\xaf\xc6\xf7 D \xd6\xd0\xb5\xc4\xbe\xed\xca\xc7 Work\n \xbe\xed\xb5\xc4\xd0\xf2\xc1\xd0\xba\xc5\xca\xc7 6240-5129\n\n d:\\Programming\\python \xb5\xc4\xc4\xbf\xc2\xbc\n\n2013/04/25  20:05    <DIR>          .\n2013/04/25  20:05    <DIR>          ..\n2013/04/25  19:19               445 documentational Use.py\n2013/04/25  20:38            24,576 hereIsDB.db\n2013/04/25  21:05               150 myfile.txt\n               3 \xb8\xf6\xce\xc4\xbc\xfe         25,171 \xd7\xd6\xbd\xda\n               2 \xb8\xf6\xc4\xbf\xc2\xbc 119,540,989,952 \xbf\xc9\xd3\xc3\xd7\xd6\xbd\xda\n'
>>> stat = fp.close()
>>> print res
 驱动器 D 中的卷是 Work
 卷的序列号是 6240-5129

 d:\Programming\python 的目录

2013/04/25  20:05    <DIR>          .
2013/04/25  20:05    <DIR>          ..
2013/04/25  19:19               445 documentational Use.py
2013/04/25  20:38            24,576 hereIsDB.db
2013/04/25  21:05               150 myfile.txt
               3 个文件         25,171 字节
               2 个目录 119,540,989,952 可用字节

>>> print stat #None means it ends normally
None

# Writing modules
_____________________wc.py_____________________
def linecount(filename):
	count = 0
	for line in open(filename):
		count +=1
	return count
	
if __name__== '__main__':  # __name__ is a built-in variable; __name__=='__main__' means the program is running this(wc.py) as a script 
	print linecount('wc.py')
____________________END________________________

>>>import wc              
>>>wc.linecount('wc.py')
7
>>> from wc import linecount #specifically import functions

--------------------------------------------------------------------
Chapter 10: Classes and objects
class Point(object):
	""" a point in x-y plane"""
	
pt = Point()
pt.x = 1
pt.y = 2 #set attributes

# instances as return values
def midPt(pt1,pt2):
	p = Point()
	p.x = pt1.x/2.0 +pt2.x/2.0
	p.y = pt1.y/2.0 +pt2.y/2.0
	return p
#Objects are mutable
p.x +=1
p.y +=p.x
def modifyFunc(p)
	p.x +=1
	p.y +=p.x  #yep, we r trying to modify the object
	
#Copying
import copy
p2 = copy.copy(p)
p2 == p #=> False
p2 is p #=> False

#deep copy
p2 = copy.deepcopy(p) # compared with shallow copy, deepcopy copys everything not just a reference

#check attribute
hasattr(p,'x') #=> True
hasattr(p,'z') #=> False

# Object-oriented programming
What is object-oriented programming
(1) programs made up of objects and functions
(2) object and function definitions interact to realworld
Methods: Class inheritance polymorphism

class Time(object):
	"""represents the time of a day
	   attributes: hour, minutes, seconds"""
	def print_time(self): #time.print_time()
		print '%.2d:%.2d:%.2d' % (self.hour,self.minute,self.second)
		
	def __init__(self,hour=0,minute=0,second=0): # time = Time() or time = Time(6,30,0)
		seconds = 3600*hour+60*minute+second
        minutes, second = divmod(seconds,60)
		hour,minute = divmod(minutes,60)
		self.hour = hour
		self.minute = minute
		self.second = second    #now, even time = Time(0,0,3600) is allowed
	
	def __str__(self): # print time
		return '%.2d:%.2d:%.2d' % (self.hour,self.minute,self.second)
		
	def time_to_int(self): #time.time_to_int()
		return self.hour*3600+self.minute*60+self.second
	
	def increment(self,seconds): #time.increment(60)
		seconds+= self.time_to_int()
		return int_to_time(seconds)
		
	def add_time(self,other): #time = time1.add_time(time2)
		seconds = self.time_to_int()+other.time_to_int()
		return int_to_time(seconds)
		
	def __add__(self,other):  # time1 + time2 or time1 + integer is allow
		if isinstance(other,Time): # isinstance takes a value and a class oject, returns True if the value is an instance of the class
			return self.add_time(other)
		else:
			return self.increment(other)
		
	def __radd__(self,other): #radd for right-side add. like integer + time
		return self.__add__(other)		
	
	def print_attributes(self):
		for attr in self.__dict__:
			print attr,getattr(self,attr) #getattr takes an object and an attribute name and returns its value
			
def int_to_time(seconds):
	time = Time()
	minutes, time.second = divmod(seconds,60)
	time.hour,time.minute = divmod(minutes,60)
	return time
	
# polymorphism
t1 = Time(0,0,3600)
t2 = Time(0,0,1800)
t3 = Time()
print (sum([t1,t2,t3])) #=> 01:30:00

#print attribute
>>>print t1.__dict__ #__dict__ is built-in
{'second': 0, 'minute': 0, 'hour': 1}
## normally we add a method to the class instead of using __dict__
--------------------------------------------------------------------
Appendix:
String
class str(basestring)
 |  str(object) -> string
 |  
 |  Return a nice string representation of the object.
 |  If the argument is a string, the return value is the same object.
 |  
 |  Method resolution order:
 |      str
 |      basestring
 |      object
 |  
 |  Methods defined here:
 |  
 |  __add__(...)
 |      x.__add__(y) <==> x+y
 |  
 |  __contains__(...)
 |      x.__contains__(y) <==> y in x
 |  
 |  __eq__(...)
 |      x.__eq__(y) <==> x==y
 |  
 |  __format__(...)
 |      S.__format__(format_spec) -> string
 |      
 |      Return a formatted version of S as described by format_spec.
 |  
 |  __ge__(...)
 |      x.__ge__(y) <==> x>=y
 |  
 |  __getattribute__(...)
 |      x.__getattribute__('name') <==> x.name
 |  
 |  __getitem__(...)
 |      x.__getitem__(y) <==> x[y]
 |  
 |  __getnewargs__(...)
 |  
 |  __getslice__(...)
 |      x.__getslice__(i, j) <==> x[i:j]
 |      
 |      Use of negative indices is not supported.
 |  
 |  __gt__(...)
 |      x.__gt__(y) <==> x>y
 |  
 |  __hash__(...)
 |      x.__hash__() <==> hash(x)
 |  
 |  __le__(...)
 |      x.__le__(y) <==> x<=y
 |  
 |  __len__(...)
 |      x.__len__() <==> len(x)
 |  
 |  __lt__(...)
 |      x.__lt__(y) <==> x<y
 |  
 |  __mod__(...)
 |      x.__mod__(y) <==> x%y
 |  
 |  __mul__(...)
 |      x.__mul__(n) <==> x*n
 |  
 |  __ne__(...)
 |      x.__ne__(y) <==> x!=y
 |  
 |  __repr__(...)
 |      x.__repr__() <==> repr(x)
 |  
 |  __rmod__(...)
 |      x.__rmod__(y) <==> y%x
 |  
 |  __rmul__(...)
 |      x.__rmul__(n) <==> n*x
 |  
 |  __sizeof__(...)
 |      S.__sizeof__() -> size of S in memory, in bytes
 |  
 |  __str__(...)
 |      x.__str__() <==> str(x)
 |  
 |  capitalize(...)
 |      S.capitalize() -> string
 |      
 |      Return a copy of the string S with only its first character
 |      capitalized.
 |  
 |  center(...)
 |      S.center(width[, fillchar]) -> string
 |      
 |      Return S centered in a string of length width. Padding is
 |      done using the specified fill character (default is a space)
 |  
 |  count(...)
 |      S.count(sub[, start[, end]]) -> int
 |      
 |      Return the number of non-overlapping occurrences of substring sub in
 |      string S[start:end].  Optional arguments start and end are interpreted
 |      as in slice notation.
 |  
 |  decode(...)
 |      S.decode([encoding[,errors]]) -> object
 |      
 |      Decodes S using the codec registered for encoding. encoding defaults
 |      to the default encoding. errors may be given to set a different error
 |      handling scheme. Default is 'strict' meaning that encoding errors raise
 |      a UnicodeDecodeError. Other possible values are 'ignore' and 'replace'
 |      as well as any other name registered with codecs.register_error that is
 |      able to handle UnicodeDecodeErrors.
 |  
 |  encode(...)
 |      S.encode([encoding[,errors]]) -> object
 |      
 |      Encodes S using the codec registered for encoding. encoding defaults
 |      to the default encoding. errors may be given to set a different error
 |      handling scheme. Default is 'strict' meaning that encoding errors raise
 |      a UnicodeEncodeError. Other possible values are 'ignore', 'replace' and
 |      'xmlcharrefreplace' as well as any other name registered with
 |      codecs.register_error that is able to handle UnicodeEncodeErrors.
 |  
 |  endswith(...)
 |      S.endswith(suffix[, start[, end]]) -> bool
 |      
 |      Return True if S ends with the specified suffix, False otherwise.
 |      With optional start, test S beginning at that position.
 |      With optional end, stop comparing S at that position.
 |      suffix can also be a tuple of strings to try.
 |  
 |  expandtabs(...)
 |      S.expandtabs([tabsize]) -> string
 |      
 |      Return a copy of S where all tab characters are expanded using spaces.
 |      If tabsize is not given, a tab size of 8 characters is assumed.
 |  
 |  find(...)
 |      S.find(sub [,start [,end]]) -> int
 |      
 |      Return the lowest index in S where substring sub is found,
 |      such that sub is contained within S[start:end].  Optional
 |      arguments start and end are interpreted as in slice notation.
 |      
 |      Return -1 on failure.
 |  
 |  format(...)
 |      S.format(*args, **kwargs) -> string
 |      
 |      Return a formatted version of S, using substitutions from args and kwargs.
 |      The substitutions are identified by braces ('{' and '}').
 |  
 |  index(...)
 |      S.index(sub [,start [,end]]) -> int
 |      
 |      Like S.find() but raise ValueError when the substring is not found.
 |  
 |  isalnum(...)
 |      S.isalnum() -> bool
 |      
 |      Return True if all characters in S are alphanumeric
 |      and there is at least one character in S, False otherwise.
 |  
 |  isalpha(...)
 |      S.isalpha() -> bool
 |      
 |      Return True if all characters in S are alphabetic
 |      and there is at least one character in S, False otherwise.
 |  
 |  isdigit(...)
 |      S.isdigit() -> bool
 |      
 |      Return True if all characters in S are digits
 |      and there is at least one character in S, False otherwise.
 |  
 |  islower(...)
 |      S.islower() -> bool
 |      
 |      Return True if all cased characters in S are lowercase and there is
 |      at least one cased character in S, False otherwise.
 |  
 |  isspace(...)
 |      S.isspace() -> bool
 |      
 |      Return True if all characters in S are whitespace
 |      and there is at least one character in S, False otherwise.
 |  
 |  istitle(...)
 |      S.istitle() -> bool
 |      
 |      Return True if S is a titlecased string and there is at least one
 |      character in S, i.e. uppercase characters may only follow uncased
 |      characters and lowercase characters only cased ones. Return False
 |      otherwise.
 |  
 |  isupper(...)
 |      S.isupper() -> bool
 |      
 |      Return True if all cased characters in S are uppercase and there is
 |      at least one cased character in S, False otherwise.
 |  
 |  join(...)
 |      S.join(iterable) -> string
 |      
 |      Return a string which is the concatenation of the strings in the
 |      iterable.  The separator between elements is S.
 |  
 |  ljust(...)
 |      S.ljust(width[, fillchar]) -> string
 |      
 |      Return S left-justified in a string of length width. Padding is
 |      done using the specified fill character (default is a space).
 |  
 |  lower(...)
 |      S.lower() -> string
 |      
 |      Return a copy of the string S converted to lowercase.
 |  
 |  lstrip(...)
 |      S.lstrip([chars]) -> string or unicode
 |      
 |      Return a copy of the string S with leading whitespace removed.
 |      If chars is given and not None, remove characters in chars instead.
 |      If chars is unicode, S will be converted to unicode before stripping
 |  
 |  partition(...)
 |      S.partition(sep) -> (head, sep, tail)
 |      
 |      Search for the separator sep in S, and return the part before it,
 |      the separator itself, and the part after it.  If the separator is not
 |      found, return S and two empty strings.
 |  
 |  replace(...)
 |      S.replace(old, new[, count]) -> string
 |      
 |      Return a copy of string S with all occurrences of substring
 |      old replaced by new.  If the optional argument count is
 |      given, only the first count occurrences are replaced.
 |  
 |  rfind(...)
 |      S.rfind(sub [,start [,end]]) -> int
 |      
 |      Return the highest index in S where substring sub is found,
 |      such that sub is contained within S[start:end].  Optional
 |      arguments start and end are interpreted as in slice notation.
 |      
 |      Return -1 on failure.
 |  
 |  rindex(...)
 |      S.rindex(sub [,start [,end]]) -> int
 |      
 |      Like S.rfind() but raise ValueError when the substring is not found.
 |  
 |  rjust(...)
 |      S.rjust(width[, fillchar]) -> string
 |      
 |      Return S right-justified in a string of length width. Padding is
 |      done using the specified fill character (default is a space)
 |  
 |  rpartition(...)
 |      S.rpartition(sep) -> (head, sep, tail)
 |      
 |      Search for the separator sep in S, starting at the end of S, and return
 |      the part before it, the separator itself, and the part after it.  If the
 |      separator is not found, return two empty strings and S.
 |  
 |  rsplit(...)
 |      S.rsplit([sep [,maxsplit]]) -> list of strings
 |      
 |      Return a list of the words in the string S, using sep as the
 |      delimiter string, starting at the end of the string and working
 |      to the front.  If maxsplit is given, at most maxsplit splits are
 |      done. If sep is not specified or is None, any whitespace string
 |      is a separator.
 |  
 |  rstrip(...)
 |      S.rstrip([chars]) -> string or unicode
 |      
 |      Return a copy of the string S with trailing whitespace removed.
 |      If chars is given and not None, remove characters in chars instead.
 |      If chars is unicode, S will be converted to unicode before stripping
 |  
 |  split(...)
 |      S.split([sep [,maxsplit]]) -> list of strings
 |      
 |      Return a list of the words in the string S, using sep as the
 |      delimiter string.  If maxsplit is given, at most maxsplit
 |      splits are done. If sep is not specified or is None, any
 |      whitespace string is a separator and empty strings are removed
 |      from the result.
 |  
 |  splitlines(...)
 |      S.splitlines([keepends]) -> list of strings
 |      
 |      Return a list of the lines in S, breaking at line boundaries.
 |      Line breaks are not included in the resulting list unless keepends
 |      is given and true.
 |  
 |  startswith(...)
 |      S.startswith(prefix[, start[, end]]) -> bool
 |      
 |      Return True if S starts with the specified prefix, False otherwise.
 |      With optional start, test S beginning at that position.
 |      With optional end, stop comparing S at that position.
 |      prefix can also be a tuple of strings to try.
 |  
 |  strip(...)
 |      S.strip([chars]) -> string or unicode
 |      
 |      Return a copy of the string S with leading and trailing
 |      whitespace removed.
 |      If chars is given and not None, remove characters in chars instead.
 |      If chars is unicode, S will be converted to unicode before stripping
 |  
 |  swapcase(...)
 |      S.swapcase() -> string
 |      
 |      Return a copy of the string S with uppercase characters
 |      converted to lowercase and vice versa.
 |  
 |  title(...)
 |      S.title() -> string
 |      
 |      Return a titlecased version of S, i.e. words start with uppercase
 |      characters, all remaining cased characters have lowercase.
 |  
 |  translate(...)
 |      S.translate(table [,deletechars]) -> string
 |      
 |      Return a copy of the string S, where all characters occurring
 |      in the optional argument deletechars are removed, and the
 |      remaining characters have been mapped through the given
 |      translation table, which must be a string of length 256 or None.
 |      If the table argument is None, no translation is applied and
 |      the operation simply removes the characters in deletechars.
 |  
 |  upper(...)
 |      S.upper() -> string
 |      
 |      Return a copy of the string S converted to uppercase.
 |  
 |  zfill(...)
 |      S.zfill(width) -> string
 |      
 |      Pad a numeric string S with zeros on the left, to fill a field
 |      of the specified width.  The string S is never truncated.
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __new__ = <built-in method __new__ of type object>
 |      T.__new__(S, ...) -> a new object with type S, a subtype of T
 
 /////////////////////////////////////////////////////////////////////////////////
 List
 
class list(object)
 |  list() -> new empty list
 |  list(iterable) -> new list initialized from iterable's items
 |  
 |  Methods defined here:
 |  
 |  __add__(...)
 |      x.__add__(y) <==> x+y
 |  
 |  __contains__(...)
 |      x.__contains__(y) <==> y in x
 |  
 |  __delitem__(...)
 |      x.__delitem__(y) <==> del x[y]
 |  
 |  __delslice__(...)
 |      x.__delslice__(i, j) <==> del x[i:j]
 |      
 |      Use of negative indices is not supported.
 |  
 |  __eq__(...)
 |      x.__eq__(y) <==> x==y
 |  
 |  __ge__(...)
 |      x.__ge__(y) <==> x>=y
 |  
 |  __getattribute__(...)
 |      x.__getattribute__('name') <==> x.name
 |  
 |  __getitem__(...)
 |      x.__getitem__(y) <==> x[y]
 |  
 |  __getslice__(...)
 |      x.__getslice__(i, j) <==> x[i:j]
 |      
 |      Use of negative indices is not supported.
 |  
 |  __gt__(...)
 |      x.__gt__(y) <==> x>y
 |  
 |  __iadd__(...)
 |      x.__iadd__(y) <==> x+=y
 |  
 |  __imul__(...)
 |      x.__imul__(y) <==> x*=y
 |  
 |  __init__(...)
 |      x.__init__(...) initializes x; see help(type(x)) for signature
 |  
 |  __iter__(...)
 |      x.__iter__() <==> iter(x)
 |  
 |  __le__(...)
 |      x.__le__(y) <==> x<=y
 |  
 |  __len__(...)
 |      x.__len__() <==> len(x)
 |  
 |  __lt__(...)
 |      x.__lt__(y) <==> x<y
 |  
 |  __mul__(...)
 |      x.__mul__(n) <==> x*n
 |  
 |  __ne__(...)
 |      x.__ne__(y) <==> x!=y
 |  
 |  __repr__(...)
 |      x.__repr__() <==> repr(x)
 |  
 |  __reversed__(...)
 |      L.__reversed__() -- return a reverse iterator over the list
 |  
 |  __rmul__(...)
 |      x.__rmul__(n) <==> n*x
 |  
 |  __setitem__(...)
 |      x.__setitem__(i, y) <==> x[i]=y
 |  
 |  __setslice__(...)
 |      x.__setslice__(i, j, y) <==> x[i:j]=y
 |      
 |      Use  of negative indices is not supported.
 |  
 |  __sizeof__(...)
 |      L.__sizeof__() -- size of L in memory, in bytes
 |  
 |  append(...)
 |      L.append(object) -- append object to end
 |  
 |  count(...)
 |      L.count(value) -> integer -- return number of occurrences of value
 |  
 |  extend(...)
 |      L.extend(iterable) -- extend list by appending elements from the iterable
 |  
 |  index(...)
 |      L.index(value, [start, [stop]]) -> integer -- return first index of value.
 |      Raises ValueError if the value is not present.
 |  
 |  insert(...)
 |      L.insert(index, object) -- insert object before index
 |  
 |  pop(...)
 |      L.pop([index]) -> item -- remove and return item at index (default last).
 |      Raises IndexError if list is empty or index is out of range.
 |  
 |  remove(...)
 |      L.remove(value) -- remove first occurrence of value.
 |      Raises ValueError if the value is not present.
 |  
 |  reverse(...)
 |      L.reverse() -- reverse *IN PLACE*
 |  
 |  sort(...)
 |      L.sort(cmp=None, key=None, reverse=False) -- stable sort *IN PLACE*;
 |      cmp(x, y) -> -1, 0, 1
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __hash__ = None
 |  
 |  __new__ = <built-in method __new__ of type object>
 |      T.__new__(S, ...) -> a new object with type S, a subtype of T
 
 ////////////////////////////////////////////////////////////////////////////////////
 Dictionary
 class dict(object)
 |  dict() -> new empty dictionary
 |  dict(mapping) -> new dictionary initialized from a mapping object's
 |      (key, value) pairs
 |  dict(iterable) -> new dictionary initialized as if via:
 |      d = {}
 |      for k, v in iterable:
 |          d[k] = v
 |  dict(**kwargs) -> new dictionary initialized with the name=value pairs
 |      in the keyword argument list.  For example:  dict(one=1, two=2)
 |  
 |  Methods defined here:
 |  
 |  __cmp__(...)
 |      x.__cmp__(y) <==> cmp(x,y)
 |  
 |  __contains__(...)
 |      D.__contains__(k) -> True if D has a key k, else False
 |  
 |  __delitem__(...)
 |      x.__delitem__(y) <==> del x[y]
 |  
 |  __eq__(...)
 |      x.__eq__(y) <==> x==y
 |  
 |  __ge__(...)
 |      x.__ge__(y) <==> x>=y
 |  
 |  __getattribute__(...)
 |      x.__getattribute__('name') <==> x.name
 |  
 |  __getitem__(...)
 |      x.__getitem__(y) <==> x[y]
 |  
 |  __gt__(...)
 |      x.__gt__(y) <==> x>y
 |  
 |  __init__(...)
 |      x.__init__(...) initializes x; see help(type(x)) for signature
 |  
 |  __iter__(...)
 |      x.__iter__() <==> iter(x)
 |  
 |  __le__(...)
 |      x.__le__(y) <==> x<=y
 |  
 |  __len__(...)
 |      x.__len__() <==> len(x)
 |  
 |  __lt__(...)
 |      x.__lt__(y) <==> x<y
 |  
 |  __ne__(...)
 |      x.__ne__(y) <==> x!=y
 |  
 |  __repr__(...)
 |      x.__repr__() <==> repr(x)
 |  
 |  __setitem__(...)
 |      x.__setitem__(i, y) <==> x[i]=y
 |  
 |  __sizeof__(...)
 |      D.__sizeof__() -> size of D in memory, in bytes
 |  
 |  clear(...)
 |      D.clear() -> None.  Remove all items from D.
 |  
 |  copy(...)
 |      D.copy() -> a shallow copy of D
 |  
 |  fromkeys(...)
 |      dict.fromkeys(S[,v]) -> New dict with keys from S and values equal to v.
 |      v defaults to None.
 |  
 |  get(...)
 |      D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None.
 |  
 |  has_key(...)
 |      D.has_key(k) -> True if D has a key k, else False
 |  
 |  items(...)
 |      D.items() -> list of D's (key, value) pairs, as 2-tuples
 |  
 |  iteritems(...)
 |      D.iteritems() -> an iterator over the (key, value) items of D
 |  
 |  iterkeys(...)
 |      D.iterkeys() -> an iterator over the keys of D
 |  
 |  itervalues(...)
 |      D.itervalues() -> an iterator over the values of D
 |  
 |  keys(...)
 |      D.keys() -> list of D's keys
 |  
 |  pop(...)
 |      D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
 |      If key is not found, d is returned if given, otherwise KeyError is raised
 |  
 |  popitem(...)
 |      D.popitem() -> (k, v), remove and return some (key, value) pair as a
 |      2-tuple; but raise KeyError if D is empty.
 |  
 |  setdefault(...)
 |      D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D
 |  
 |  update(...)
 |      D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.
 |      If E present and has a .keys() method, does:     for k in E: D[k] = E[k]
 |      If E present and lacks .keys() method, does:     for (k, v) in E: D[k] = v
 |      In either case, this is followed by: for k in F: D[k] = F[k]
 |  
 |  values(...)
 |      D.values() -> list of D's values
 |  
 |  viewitems(...)
 |      D.viewitems() -> a set-like object providing a view on D's items
 |  
 |  viewkeys(...)
 |      D.viewkeys() -> a set-like object providing a view on D's keys
 |  
 |  viewvalues(...)
 |      D.viewvalues() -> an object providing a view on D's values
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __hash__ = None
 |  
 |  __new__ = <built-in method __new__ of type object>
 |      T.__new__(S, ...) -> a new object with type S, a subtype of T
 
 ///////////////////////////////////////////////////////////////////////////////
NAME
    math

FILE
    (built-in)

DESCRIPTION
    This module is always available.  It provides access to the
    mathematical functions defined by the C standard.

FUNCTIONS
    acos(...)
        acos(x)
        
        Return the arc cosine (measured in radians) of x.
    
    acosh(...)
        acosh(x)
        
        Return the hyperbolic arc cosine (measured in radians) of x.
    
    asin(...)
        asin(x)
        
        Return the arc sine (measured in radians) of x.
    
    asinh(...)
        asinh(x)
        
        Return the hyperbolic arc sine (measured in radians) of x.
    
    atan(...)
        atan(x)
        
        Return the arc tangent (measured in radians) of x.
    
    atan2(...)
        atan2(y, x)
        
        Return the arc tangent (measured in radians) of y/x.
        Unlike atan(y/x), the signs of both x and y are considered.
    
    atanh(...)
        atanh(x)
        
        Return the hyperbolic arc tangent (measured in radians) of x.
    
    ceil(...)
        ceil(x)
        
        Return the ceiling of x as a float.
        This is the smallest integral value >= x.
    
    copysign(...)
        copysign(x, y)
        
        Return x with the sign of y.
    
    cos(...)
        cos(x)
        
        Return the cosine of x (measured in radians).
    
    cosh(...)
        cosh(x)
        
        Return the hyperbolic cosine of x.
    
    degrees(...)
        degrees(x)
        
        Convert angle x from radians to degrees.
    
    erf(...)
        erf(x)
        
        Error function at x.
    
    erfc(...)
        erfc(x)
        
        Complementary error function at x.
    
    exp(...)
        exp(x)
        
        Return e raised to the power of x.
    
    expm1(...)
        expm1(x)
        
        Return exp(x)-1.
        This function avoids the loss of precision involved in the direct evaluation of exp(x)-1 for small x.
    
    fabs(...)
        fabs(x)
        
        Return the absolute value of the float x.
    
    factorial(...)
        factorial(x) -> Integral
        
        Find x!. Raise a ValueError if x is negative or non-integral.
    
    floor(...)
        floor(x)
        
        Return the floor of x as a float.
        This is the largest integral value <= x.
    
    fmod(...)
        fmod(x, y)
        
        Return fmod(x, y), according to platform C.  x % y may differ.
    
    frexp(...)
        frexp(x)
        
        Return the mantissa and exponent of x, as pair (m, e).
        m is a float and e is an int, such that x = m * 2.**e.
        If x is 0, m and e are both 0.  Else 0.5 <= abs(m) < 1.0.
    
    fsum(...)
        fsum(iterable)
        
        Return an accurate floating point sum of values in the iterable.
        Assumes IEEE-754 floating point arithmetic.
    
    gamma(...)
        gamma(x)
        
        Gamma function at x.
    
    hypot(...)
        hypot(x, y)
        
        Return the Euclidean distance, sqrt(x*x + y*y).
    
    isinf(...)
        isinf(x) -> bool
        
        Check if float x is infinite (positive or negative).
    
    isnan(...)
        isnan(x) -> bool
        
        Check if float x is not a number (NaN).
    
    ldexp(...)
        ldexp(x, i)
        
        Return x * (2**i).
    
    lgamma(...)
        lgamma(x)
        
        Natural logarithm of absolute value of Gamma function at x.
    
    log(...)
        log(x[, base])
        
        Return the logarithm of x to the given base.
        If the base not specified, returns the natural logarithm (base e) of x.
    
    log10(...)
        log10(x)
        
        Return the base 10 logarithm of x.
    
    log1p(...)
        log1p(x)
        
        Return the natural logarithm of 1+x (base e).
        The result is computed in a way which is accurate for x near zero.
    
    modf(...)
        modf(x)
        
        Return the fractional and integer parts of x.  Both results carry the sign
        of x and are floats.
    
    pow(...)
        pow(x, y)
        
        Return x**y (x to the power of y).
    
    radians(...)
        radians(x)
        
        Convert angle x from degrees to radians.
    
    sin(...)
        sin(x)
        
        Return the sine of x (measured in radians).
    
    sinh(...)
        sinh(x)
        
        Return the hyperbolic sine of x.
    
    sqrt(...)
        sqrt(x)
        
        Return the square root of x.
    
    tan(...)
        tan(x)
        
        Return the tangent of x (measured in radians).
    
    tanh(...)
        tanh(x)
        
        Return the hyperbolic tangent of x.
    
    trunc(...)
        trunc(x:Real) -> Integral
        
        Truncates x to the nearest Integral toward 0. Uses the __trunc__ magic method.

DATA
    e = 2.718281828459045
    pi = 3.141592653589793

 //////////////////////////////////////////////////////////////////////////////////////
 class tuple(object)
 |  tuple() -> empty tuple
 |  tuple(iterable) -> tuple initialized from iterable's items
 |  
 |  If the argument is a tuple, the return value is the same object.
 |  
 |  Methods defined here:
 |  
 |  __add__(...)
 |      x.__add__(y) <==> x+y
 |  
 |  __contains__(...)
 |      x.__contains__(y) <==> y in x
 |  
 |  __eq__(...)
 |      x.__eq__(y) <==> x==y
 |  
 |  __ge__(...)
 |      x.__ge__(y) <==> x>=y
 |  
 |  __getattribute__(...)
 |      x.__getattribute__('name') <==> x.name
 |  
 |  __getitem__(...)
 |      x.__getitem__(y) <==> x[y]
 |  
 |  __getnewargs__(...)
 |  
 |  __getslice__(...)
 |      x.__getslice__(i, j) <==> x[i:j]
 |      
 |      Use of negative indices is not supported.
 |  
 |  __gt__(...)
 |      x.__gt__(y) <==> x>y
 |  
 |  __hash__(...)
 |      x.__hash__() <==> hash(x)
 |  
 |  __iter__(...)
 |      x.__iter__() <==> iter(x)
 |  
 |  __le__(...)
 |      x.__le__(y) <==> x<=y
 |  
 |  __len__(...)
 |      x.__len__() <==> len(x)
 |  
 |  __lt__(...)
 |      x.__lt__(y) <==> x<y
 |  
 |  __mul__(...)
 |      x.__mul__(n) <==> x*n
 |  
 |  __ne__(...)
 |      x.__ne__(y) <==> x!=y
 |  
 |  __repr__(...)
 |      x.__repr__() <==> repr(x)
 |  
 |  __rmul__(...)
 |      x.__rmul__(n) <==> n*x
 |  
 |  __sizeof__(...)
 |      T.__sizeof__() -- size of T in memory, in bytes
 |  
 |  count(...)
 |      T.count(value) -> integer -- return number of occurrences of value
 |  
 |  index(...)
 |      T.index(value, [start, [stop]]) -> integer -- return first index of value.
 |      Raises ValueError if the value is not present.
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __new__ = <built-in method __new__ of type object>
 |      T.__new__(S, ...) -> a new object with type S, a subtype of T
 ////////////////////////////////////////////////////////////////////////////////////
 NAME
    random - Random variable generators.

FILE
    c:\python27\lib\random.py

DESCRIPTION
        integers
        --------
               uniform within range
    
        sequences
        ---------
               pick random element
               pick random sample
               generate random permutation
    
        distributions on the real line:
        ------------------------------
               uniform
               triangular
               normal (Gaussian)
               lognormal
               negative exponential
               gamma
               beta
               pareto
               Weibull
    
        distributions on the circle (angles 0 to 2pi)
        ---------------------------------------------
               circular uniform
               von Mises
    
    General notes on the underlying Mersenne Twister core generator:
    
    * The period is 2**19937-1.
    * It is one of the most extensively tested generators in existence.
    * Without a direct way to compute N steps forward, the semantics of
      jumpahead(n) are weakened to simply jump to another distant state and rely
      on the large period to avoid overlapping sequences.
    * The random() method is implemented in C, executes in a single Python step,
      and is, therefore, threadsafe.

CLASSES
    _random.Random(__builtin__.object)
        Random
            SystemRandom
            WichmannHill
    
    class Random(_random.Random)
     |  Random number generator base class used by bound module functions.
     |  
     |  Used to instantiate instances of Random to get generators that don't
     |  share state.  Especially useful for multi-threaded programs, creating
     |  a different instance of Random for each thread, and using the jumpahead()
     |  method to ensure that the generated sequences seen by each thread don't
     |  overlap.
     |  
     |  Class Random can also be subclassed if you want to use a different basic
     |  generator of your own devising: in that case, override the following
     |  methods: random(), seed(), getstate(), setstate() and jumpahead().
     |  Optionally, implement a getrandbits() method so that randrange() can cover
     |  arbitrarily large ranges.
     |  
     |  Method resolution order:
     |      Random
     |      _random.Random
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __getstate__(self)
     |  
     |  __init__(self, x=None)
     |      Initialize an instance.
     |      
     |      Optional argument x controls seeding, as for Random.seed().
     |  
     |  __reduce__(self)
     |  
     |  __setstate__(self, state)
     |  
     |  betavariate(self, alpha, beta)
     |      Beta distribution.
     |      
     |      Conditions on the parameters are alpha > 0 and beta > 0.
     |      Returned values range between 0 and 1.
     |  
     |  choice(self, seq)
     |      Choose a random element from a non-empty sequence.
     |  
     |  expovariate(self, lambd)
     |      Exponential distribution.
     |      
     |      lambd is 1.0 divided by the desired mean.  It should be
     |      nonzero.  (The parameter would be called "lambda", but that is
     |      a reserved word in Python.)  Returned values range from 0 to
     |      positive infinity if lambd is positive, and from negative
     |      infinity to 0 if lambd is negative.
     |  
     |  gammavariate(self, alpha, beta)
     |      Gamma distribution.  Not the gamma function!
     |      
     |      Conditions on the parameters are alpha > 0 and beta > 0.
     |      
     |      The probability distribution function is:
     |      
     |                  x ** (alpha - 1) * math.exp(-x / beta)
     |        pdf(x) =  --------------------------------------
     |                    math.gamma(alpha) * beta ** alpha
     |  
     |  gauss(self, mu, sigma)
     |      Gaussian distribution.
     |      
     |      mu is the mean, and sigma is the standard deviation.  This is
     |      slightly faster than the normalvariate() function.
     |      
     |      Not thread-safe without a lock around calls.
     |  
     |  getstate(self)
     |      Return internal state; can be passed to setstate() later.
     |  
     |  jumpahead(self, n)
     |      Change the internal state to one that is likely far away
     |      from the current state.  This method will not be in Py3.x,
     |      so it is better to simply reseed.
     |  
     |  lognormvariate(self, mu, sigma)
     |      Log normal distribution.
     |      
     |      If you take the natural logarithm of this distribution, you'll get a
     |      normal distribution with mean mu and standard deviation sigma.
     |      mu can have any value, and sigma must be greater than zero.
     |  
     |  normalvariate(self, mu, sigma)
     |      Normal distribution.
     |      
     |      mu is the mean, and sigma is the standard deviation.
     |  
     |  paretovariate(self, alpha)
     |      Pareto distribution.  alpha is the shape parameter.
     |  
     |  randint(self, a, b)
     |      Return random integer in range [a, b], including both end points.
     |  
     |  randrange(self, start, stop=None, step=1, int=<type 'int'>, default=None, maxwidth=9007199254740992L)
     |      Choose a random item from range(start, stop[, step]).
     |      
     |      This fixes the problem with randint() which includes the
     |      endpoint; in Python this is usually not what you want.
     |      Do not supply the 'int', 'default', and 'maxwidth' arguments.
     |  
     |  sample(self, population, k)
     |      Chooses k unique random elements from a population sequence.
     |      
     |      Returns a new list containing elements from the population while
     |      leaving the original population unchanged.  The resulting list is
     |      in selection order so that all sub-slices will also be valid random
     |      samples.  This allows raffle winners (the sample) to be partitioned
     |      into grand prize and second place winners (the subslices).
     |      
     |      Members of the population need not be hashable or unique.  If the
     |      population contains repeats, then each occurrence is a possible
     |      selection in the sample.
     |      
     |      To choose a sample in a range of integers, use xrange as an argument.
     |      This is especially fast and space efficient for sampling from a
     |      large population:   sample(xrange(10000000), 60)
     |  
     |  seed(self, a=None)
     |      Initialize internal state from hashable object.
     |      
     |      None or no argument seeds from current time or from an operating
     |      system specific randomness source if available.
     |      
     |      If a is not None or an int or long, hash(a) is used instead.
     |  
     |  setstate(self, state)
     |      Restore internal state from object returned by getstate().
     |  
     |  shuffle(self, x, random=None, int=<type 'int'>)
     |      x, random=random.random -> shuffle list x in place; return None.
     |      
     |      Optional arg random is a 0-argument function returning a random
     |      float in [0.0, 1.0); by default, the standard random.random.
     |  
     |  triangular(self, low=0.0, high=1.0, mode=None)
     |      Triangular distribution.
     |      
     |      Continuous distribution bounded by given lower and upper limits,
     |      and having a given mode value in-between.
     |      
     |      http://en.wikipedia.org/wiki/Triangular_distribution
     |  
     |  uniform(self, a, b)
     |      Get a random number in the range [a, b) or [a, b] depending on rounding.
     |  
     |  vonmisesvariate(self, mu, kappa)
     |      Circular data distribution.
     |      
     |      mu is the mean angle, expressed in radians between 0 and 2*pi, and
     |      kappa is the concentration parameter, which must be greater than or
     |      equal to zero.  If kappa is equal to zero, this distribution reduces
     |      to a uniform random angle over the range 0 to 2*pi.
     |  
     |  weibullvariate(self, alpha, beta)
     |      Weibull distribution.
     |      
     |      alpha is the scale parameter and beta is the shape parameter.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  VERSION = 3
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from _random.Random:
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  getrandbits(...)
     |      getrandbits(k) -> x.  Generates a long int with k random bits.
     |  
     |  random(...)
     |      random() -> x in the interval [0, 1).
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from _random.Random:
     |  
     |  __new__ = <built-in method __new__ of type object>
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class SystemRandom(Random)
     |  Alternate random number generator using sources provided
     |  by the operating system (such as /dev/urandom on Unix or
     |  CryptGenRandom on Windows).
     |  
     |   Not available on all systems (see os.urandom() for details).
     |  
     |  Method resolution order:
     |      SystemRandom
     |      Random
     |      _random.Random
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  getrandbits(self, k)
     |      getrandbits(k) -> x.  Generates a long int with k random bits.
     |  
     |  getstate = _notimplemented(self, *args, **kwds)
     |  
     |  jumpahead = _stub(self, *args, **kwds)
     |  
     |  random(self)
     |      Get the next random number in the range [0.0, 1.0).
     |  
     |  seed = _stub(self, *args, **kwds)
     |  
     |  setstate = _notimplemented(self, *args, **kwds)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from Random:
     |  
     |  __getstate__(self)
     |  
     |  __init__(self, x=None)
     |      Initialize an instance.
     |      
     |      Optional argument x controls seeding, as for Random.seed().
     |  
     |  __reduce__(self)
     |  
     |  __setstate__(self, state)
     |  
     |  betavariate(self, alpha, beta)
     |      Beta distribution.
     |      
     |      Conditions on the parameters are alpha > 0 and beta > 0.
     |      Returned values range between 0 and 1.
     |  
     |  choice(self, seq)
     |      Choose a random element from a non-empty sequence.
     |  
     |  expovariate(self, lambd)
     |      Exponential distribution.
     |      
     |      lambd is 1.0 divided by the desired mean.  It should be
     |      nonzero.  (The parameter would be called "lambda", but that is
     |      a reserved word in Python.)  Returned values range from 0 to
     |      positive infinity if lambd is positive, and from negative
     |      infinity to 0 if lambd is negative.
     |  
     |  gammavariate(self, alpha, beta)
     |      Gamma distribution.  Not the gamma function!
     |      
     |      Conditions on the parameters are alpha > 0 and beta > 0.
     |      
     |      The probability distribution function is:
     |      
     |                  x ** (alpha - 1) * math.exp(-x / beta)
     |        pdf(x) =  --------------------------------------
     |                    math.gamma(alpha) * beta ** alpha
     |  
     |  gauss(self, mu, sigma)
     |      Gaussian distribution.
     |      
     |      mu is the mean, and sigma is the standard deviation.  This is
     |      slightly faster than the normalvariate() function.
     |      
     |      Not thread-safe without a lock around calls.
     |  
     |  lognormvariate(self, mu, sigma)
     |      Log normal distribution.
     |      
     |      If you take the natural logarithm of this distribution, you'll get a
     |      normal distribution with mean mu and standard deviation sigma.
     |      mu can have any value, and sigma must be greater than zero.
     |  
     |  normalvariate(self, mu, sigma)
     |      Normal distribution.
     |      
     |      mu is the mean, and sigma is the standard deviation.
     |  
     |  paretovariate(self, alpha)
     |      Pareto distribution.  alpha is the shape parameter.
     |  
     |  randint(self, a, b)
     |      Return random integer in range [a, b], including both end points.
     |  
     |  randrange(self, start, stop=None, step=1, int=<type 'int'>, default=None, maxwidth=9007199254740992L)
     |      Choose a random item from range(start, stop[, step]).
     |      
     |      This fixes the problem with randint() which includes the
     |      endpoint; in Python this is usually not what you want.
     |      Do not supply the 'int', 'default', and 'maxwidth' arguments.
     |  
     |  sample(self, population, k)
     |      Chooses k unique random elements from a population sequence.
     |      
     |      Returns a new list containing elements from the population while
     |      leaving the original population unchanged.  The resulting list is
     |      in selection order so that all sub-slices will also be valid random
     |      samples.  This allows raffle winners (the sample) to be partitioned
     |      into grand prize and second place winners (the subslices).
     |      
     |      Members of the population need not be hashable or unique.  If the
     |      population contains repeats, then each occurrence is a possible
     |      selection in the sample.
     |      
     |      To choose a sample in a range of integers, use xrange as an argument.
     |      This is especially fast and space efficient for sampling from a
     |      large population:   sample(xrange(10000000), 60)
     |  
     |  shuffle(self, x, random=None, int=<type 'int'>)
     |      x, random=random.random -> shuffle list x in place; return None.
     |      
     |      Optional arg random is a 0-argument function returning a random
     |      float in [0.0, 1.0); by default, the standard random.random.
     |  
     |  triangular(self, low=0.0, high=1.0, mode=None)
     |      Triangular distribution.
     |      
     |      Continuous distribution bounded by given lower and upper limits,
     |      and having a given mode value in-between.
     |      
     |      http://en.wikipedia.org/wiki/Triangular_distribution
     |  
     |  uniform(self, a, b)
     |      Get a random number in the range [a, b) or [a, b] depending on rounding.
     |  
     |  vonmisesvariate(self, mu, kappa)
     |      Circular data distribution.
     |      
     |      mu is the mean angle, expressed in radians between 0 and 2*pi, and
     |      kappa is the concentration parameter, which must be greater than or
     |      equal to zero.  If kappa is equal to zero, this distribution reduces
     |      to a uniform random angle over the range 0 to 2*pi.
     |  
     |  weibullvariate(self, alpha, beta)
     |      Weibull distribution.
     |      
     |      alpha is the scale parameter and beta is the shape parameter.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from Random:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from Random:
     |  
     |  VERSION = 3
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from _random.Random:
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from _random.Random:
     |  
     |  __new__ = <built-in method __new__ of type object>
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class WichmannHill(Random)
     |  Method resolution order:
     |      WichmannHill
     |      Random
     |      _random.Random
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  getstate(self)
     |      Return internal state; can be passed to setstate() later.
     |  
     |  jumpahead(self, n)
     |      Act as if n calls to random() were made, but quickly.
     |      
     |      n is an int, greater than or equal to 0.
     |      
     |      Example use:  If you have 2 threads and know that each will
     |      consume no more than a million random numbers, create two Random
     |      objects r1 and r2, then do
     |          r2.setstate(r1.getstate())
     |          r2.jumpahead(1000000)
     |      Then r1 and r2 will use guaranteed-disjoint segments of the full
     |      period.
     |  
     |  random(self)
     |      Get the next random number in the range [0.0, 1.0).
     |  
     |  seed(self, a=None)
     |      Initialize internal state from hashable object.
     |      
     |      None or no argument seeds from current time or from an operating
     |      system specific randomness source if available.
     |      
     |      If a is not None or an int or long, hash(a) is used instead.
     |      
     |      If a is an int or long, a is used directly.  Distinct values between
     |      0 and 27814431486575L inclusive are guaranteed to yield distinct
     |      internal states (this guarantee is specific to the default
     |      Wichmann-Hill generator).
     |  
     |  setstate(self, state)
     |      Restore internal state from object returned by getstate().
     |  
     |  whseed(self, a=None)
     |      Seed from hashable object's hash code.
     |      
     |      None or no argument seeds from current time.  It is not guaranteed
     |      that objects with distinct hash codes lead to distinct internal
     |      states.
     |      
     |      This is obsolete, provided for compatibility with the seed routine
     |      used prior to Python 2.1.  Use the .seed() method instead.
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  VERSION = 1
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from Random:
     |  
     |  __getstate__(self)
     |  
     |  __init__(self, x=None)
     |      Initialize an instance.
     |      
     |      Optional argument x controls seeding, as for Random.seed().
     |  
     |  __reduce__(self)
     |  
     |  __setstate__(self, state)
     |  
     |  betavariate(self, alpha, beta)
     |      Beta distribution.
     |      
     |      Conditions on the parameters are alpha > 0 and beta > 0.
     |      Returned values range between 0 and 1.
     |  
     |  choice(self, seq)
     |      Choose a random element from a non-empty sequence.
     |  
     |  expovariate(self, lambd)
     |      Exponential distribution.
     |      
     |      lambd is 1.0 divided by the desired mean.  It should be
     |      nonzero.  (The parameter would be called "lambda", but that is
     |      a reserved word in Python.)  Returned values range from 0 to
     |      positive infinity if lambd is positive, and from negative
     |      infinity to 0 if lambd is negative.
     |  
     |  gammavariate(self, alpha, beta)
     |      Gamma distribution.  Not the gamma function!
     |      
     |      Conditions on the parameters are alpha > 0 and beta > 0.
     |      
     |      The probability distribution function is:
     |      
     |                  x ** (alpha - 1) * math.exp(-x / beta)
     |        pdf(x) =  --------------------------------------
     |                    math.gamma(alpha) * beta ** alpha
     |  
     |  gauss(self, mu, sigma)
     |      Gaussian distribution.
     |      
     |      mu is the mean, and sigma is the standard deviation.  This is
     |      slightly faster than the normalvariate() function.
     |      
     |      Not thread-safe without a lock around calls.
     |  
     |  lognormvariate(self, mu, sigma)
     |      Log normal distribution.
     |      
     |      If you take the natural logarithm of this distribution, you'll get a
     |      normal distribution with mean mu and standard deviation sigma.
     |      mu can have any value, and sigma must be greater than zero.
     |  
     |  normalvariate(self, mu, sigma)
     |      Normal distribution.
     |      
     |      mu is the mean, and sigma is the standard deviation.
     |  
     |  paretovariate(self, alpha)
     |      Pareto distribution.  alpha is the shape parameter.
     |  
     |  randint(self, a, b)
     |      Return random integer in range [a, b], including both end points.
     |  
     |  randrange(self, start, stop=None, step=1, int=<type 'int'>, default=None, maxwidth=9007199254740992L)
     |      Choose a random item from range(start, stop[, step]).
     |      
     |      This fixes the problem with randint() which includes the
     |      endpoint; in Python this is usually not what you want.
     |      Do not supply the 'int', 'default', and 'maxwidth' arguments.
     |  
     |  sample(self, population, k)
     |      Chooses k unique random elements from a population sequence.
     |      
     |      Returns a new list containing elements from the population while
     |      leaving the original population unchanged.  The resulting list is
     |      in selection order so that all sub-slices will also be valid random
     |      samples.  This allows raffle winners (the sample) to be partitioned
     |      into grand prize and second place winners (the subslices).
     |      
     |      Members of the population need not be hashable or unique.  If the
     |      population contains repeats, then each occurrence is a possible
     |      selection in the sample.
     |      
     |      To choose a sample in a range of integers, use xrange as an argument.
     |      This is especially fast and space efficient for sampling from a
     |      large population:   sample(xrange(10000000), 60)
     |  
     |  shuffle(self, x, random=None, int=<type 'int'>)
     |      x, random=random.random -> shuffle list x in place; return None.
     |      
     |      Optional arg random is a 0-argument function returning a random
     |      float in [0.0, 1.0); by default, the standard random.random.
     |  
     |  triangular(self, low=0.0, high=1.0, mode=None)
     |      Triangular distribution.
     |      
     |      Continuous distribution bounded by given lower and upper limits,
     |      and having a given mode value in-between.
     |      
     |      http://en.wikipedia.org/wiki/Triangular_distribution
     |  
     |  uniform(self, a, b)
     |      Get a random number in the range [a, b) or [a, b] depending on rounding.
     |  
     |  vonmisesvariate(self, mu, kappa)
     |      Circular data distribution.
     |      
     |      mu is the mean angle, expressed in radians between 0 and 2*pi, and
     |      kappa is the concentration parameter, which must be greater than or
     |      equal to zero.  If kappa is equal to zero, this distribution reduces
     |      to a uniform random angle over the range 0 to 2*pi.
     |  
     |  weibullvariate(self, alpha, beta)
     |      Weibull distribution.
     |      
     |      alpha is the scale parameter and beta is the shape parameter.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from Random:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from _random.Random:
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  getrandbits(...)
     |      getrandbits(k) -> x.  Generates a long int with k random bits.
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from _random.Random:
     |  
     |  __new__ = <built-in method __new__ of type object>
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T

FUNCTIONS
    betavariate(self, alpha, beta) method of Random instance
        Beta distribution.
        
        Conditions on the parameters are alpha > 0 and beta > 0.
        Returned values range between 0 and 1.
    
    choice(self, seq) method of Random instance
        Choose a random element from a non-empty sequence.
    
    expovariate(self, lambd) method of Random instance
        Exponential distribution.
        
        lambd is 1.0 divided by the desired mean.  It should be
        nonzero.  (The parameter would be called "lambda", but that is
        a reserved word in Python.)  Returned values range from 0 to
        positive infinity if lambd is positive, and from negative
        infinity to 0 if lambd is negative.
    
    gammavariate(self, alpha, beta) method of Random instance
        Gamma distribution.  Not the gamma function!
        
        Conditions on the parameters are alpha > 0 and beta > 0.
        
        The probability distribution function is:
        
                    x ** (alpha - 1) * math.exp(-x / beta)
          pdf(x) =  --------------------------------------
                      math.gamma(alpha) * beta ** alpha
    
    gauss(self, mu, sigma) method of Random instance
        Gaussian distribution.
        
        mu is the mean, and sigma is the standard deviation.  This is
        slightly faster than the normalvariate() function.
        
        Not thread-safe without a lock around calls.
    
    getrandbits(...)
        getrandbits(k) -> x.  Generates a long int with k random bits.
    
    getstate(self) method of Random instance
        Return internal state; can be passed to setstate() later.
    
    jumpahead(self, n) method of Random instance
        Change the internal state to one that is likely far away
        from the current state.  This method will not be in Py3.x,
        so it is better to simply reseed.
    
    lognormvariate(self, mu, sigma) method of Random instance
        Log normal distribution.
        
        If you take the natural logarithm of this distribution, you'll get a
        normal distribution with mean mu and standard deviation sigma.
        mu can have any value, and sigma must be greater than zero.
    
    normalvariate(self, mu, sigma) method of Random instance
        Normal distribution.
        
        mu is the mean, and sigma is the standard deviation.
    
    paretovariate(self, alpha) method of Random instance
        Pareto distribution.  alpha is the shape parameter.
    
    randint(self, a, b) method of Random instance
        Return random integer in range [a, b], including both end points.
    
    random(...)
        random() -> x in the interval [0, 1).
    
    randrange(self, start, stop=None, step=1, int=<type 'int'>, default=None, maxwidth=9007199254740992L) method of Random instance
        Choose a random item from range(start, stop[, step]).
        
        This fixes the problem with randint() which includes the
        endpoint; in Python this is usually not what you want.
        Do not supply the 'int', 'default', and 'maxwidth' arguments.
    
    sample(self, population, k) method of Random instance
        Chooses k unique random elements from a population sequence.
        
        Returns a new list containing elements from the population while
        leaving the original population unchanged.  The resulting list is
        in selection order so that all sub-slices will also be valid random
        samples.  This allows raffle winners (the sample) to be partitioned
        into grand prize and second place winners (the subslices).
        
        Members of the population need not be hashable or unique.  If the
        population contains repeats, then each occurrence is a possible
        selection in the sample.
        
        To choose a sample in a range of integers, use xrange as an argument.
        This is especially fast and space efficient for sampling from a
        large population:   sample(xrange(10000000), 60)
    
    seed(self, a=None) method of Random instance
        Initialize internal state from hashable object.
        
        None or no argument seeds from current time or from an operating
        system specific randomness source if available.
        
        If a is not None or an int or long, hash(a) is used instead.
    
    setstate(self, state) method of Random instance
        Restore internal state from object returned by getstate().
    
    shuffle(self, x, random=None, int=<type 'int'>) method of Random instance
        x, random=random.random -> shuffle list x in place; return None.
        
        Optional arg random is a 0-argument function returning a random
        float in [0.0, 1.0); by default, the standard random.random.
    
    triangular(self, low=0.0, high=1.0, mode=None) method of Random instance
        Triangular distribution.
        
        Continuous distribution bounded by given lower and upper limits,
        and having a given mode value in-between.
        
        http://en.wikipedia.org/wiki/Triangular_distribution
    
    uniform(self, a, b) method of Random instance
        Get a random number in the range [a, b) or [a, b] depending on rounding.
    
    vonmisesvariate(self, mu, kappa) method of Random instance
        Circular data distribution.
        
        mu is the mean angle, expressed in radians between 0 and 2*pi, and
        kappa is the concentration parameter, which must be greater than or
        equal to zero.  If kappa is equal to zero, this distribution reduces
        to a uniform random angle over the range 0 to 2*pi.
    
    weibullvariate(self, alpha, beta) method of Random instance
        Weibull distribution.
        
        alpha is the scale parameter and beta is the shape parameter.

DATA
    __all__ = ['Random', 'seed', 'random', 'uniform', 'randint', 'choice',...

 

