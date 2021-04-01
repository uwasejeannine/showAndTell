Python 3.8.6 (default, Jan 27 2021, 15:42:20) 
[GCC 10.2.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> #python Valiables(INt,Float and Boolean)
>>> studentNumber=2 # variable number is 2
>>> print(studentNumber)
2
>>> #Oparetors(Arthemetic)
>>> x=2
>>> y=3
>>> y+x
5
>>> # Assignment Oparetors
>>> x+=2 # adding 2 two the value of x
>>> print(x)
4
>>> y-=1
>>> print(y)
2
>>> # relational oparetors
>>> # relational oparetors( relatang two value using different sign)
>>> x<b
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    x<b
NameError: name 'b' is not defined
>>> x<y
False
>>> x==y # it's returs boolean(True of False)
False
>>> # Datatype (int, float,boolean,complex, string,list...)
>>> c=2+3j # complex method return complex number when Imaginary and real nbr has provided
>>> print(c)
(2+3j)
>>> #String method are build in fuction to chance appearence of a string output
>>> firstName="mukagasaraba"
>>> secondName="rachel"
>>> country="rwanda"
>>> district="rusizi"
>>> lendMoney=200,000
>>> payedBack=50,000
>>>  currency="rwf"
 
SyntaxError: unexpected indent
>>> currency="rwf"
>>> print(f"Dear {firstName.capitalize()} {secondName.capitalize()} who is {2021-1978} years old from {country.upper()} in {district.title()}.We are extrimly excited to give you your remining {200000-5000} {currency.upper()}.")
Dear Mukagasaraba Rachel who is 43 years old from RWANDA in Rusizi.We are extrimly excited to give you your remining 195000 RWF.
>>> # datastrucure using a list(List can contain anything)
>>> foodList=["Bread","Cakes","Meat","Rolls"]
>>> foodList[2] # always index start from zero
'Meat'
>>> foodList[0:2]
['Bread', 'Cakes']
>>> foodList[-3:-1]
['Cakes', 'Meat']
>>> foodList.append("Marshmallow") # add value to the bottom of the list
>>>  foodList.insert(1,"beans") # insert value to between index specified
 
SyntaxError: unexpected indent
>>> foodList.insert(1,"beans") # insert value to between index specified
>>> foodList.extend(["sweet potatoes","millet "]) # add alist to the bottom of list
>>> foodList.remove("Meat")# removes last item in the list
>>> foodList.sort() # sort items in accending manner
>>> foodList.reverse() #reverse item last became first
>>> print(foodList)
['sweet potatoes', 'millet ', 'beans', 'Rolls', 'Marshmallow', 'Cakes', 'Bread']
>>> foodList.clrean() # delet items in the list
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    foodList.clrean() # delet items in the list
AttributeError: 'list' object has no attribute 'clrean'
>>> foodList.clear() # delet items in the list
>>> print(foodList)
[]
>>> list=[1, 3, 5, 7, 9]
>>> for i in list:
	a=i*2
	print(a)

	
2
6
10
14
18
>>> # getting length of list
>>> length = len(list)
>>> print(lenght)
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    print(lenght)
NameError: name 'lenght' is not defined
>>> print(length)
5
>>> # make a list from a nother list 
>>> a=[[1,2,3],[4,5,6],[7,8,9]]
>>> b=[]
>>> b=[e for sublist in a  for e in sublist]
>>> print(b)
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> 
