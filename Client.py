import json
import pprint
import Check_Monitin

NEW = 'A3FC3D4DEC7DA63A6FE224A3B529144F'
RIMON = '8d9de58d7fded7a4b734707ea7614998'
TXT = '202119E519DD179DE64AFD195F0DDA42'
WANNACRY = '84c82835a5d21bbcf75a61706d8ab549'
MONITIN_FILE = 'Monitin_Dir\RimonCrtNew.exe'
MONITIN_DIR = 'Monitin_Dir'

def main():
    # dic = Monitin.directory(MONITIN_DIR)
    # Monitin.sortDicByRate(dic)
    option, file = menu()
    if option == '1':
        printFile(Check_Monitin.singleFile2List(file), file)
    elif option == '2':
        printDic(Check_Monitin.directory(file))

def menu():
    print "Options:\n",\
        "\t1 -> Calculate monitin for a file\n",\
        "\t2 -> Calculate monitin for all files under a folder\n"
    option = raw_input("Please select action: ")
    file = raw_input("Please enter a path: ")
    return option, file

def printDic(lst):
    print "\n{:<30} {:<17} {:<15} {:<25} {:<10}".format('File', 'Size in Mb', 'Executable', 'Change time', 'Rate')
    for i in lst:
        print "{:<30} {:<17} {:<15} {:<25} {:<10}".format(i[0], i[1][0], i[1][1], i[1][2], i[1][3])

def printFile(lst, file_path):
    print "\n{:<30} {:<17} {:<15} {:<25} {:<10}".format('File', 'Size in Mb', 'Executable', 'Change time', 'Rate')
    print "{:<30} {:<17} {:<15} {:<25} {:<10}".format(file_path, lst[0], lst[1], lst[2], lst[3])

def printDicJson(dic):
    print json.dumps(dic, indent=4)

def printDicPP(dic):
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(dic)

if __name__ == '__main__':
    main()