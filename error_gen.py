from reader import final_data
error_present = False

hlt_count = 0

ISA = open("ISA.txt", 'r')

ISA = ISA.read()
ISA = eval(ISA)

lables = []
vars = True

for i in final_data:    
    if (i[0] != 'var'):
        vars = False
    if (i[0] == 'var'): #checks for erroe in middle of code
        if (vars == False):
            print("variable assigned in middle of code")
            error_present = True
    for j in i:    #checks for more than one halt
        if j == 'hlt':
            hlt_count+=1
            if hlt_count >1:
                print("hlt occures more than once")
                error_present = True
    if i[0] == 'var':
        lables.append(i[1])
    elif i[0] == 'st':  #checks for unknown variables in st funciton
        if i[2] not in lables:
            print(i[2], "not a variable")
            error_present = True
    elif i[0] == 'ld':  #checks for unknown variables in st funciton
        if i[2] not in lables:
            print(i[2], "not a variable")
            error_present = True
    elif ((i[0] == 'add') or (i[0] == 'sub') or ( i[0] == 'mul') or (i[0] == 'xor') or (i[0] == 'or')):  #checking if type A are correct
        if len(i) != 4:
            print(i[0], "takes 3 arguments", len(i)-1, "given")
            error_present = True
    elif ((i[0] == 'ls') or (i[0] == 'rs')):
        if len(i[0]) != 3:
            print(i[0], "takes 2 arguments", len(i)-1, "given")
            error_present = True
        elif (i[2][0] != '$'):
            print("must be a $")
            error_present = True
    elif ((i[0] not in ISA) and (i[0] != 'var')):  #condition for unknown command
        if (':' not in i[0]):
            print("Error", i[0], "not a recognised command")
            error_present = True
    
    
          

if hlt_count == 0:
    print('No halt statement cound')
    error_present = True
