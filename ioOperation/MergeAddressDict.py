
def mergeAddressDict():
    teleFile = open('..\data\TeleAddressBook.txt','rb')
    emailFile = open('..\data\EmailAddressBook.txt','rb')

    teleFile.readline()
    emailFile.readline()
    line1 = teleFile.readlines()
    line2 = emailFile.readlines()

    dict1 = {}
    dict2 = {}

    for line in line1:
        elements = line.split()
        dict1[elements[0]] = str(elements[1].decode('gbk'))

    for line in line2:
        elements = line.split()
        dict2[elements[0]] = str(elements[1].decode('gbk'))

    lines = []
    lines.append('姓名\t      电话  \t  邮箱\n')
    for key in dict1:
        s = ''
        if key in dict2.keys():
            s= '\t'.join([str(key.decode('gbk')),dict1[key],dict2[key]])
            s+='\n'
        else:
            s = '\t'.join([str(key.decode('gbk')),dict1[key],str('  -----   ')])
            s += '\n'
        lines.append(s)
    for key in dict2:
        s = ''
        if key not in dict1.keys():
            s = '\t'.join([str(key.decode('gbk')),str(' -----   '),dict2[key]])
            s += '\n'
        lines.append(s)

    resultFile = open('..\data\MergeAddressBookDict.txt','w');
    resultFile.writelines(lines)

    resultFile.close()
    emailFile.close()
    teleFile.close()

if __name__ == '__main__':
    mergeAddressDict()