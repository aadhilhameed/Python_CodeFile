#using for loop and printing name
names = []
names.append('wajiii')
names.append('sharmii')
names.append('samra')
names.append('shama')
names.append('hani')

print(names)
for name in names:
    print("hi", name)
del names[4]
print(names)
 

#dictionary
dic = {'name' :'wajiii', 'age': 22 }
dic['name'] = 'shamri'
dic['age'] = 22
dic['state'] = 'undergraduate'
print(dic)

for name, value in dic.items():
    print (name , ":", value)

#dic in list
list_01 = []
name_1 = {'name': 'wajiii',
          'age': 22,
          'state': 'mannar'}
list_01.append(name_1)
print(list_01)

name_2 = {'name' : 'sharmii',
          'age' : 22,
          'state': 'mannar'}
list_01.append(name_2)
for name_all in list_01:
    for i, j in name_all.items():
        print(i , ':', j)
    print("\n")












   
