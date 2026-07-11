from pathlib import Path
import os

def readfileandfolder():
    path = Path('.')   # current directory
    items = list(path.rglob('*'))
    for i, item in enumerate(items):
        print(f'{i+1} : {item}')



def createfile():
    try:
        
        readfileandfolder()
        name = input("please tell your file name :-")
        p = Path (name)
        if not p.exists():

            with open (p,"w") as fs:
                data = input("what you want to write in this file:- ")
                fs.write(data)
            print("file created successfully")
        else:
            print('this file already exist!!')
    
    except Exception as err:
        print('an error offured as ', err)



def readfile():
    try:
        
        readfileandfolder()
        name = input('which file you want to read :')
        p = Path(name)
        if p.exists() and p.is_file():
            with open(p,'r') as fs:
                data = fs.read()
                print(data)
            print("file readed sucessfully")
        else:
            print('file does not exist')
    except Exception as err:
        print(f'an error occured as {err}')



def updatefile():
    try:
        readfileandfolder()
        name =  input ('tell which file you want to update:-')
        p=Path(name)
        if p.exists() and p.is_file():
            print("press 1 for changing the name of your file")
            print("press 2 for overwriting the data of your file")
            print('press 3 for appending some content of your file')

            res = int (input('tell your response:- '))

            if res == 1:
                name2 = input('tell yout new file name: ')
                p2 = Path(name2)
                p.rename(p2)
                
            if res ==2:
                with open(p,'w') as fs:
                    data = input ('tell what you want to write this will overwrite your file')
                    fs.write(data )
            
            if res ==3:
                with open(p,'a') as fs:
                    data = input ('tell what you want to append: ')
                    fs.write(" ",+data )
    except Exception as err:
        print ('some error occured that is ', err)


def deletefile():
    try:

        readfileandfolder()
        name = input (f'which file you want to delete: ')
        p = Path(name)

        if p.exists() and p.is_file():
            os.remove(name)
            print("file removed sucessfully")
        else:
            print('no such file exist')
    except Exception as err:
        print(f'some error occured : {err}')



print("Press 1 for creating a file")
print("Press 2 for reading a file")
print("Press 3 for updating a file")
print("Press 4 for delete a file")


check = int(input('enter your response : '))


if check == 1:
    createfile()

if check ==2:
    readfile()

if check ==3:
    updatefile()

if check ==4:
    deletefile()
