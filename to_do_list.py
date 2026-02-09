user_input='random'
data=[]

def show_menu():
    print('Menu:')
    print('1.Add an item')
    print('2.Mark as done')
    print('3.View the to do items')
    print('4.Exit')

while user_input!='4':
    show_menu()
    user_input=input('Enter your choice: ')
    if user_input=='1':
        item=input('What is to be done? ')
        data.append(item)
        print('You added: ',item)
    elif user_input=='2':
        item=input('What is to be marked as done? ')
        if item in data:
            data.remove(item)
            print('You removed: ',item)
        else:
            print('Item not found in the list.')
    elif user_input=='3':
        print('Items in to-do list: ')
        for item in data:
            print(item)
    elif user_input=='4':
        print('Goodbye')
    else:
        print('Please enter one of 1, 2, 3 and 4')
