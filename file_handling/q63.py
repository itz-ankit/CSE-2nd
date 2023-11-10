name= input("Enter file name: ")
with open(name,'r') as f:
    sentence=f.read()
    word=sentence.split()
    num=len(word)
    print("The file contains ",num, "words")

'''
Enter file name: Countwords.txt
The file contains  12 words

'''