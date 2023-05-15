from reader import final_data
error_present = False

hlt_count = 0

ISA = open("ISA.txt", 'r')

ISA = ISA.read()
ISA = eval(ISA)

regs = open("testing_regs.txt", 'r')
regs = regs.read()
regs = eval(regs)

mov_registers = open("register.txt")
mov_registers = mov_registers.read()
mov_registers = eval(mov_registers)

variables = []
lables = []
vars = True

for i in final_data:    
    #print(i)
    if (i[0] != 'var'):  
        vars = False
    if (i[0] == 'var'): #checks for erroe in middle of code
        if (vars == False):
            print("variable assigned in middle of code")
            error_present = True ######checks out till here
    for j in i:    #checks for more than one halt
        if j == 'hlt':
            hlt_count+=1
            if hlt_count >1:
                print("hlt occures more than once")
                error_present = True######checks out till here
    if i[0] == 'var':
        variables.append(i[1])
    if i[0][-1] == ':':
        lables.append(i[0])
    
    if i[0] == 'st':  #checks for unknown variables in st funciton
        if len(i) != 3:
            print("st should have 2 parameters")  
        elif len(i) == 3:
            if i[2] not in variables:
                print(i[2], "not a variable")
                error_present = True#checks out till here
    if i[0] == 'ld':  #checks for unknown variables in ld funciton
        if len(i) != 3:
            print("ld only takes two arguments")
        if i[2] not in variables:
            print(i[2], "not a variable")#checks out till here
            error_present = True
    if ((i[0] == 'add') or (i[0] == 'sub') or ( i[0] == 'mul') or (i[0] == 'xor') or (i[0] == 'or')):  #checking if type A are correct
       # print("add was encountered", len(i[0]))
        if len(i) != 4:
            print(i[0], "takes 3 arguments", len(i)-1, "given")

            error_present = True
        elif (len(i) == 4):
            if ((i[1] not in regs) or (i[2] not in regs) or (i[3] not in regs) ):
                print("one or more of",i[1],i[2], i[3], "not in registers") #checks out till here
    if ((i[0] == 'ls') or (i[0] == 'rs')):
        #print(len(i))
        if len(i) != 3:
            print(i[0][1:], "takes 2 arguments", len(i)-1, "given")
            error_present = True
        elif len(i) == 3:
            #print(i[2])
            #print(i[2].isdigit(), i[2])
            if (i[1] not in regs):
                print(i[1], "not a valid register")
                error_present = True
            if (i[2][0] != '$'):
                print("imm must include $ before assignment")
                error_present = True
            if (i[2][1:].isdigit() ==  False):
                print(i[2][1:],"not an valid intiger")
                error_present = True
            else:
                if (int(i[2][1:]) > 127):
                    print(i[2][1:],"value overflow, greater than 127")
                    error_present = True  #we checks out till here
    if (i[0] == 'mov'):
        if len(i) != 3:
            print("mov takes 2 arguments")
        if (len(i) == 3):
            if i[2][0] == '$':
                if (i[2][1:].isdigit() == False):
                    print(i[2][1],"not an intiger")
                    error_present = True
                else:
                    if (int(i[2][1:]) > 127):
                        print(i[2][1:],"value overflow, greater than 127")
                        error_present = True  #we checks out till here
            else:
                if ((i[1] not in mov_registers) or (i[2] not in mov_registers)):
                    print("one or more of", i[1], i[2], "are not valid registers")


    if ((i[0] == 'not') or (i[0] == 'cmp')):
        if (len(i) != 3):
            print(i[0], "takes only 2 arguments")
            error_present = True
        if (len(i) == 3):
            if ((i[1] not in regs) or (i[2] not in regs)):
                print("one or more of", i[1], i[2], "not in registers")


    if ((i[0] not in ISA) and (i[0] != 'var')):  #condition for unknown command
        if (':' not in i[0]):
            print("Error", i[0], "not a recognised command")
            error_present = True
    
    



          

if hlt_count == 0:
    print('No halt statement cound')
    error_present = True



if final_data[-1][-1] != 'hlt':  #checks for last command to be halt
    print("last command is not hlt")
    error_present = True









for i in final_data:
    if ((i[0] == 'jmp') or (i[0] == 'jlt') or (i[0] == 'jgt') or (i[0] == 'je')):
        if (len(i) != 2):
            print(i[0], "takes 1 argument")
        if (len(i) == 2):
            if i[1] + ':' not in lables:
                print(i[1], "not in lables")
