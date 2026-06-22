# # -----------------------TUPLE--------------------------
# # Definition and property of tuple
# # Creation of tuple
# # Indexing and slicing
# Traversing
# In-biuilt method
# Assignment and class Acitivy.

# # Definition and property of tuple--------------
#1. tuple is a data structure in python used to store
#2. multiple data of different types with comma(,) in round braces.
#3. Immutable
#4. supprort indexing,slicing and ordered.

#-----------------------creation of tuple----------------------
t1,t2,t3=(50,40,"manisha")
print(type(t3))
print(t1)
print(t2)
print(t3)

#----------------------indexing and slicing.---------------------
marks_tuple=(50,55,69,34,89)
print(marks_tuple[-1])
print(marks_tuple[::-1])

#mutability
#marks_tuple=(50,55,69,34,89)
#marks_tuple[2]=500
#print(marks_tuple)

#Transversing
# 1.waf to extract all number greater than 55, marks_tuple=(50,55,69,34,89)
def tuple_fun(m):
    new_value=[]
    for i in m:
        if i>55:
            new_value.append(i)
    return new_value
marks_tuple=(50,55,69,34,89)
res=tuple_fun(marks_tuple)
print(res)

#1. waf to sum of indexes of tuple,
marks_tuple=(50,55,69,34,89)
count=0
for i in range(len(marks_tuple)):
    count += i
print("sum of all indexes of tuple is:", count)







       

