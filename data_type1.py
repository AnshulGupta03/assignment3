#Q.1- Create a list with user defined inputs. 

x1=input("enter first element of list")
x2=input("enter second element of list")
x3=input("enter third element of list")
my_list=[x1,x2,x3]
print(my_list,"\n\n")
print(10*"*")


#Q.2- Add the following list to above created list:[‘google’,’apple’,’facebook’,’microsoft’,’tesla’]

list2=['google','apple','facebook','microsoft','tesla']
my_list=my_list+list2
print(my_list,"\n\n")
print(10*"*")


#Q.3- Count the number of time an object occurs in a list.

list1=['apple','lichi','banana','orange','orange','lichi','lichi']
print(list1)
print("no. of count of lichi is:",list1.count('lichi'),"\n\n")
print(10*"*")


#Q.4- create a list with numbers and sort it in ascending order.

list2=['4','3','7','2','9']
print("original list:",list2)
list2.sort()
print("sorted list:",list2,"\n\n")
print(10*"*")

#Q.5- Given are two 1D arrays A and B which are sorted in ascending order.WAP to merge them into a single sorted array C.

arrA=['4','1','7','9']
arrB=['8','0','4']
arrA.sort()
arrB.sort()
print("array A :",arrA)
print("array B :",arrB)
arrC=arrA+arrB
arrC.sort()
print("array C :",arrC,"\n\n")
print(10*"*")


#Q.6-Implement a stack and queue using lists.

S_list=['4','1','9']
print("initial stack list:",S_list)
print(S_list.pop(),"is popped")
print("append 7 to stack")
S_list.append('7')
print("new stack list:",S_list)
Q_list=['3','8','5','2']
print("initial queue list:",Q_list)
print(Q_list.pop(0),"is popped")
print("append 23 to stack")
Q_list.append('23')
print("new queue list:",Q_list,"\n\n")
print(10*"*")


#OPTIONAL QUESTION Count even and odd numbers in the list.

x=[2,1,23,17,76]
print("list is:",x)
count_odd=0
count_even=0
for i in x:
        if i % 2 == 0:
    	     count_even+=1
        else:
    	     count_odd+=1
print("Number of even numbers :",count_even)
print("Number of odd numbers :",count_odd,"\n\n")
print(10*"*")





