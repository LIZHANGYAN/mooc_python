def mergeAddress():
    teleFile = open('..\data\TeleAddressBook.txt','rb')
    emailFile = open('..\data\EmailAddressBook.txt','rb')
    mergeFile = open('..\data\MergeAddressBook.txt','w')

    list1Name = []
    list1Tele = []
    list2Name = []
    list2Email = []
    # 跳过第一行
    teleFile.readline()
    emailFile.readline()

    for line in teleFile:
        elements = line.split()
        list1Name.append(str(elements[0].decode('gbk')))
        list1Tele.append(str(elements[1].decode('gbk')))
    for line in emailFile:
        elements = line.split()
        list2Name.append(str(elements[0].decode('gbk')))
        list2Email.append(str(elements[1].decode('gbk')))

    lines = []
    lines.append('姓名\t    电话\t    邮箱\n')
    for i in range(len(list1Name)):
        s = ''
        if list1Name[i] in list2Name:
            j = list2Name.index(list1Name[i])
            s = '\t'.join([list1Name[i],list1Tele[i],list2Email[j]])
            s+='\n'
        else:
            s = '\t'.join([list1Name[i],list1Tele[i],str('  -----   ')])
            s+='\n'

        lines.append(s)

    for i in range(len(list2Name)):
        s = ''
        if list2Name[i] not in list1Name:
            s = '\t'.join([list2Name[i],str('   -----   '),list2Email[i]])
            s+='\n'
        lines.append(s)

    mergeFile.writelines(lines)
    teleFile.close()
    emailFile.close()
    mergeFile.close()

if __name__ =='__main__':
    mergeAddress()