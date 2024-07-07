from tkinter import *
 
 

substitution_matrix = {  "!": 0 ,"\"" : 1,"#": 2,"$": 3 ,"%": 4,  "&": 5 ,"'" : 6,"(": 7,")": 8 ,"*": 9,
            "+": 10, ",": 11,"-": 12, ".": 13,"/": 14,
    
            "0": 15 ,"1": 16,"2": 17,"3": 18 ,"4": 19,"5": 20, "6": 21 ,"7": 22,"8": 23 ,"9": 24,
            ":":25 ,";": 26,"<": 27,  "=": 28 ,">": 29,"?":30,  "@": 31 ,

            "A": 32,"B": 33, "C": 34,"D": 35, "E": 36,"F": 37, "G": 38,"H": 39,
            "I": 40,"J": 41, "K": 42,"L": 43, "M": 44,"N": 45, "O": 46,"P": 47,
            "Q": 48, "R": 49,"S": 50, "T": 51,"U": 52, "V": 53,"W": 54,"X": 55,
            "Y": 56, "Z": 57,

            "[": 58, "\\": 59,"]": 60, "^": 61,"_": 62, " ": 63,

            "a": 64,"b": 65, "c": 66,"d": 67, "e": 68,"f": 69, "g": 70,"h": 71,
            "i": 72,"j": 73, "k": 74,"l": 75, "m": 76,"n": 77, "o": 78,"p": 79,
            "q": 80, "r": 81,"s": 82, "t": 83,"u": 84, "v": 85,"w": 86,"x": 87,
            "y": 88, "z": 89,

            "{": 90, "|": 91,"}": 92, "~": 93
            }

matrix=[[3,10,20],[20,9,17],[9,4,17]] ## key matrix
RC=len(matrix) ## length of our key matrix 
messageVector = [[0] for i in range(RC)] ## creating a matrix vector initialized with 0 in all of its values this matrix is used when we change every letter in our message to a number with our substitution matrix 
cipherMatrix = [[0] for i in range(RC)]  ## creating a matrix vector initialized with 0 in all of its values this matrix is used when we are encrypting our data



def encrypt(messageVector): ## in this function we pass the message matrix which contains values from substitution matrix
    for i in range(RC): ## matrix dimensions is 3 according to our key matrix 
        for j in range(1): ## matrix dimensions is 1 as when we multiply key matrix with message vector it is (3,3)*(3,1) which gives matrix (3,1) which is the cipher matrix  
            cipherMatrix[i][j] = 0 ## cipher matrix initialized
            for x in range(RC):  ## in this for loop we basically do the multuplication between the message vector and the key matrix then do modulos 94 due to our sub matrix having  94 value
                cipherMatrix[i][j] += (matrix[i][x] *messageVector[x][j])
            cipherMatrix[i][j] = cipherMatrix[i][j] % 94
    return cipherMatrix





def HillCipher(message): ## in this part we basically we pass the real message as a parameter and we do for loop on our sub matrix in order to find the equivlant value for each of the letters in our real message and form our message vector
    cipherMatrix1=[]
    for i in range(RC):
      for key in substitution_matrix.keys():
        if message[i]==key:
          messageVector[i][0] = substitution_matrix[key]
    cipherMatrix=encrypt(messageVector) ## here me pass our message vector in the encrypt function to be encrypted and we return the cipher matrix 
    for i in range(RC):## this for loop is basically problem solving i used it because when u try  to print the returned ciphermatrix it will be ann array inside an array so i used this loop to take all the values inisde it and put it in a normal array called ciphermatrix 1 
            cipherMatrix1.append(cipherMatrix[i][0])
##----------------------------------------------------------------------------------------------

    CipherText = []
    for i in range(RC): ## here we  do for loop on our sub matrix in order to find the equivlant value for each of the of the numbers in our ciphermatrix and print its equivlant letters 
      for key1, value1 in substitution_matrix.items():
          if value1 == cipherMatrix1[i]:
              CipherText.append(key1)
    string="".join(CipherText) 
    Output.insert(END, "".join(CipherText))






root = Tk()
root.geometry("300x400")
root.resizable(0,0)
root.title(" Encryption ")
def Take_input(Output):
    Output.delete('1.0', END)
    INPUT = inputtxt.get("1.0", "end-1c")
    print(INPUT)
    n=3
    test = ""
    my_list = [INPUT[idx:idx + n] for idx in range(0, len(INPUT), n)]
    for i in range(len(my_list)):
        HillCipher(my_list[i])

     
l = Label(text = "Enter your text")
inputtxt = Text(root, height = 10,
                width = 25,
                bg = "light yellow")
 
Output = Text(root, height = 5,
              width = 25,
              bg = "light cyan")
 
Display = Button(root, height = 2,
                 width = 20,
                 text ="Encrypt",
                 command = lambda:Take_input(Output))
 
l.pack()
inputtxt.pack()
Display.pack()
Output.pack()
 
mainloop()