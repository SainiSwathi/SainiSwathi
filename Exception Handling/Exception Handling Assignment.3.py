#3. Write a python program that opens a file and handles a FileNotFound exception if the file does not exist.

def open_file(filename):
    try:
        file=open(filename, 'r')
        print(f"Fie '{filename}' opend sucessfully.")
        print(file.read())
        file.close()
    except FileNotFoundError:
        print(f"Error:File '{filename}' not found.")


open_file('example.txt')
