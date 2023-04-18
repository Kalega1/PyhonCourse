def console_menu():
    pass
def read_file():
    with open(path_file, 'r', encoding='UTF-8') as f:
        for line in f:
            print(line.strip())
def write_file():
    with open(path_file, 'a', encoding='UTF-8') as f:
        f.writelines('\n' + input())
def find_file():
    find_info = input()
    with open(path_file, 'r', encoding='UTF-8') as f:
        for line in f:
            if find_info.casefold() in line.casefold():
                print(line)           
def change_info():
    find_info = input()
    new_info = input()
    with open(path_file, 'r+', encoding='UTF-8') as f:
        lines = f.readlines()
        f.seek(0)
        for line in lines:
            if find_info.casefold() not in line.casefold():
                f.write(line)
            else:
                f.write(new_info + '\n')
        f.truncate()

def delete_info():
    find_info = input()
    with open(path_file, 'r', encoding='UTF-8') as f:
        lines = f.readlines()
    with open(path_file, 'w', encoding='UTF-8') as f:
        for line in lines:
            if find_info.casefold() not in line.casefold():
                f.write(line)

def main():
    change_info()


path_file = r'folder/new_text.txt'
if __name__ == '__main__':
    main()