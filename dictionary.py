# # -----------------------DICTIONARY--------------------------
# # Definition and property of dictionary
# # Creation of dictionary
# # Indexing and slicing
# Traversing
# In-built method
#dictionary comprehension
# Assignment and class Acitivy.

#-----------------------Definition and property of dictionary----------------------
#1. dictionary is a data structure in python used to store multiple data in
#key-value format.
#2ordered, mutable 
#3.indexed by key, not position
#4.key must be unique and immutable
#5.value can be of any data type and can be duplicated.
#6.dynamic in nature, can be changed at runtime.
#7. used in fast lookup

#-----------------------creation of dictionary--------------------------------
stu_profile={"aman":"noida","rohan":"delhi"}
print(type(stu_profile))
print(stu_profile)

stu_marks=dict([('aman',300),("shivam",80)])
print(stu_marks)

stu_profile={"aman":"noida","rohan":"delhi"}
stu_profile["aman"]="gurgaon"
print(stu_profile)

#to
stu_marks={'aman':300,'shivam':80, 'rohan':40, 'abhi':44}
for i in stu_marks:

#------------------------inbuilt-method--------------------------------
stu_marks ={'aman':300,'shivam':80,'rohan':40,'abhi':44}
v=stu_marks.values()
k=stu_marks.keys()
print(v)
print(k)

#---------------------------update-------------------------------------------------
stu_marks={'aman':300, 'shivam':80 ,'rohan':40,'abhi':44}
new_marks={"kamal":89,"ram":77,'aman':30}
stu_marks.update(new_marks)
print(stu_marks)

profile={'aman':{'address':["Noida","Delhi","mumbai"]},"dev":{"address":["Noida","Delhi","mumbai","varanasi"]}}
res=profile.get('aman')
print(res)

profile={
    'aman':{
        'address':["Noida","Delhi","Mumbai"],
        'hobbies':["reading","cooking","travelling"],
        'password':{"insta":"443433","facebook":"45645"}
    },
}
res=profile["aman]["password"]["insta"]
print(res)

marks=[56,78,89,78]
stu_name=["a","b","c","d"]
