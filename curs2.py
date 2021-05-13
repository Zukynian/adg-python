print("Acesta este cursul al 2-lea !")

name="Ana"
if name:
    print(name)
    print(type(name))
else:

    print("nu avem deficinit niciun nume")

first_person= {'Name':'John'}
second_person=first_person

if first_person is second_person:
    print('they are the same')
else:
    print('they are not the same')

if first_person == second_person:
    print('they are the same')
else:
    print('they are not the same')

my_string=("Owner's manual")
print(my_string)

print ("""sdhasfhasf
fafasdasddasafas
fafafasdasaffas""")


def my_function():
    """this fucntion does so0mething"""

name="Ion"
age=18
msg="{name} has {age} years".format(name="Ion",age=18)
print(msg)

l=[1,2,3,"Ana are mere",True,False,None,[4,5,6]]
print(l[2])

inventar=["faina","drojdie","apa","sare"]
for item in inventar:
    print(item)

for index, value in enumerate(inventar):
    print(f"{value} la poizitia {index}")

l1=[2,3,0,8]
l2=[12,13,18,19]

l3=l1+l2
print(l3)

my_dictionary ={1:"Home",  2:"Office", 3:"Restaurant"}

for key, val in my_dictionary.items():
    print(f"{key}=>{val}")

v=my_dictionary.get(4,"**")
print(v)


l1=[1,2,2,3]
l2=[2,3,4,5]
print(l1)

my_set1=set(l1)
my_set2=set(l2)
print(my_set1.intersection(my_set2))