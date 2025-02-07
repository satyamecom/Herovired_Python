# def printfun():
#     print("This is first function")

# printfun()




def extraSentence(text):
    arr=text.split('.')
    numofarr=len(arr)
    return arr,numofarr
    
output,numoutput=extraSentence("This is first. function")
print(numoutput)

text2="This is a. Devops team. python function"
sentences,numberofsentence=extraSentence(text2)
print("sentences:", sentences)
print("number of sentence: ", numberofsentence)
