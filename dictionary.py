# Dict={} #empty dictionary
# print(Dict)
# print(dict([('Roll no.', '16/001'), ('Name', 'Vaibhav'), ('Class', 12), ('Course', 'B.tech')])) #using dict() function
# Dict1={x: 2*x for x in range(1,11)}
# print(Dict1) #using dict comprehension
# dict1={"Roll no.":"16/001","Name":"Vaibhav","Class":12,"Course":"B.tech"}   #dictionary with integer keys

# print("dict1[ROLL_NO] = "+dict1["Roll no."]) #accessing values
# print("dict1[NAME] = "+dict1['Name'])

# dict1['Class']='CSE' #modify
# dict1['Town']='Purnia' #new entry
# print("dict1[TOWN] = "+dict1['Town'])
# print("DICTIONARY:",dict1) #print modified dictionary
Dict={'Roll no.': '16/001', 'Name': 'Vaibhav', 'Class':12, 'Course': 'B.tech', 'Town': 'Purnia'}
print('Length:',len(Dict)) #length
print("String representation:",str(Dict)) #string representation
# Dict.clear() #deletes all entries 
# print(Dict)
Dict1 = Dict.copy() #shallow copy
print("Dict1:",Dict1)
Dict1['Course']='BCA'
print("Dict1[Course] :",Dict1['Course'])
print("Dict:",Dict) #No change in dict

