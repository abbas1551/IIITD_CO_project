from reader import final_data
error_present = False

hlt_count = 0

ISA = open("ISA.txt", 'r')

ISA = ISA.read()
ISA = eval(ISA)




for i in final_data:    
    for j in i:
        if j == 'hlt':
            hlt_count+=1
            if hlt_count >1:
                print("hlt occures more than once")
                error_present = True
    if ((i[0] == 'add') or (i[0] == 'sub') or ( i[0] == 'mul') or (i[0] == 'xor')):
        if len(i) != 4:
            print(i[0], "takes 3 arguments", len(i)-1, "given")
    elif ((i[0] == 'mov') or (i[0] == 'ls') or (i[0] == 'rs')):
        if len(i[0]) != 3:
            print(i[0], "takes 2 arguments", len(i)-1, "given")
        elif (i[2][0] != '$'):
            print("must be a $")
    elif ((i[0] not in ISA) and (i[0] != 'var')):
        if (':' not in i[0]):
            print("Error", i[0], "not a recognised command")
    
          
        
if hlt_count == 0:
    print('No halt statement cound')
