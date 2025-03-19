import os
def create_file(filename):
    try:
        with open(filename,'x') as f:
            print(f"File name {filename}: Created successfully")
    except FileExistsError:
        print(f"File name {filename} already exists!")
    except Exception as E:
        print("An error occured!")
def view_all_files():
    files=os.listdir()
    if not files:
        print("No file found!")
    else:
        print("Files in directory!")
        for file in files:
            print(file)
def delete_file(filename):
    try:
        os.remove(filename)
        print(f"{filename} has been deleted succesfully!")
    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print("An error ocurred")
def read_file(filename):
    try:
        with open('sample.txt','r') as f:
            content=f.read()
            print(f"Content of '{filename}':\n{content}")
    except FileNotFoundError:
        print(f"{filename} Doesn't exist!")
    except Exception as e:
        print("An error occured!")
def edit_file(filename):
    try:
        with open('sample.txt', 'a') as f:
            content=input("Enter data to add = ")
            f.write=(content +"\n")
            print(f"Content added to {filename} sucessfully!")
    except FileNotFoundError:
        print(f"{filename} Doesn't exist!")
    except Exception as e:
        print("An error occured!")

def main():
    while True:
        print("FILE MANAGEMENT APP")
        print("1: Create file")
        print("2: View all files")
        print("3: Delete file")
        print("4: Read file")
        print("5: Edit file")
        print("6: Exit")
        choice=input("Enter your choice(1-6): ")
        if choice=="1":
            filename=input("Enter the filename to create= ")
            create_file(filename)   
        elif choice=="2":
            view_all_files()
        elif choice=="3":
            filename=input("Enter the filename you want ton delete: ")
            delete_file(filename)
        elif choice=="4":
            filename=input("Enter the filename to read: ")
            read_file(filename)
        
        elif choice=="5":
            filename=input("Enter the filename to Edit: ")
            edit_file(filename)
        
        elif choice=="6":
            print("Closing the app...")
            break
        else: 
            print("In-valid syntax!")
if __name__ =="__main__":
    main()
        
        
        
        
        
        
        
        
        
        
        
        