import Check_Monitin

WANNACRY = '84c82835a5d21bbcf75a61706d8ab549'
MONITIN_FILE = 'My_Dir\RimonCrtNew.exe'
MONITIN_DIR = 'My_Dir'

def main():
    option, file = menu()
    if option == '1':
        printFile(Check_Monitin.singleFile2List(file), file)
    elif option == '2':
        printDir(Check_Monitin.directory(file))

def menu():
    print "Options:\n",\
        "\t1 -> Calculate monitin for a file\n",\
        "\t2 -> Calculate monitin for all files under a folder\n"
    option = raw_input("Please select action: ")
    file = raw_input("Please enter a path: ")
    return option, file

# Printing directory
def printDir(lst):
    print "\n{:<30} {:<17} {:<15} {:<25} {:<10}".format('File', 'Size in Mb', 'Executable', 'Change time', 'Rate')
    for i in lst:
        print "{:<30} {:<17} {:<15} {:<25} {:<10}".format(i[0], i[1][0], i[1][1], i[1][2], i[1][3])

# Printing single file
def printFile(lst, file_path):
    print "\n{:<30} {:<17} {:<15} {:<25} {:<10}".format('File', 'Size in Mb', 'Executable', 'Change time', 'Rate')
    print "{:<30} {:<17} {:<15} {:<25} {:<10}".format(file_path, lst[0], lst[1], lst[2], lst[3])

if __name__ == '__main__':
    main()