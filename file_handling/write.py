with open('file2.txt','w') as f:
    fw=''' Hello I am Archismwan Chatterjee
                 from 2nd Year CSE'''
    fww=['Hi\n','I am \n', 'Archismwan Chatterjee\n']
    f.write(fw)
    f.writelines(fww)