import reader
from functions import dec_to_bin, gen_address

R0 = 0
R1 = 0
R2 = 0
R3 = 0
R4 = 0
R5 = 0
R6 = 0
FLAG = 0

raw_regs = open("register.txt", "r")
raw_regs = raw_regs.read()
regs = eval(raw_regs)


f = open("ISA.txt", "r")
ISA = f.read()
ISA = eval(ISA)

input_list = reader.final_data

registors = [R0, R1, R2, R3, R4, R5, R6, FLAG]

machinecode = []

count = 127
lab_address = bin(count)
labels = []
lables_dict = {}

lable_numer = 0

variables = {}
add_var = 0


#print(len(input_list))
num_vars = 0

for i in range(len(input_list)):
    if input_list[i][0] == 'var':
        num_vars+=1

vars_temp = 0

total = len(input_list)

r = 0

binvar = total - num_vars

for i in range(len(input_list)):
    r+=1
    lable_numer+=1
    if input_list[i][0] != 'var':
        lable_numer += 1
    machinecode.append([])
    if input_list[i][0] == 'var':
        variables[input_list[i][1]] = gen_address(binvar + vars_temp)
        
    if input_list[i][0].count(":"):
        
        labels.append([input_list[i][0],gen_address(r-1-num_vars)])
        lables_dict[input_list[i][0]] = gen_address(r-1-num_vars)
        count = count - 1
        if input_list[i][1] == 'add':
            machinecode[i].append(ISA['add'])
            machinecode[i].append("00")
            machinecode[i].append(regs[input_list[i][2]])
            machinecode[i].append(regs[input_list[i][3]])
            machinecode[i].append(regs[input_list[i][4]])
        elif input_list[i][1] == 'sub':
            machinecode[i].append(ISA['sub'])
            machinecode[i].append("00")
            machinecode[i].append(regs[input_list[i][2]])
            machinecode[i].append(regs[input_list[i][3]])
            machinecode[i].append(regs[input_list[i][4]])
        elif input_list[i][1] == 'mov':
            if(input_list[i][3][0] == "$"):
                machinecode[i].append("00010")
                machinecode[i].append("0")
                machinecode[i].append(regs[input_list[i][2]])
                machinecode[i].append(dec_to_bin(input_list[i][3]))
            else:
                machinecode[i].append("00011")
                machinecode[i].append("00000")
                machinecode[i].append(regs[input_list[i][2]])
                machinecode[i].append(regs[input_list[i][3]])
        elif input_list[i][1] == 'ld':
            machinecode[i].append(ISA['ld'])
            machinecode[i].append["0"]
            machinecode[i].append(regs[input_list[i][2]])
            machinecode[i].append("Memory location")
        elif input_list[i][1] == 'st':
            machinecode[i].append(ISA['st'])
            machinecode[i].append("0")
            machinecode[i].append(regs[input_list[i][2]])
            machinecode[i].append(variables[input_list[i][3]])
        elif input_list[i][1] == 'mul':
            machinecode[i].append(ISA['mul'])
            machinecode[i].append("00")
            machinecode[i].append(regs[input_list[i][2]])
            machinecode[i].append(regs[input_list[i][3]])
            machinecode[i].append(regs[input_list[i][4]])
        elif input_list[i][1] == 'div':
            machinecode[i].append(ISA['div'])
            machinecode[i].append("00000")
            machinecode[i].append(regs[input_list[i][2]])
            machinecode[i].append(regs[input_list[i][3]])
        elif input_list[i][1] == 'rs':
            machinecode[i].append(ISA['rs'])
            machinecode[i].append("0")
            machinecode[i].append(regs[input_list[i][2]])
            machinecode[i].append(dec_to_bin(input_list[i][3]))
        elif input_list[i][1] == 'ls':
            machinecode[i].append(ISA['ls'])
            machinecode[i].append("0")
            machinecode[i].append(regs[input_list[i][2]])
            machinecode[i].append(dec_to_bin(input_list[i][3]))
        elif input_list[i][1] == 'xor':
            machinecode[i].append(ISA['xor'])
            machinecode[i].append("00")
            machinecode[i].append(regs[input_list[i][2]])
            machinecode[i].append(regs[input_list[i][3]])
            machinecode[i].append(regs[input_list[i][4]])
        elif input_list[i][1] == 'or':
            machinecode[i].append(ISA['or'])
            machinecode[i].append("00")
            machinecode[i].append(regs[input_list[i][2]])
            machinecode[i].append(regs[input_list[i][3]])
            machinecode[i].append(regs[input_list[i][4]])
        elif input_list[i][1] == 'and':
            machinecode[i].append(ISA['and'])
            machinecode[i].append("00")
            machinecode[i].append(regs[input_list[i][2]])
            machinecode[i].append(regs[input_list[i][3]])
            machinecode[i].append(regs[input_list[i][4]])
        elif input_list[i][1] == 'not':
            machinecode[i].append(ISA['not'])
            machinecode[i].append("00000")
            machinecode[i].append(regs[input_list[i][2]])
            machinecode[i].append(regs[input_list[i][3]])
        elif input_list[i][1] == 'cmp':
            machinecode[i].append(ISA['cmp'])
            machinecode[i].append("00000")
            machinecode[i].append(regs[input_list[i][2]])
            machinecode[i].append(regs[input_list[i][3]])
        elif input_list[i][1] == 'jmp':
            machinecode[i].append(ISA['jmp'])
            machinecode[i].append("0000")
            machinecode[i].append(lables_dict[input_list[i][1]+':'])
        elif input_list[i][1] == 'jlt':
            machinecode[i].append(ISA['jlt'])
            machinecode[i].append("0000")
            machinecode[i].append(lables_dict[input_list[i][1]+':'])
        elif input_list[i][1] == 'jgt':
            machinecode[i].append(ISA['jgt'])
            machinecode[i].append("0000")
            machinecode[i].append(lables_dict[input_list[i][1]+':'])
        elif input_list[i][1] == 'je':
            machinecode[i].append(ISA['je'])
            machinecode[i].append("0000")
            machinecode[i].append(lables_dict[input_list[i][1]+':'])
        elif input_list[i][1] == 'hlt':
            machinecode[i].append(ISA['hlt'])    
            machinecode[i].append("00000000000")
    






for i in range(len(input_list)): 
    if input_list[i][0] == 'var':
        variables[input_list[i][1]] = gen_address(binvar + vars_temp)
        vars_temp+=1
        
        

    elif input_list[i][0] == 'add':
        machinecode[i].append(ISA['add'])
        machinecode[i].append("00")
        machinecode[i].append(regs[input_list[i][1]])
        machinecode[i].append(regs[input_list[i][2]])
        machinecode[i].append(regs[input_list[i][3]])
    elif input_list[i][0] == 'sub':
        machinecode[i].append(ISA['sub'])
        machinecode[i].append("00")
        machinecode[i].append(regs[input_list[i][1]])
        machinecode[i].append(regs[input_list[i][2]])
        machinecode[i].append(regs[input_list[i][3]])
    elif input_list[i][0] == 'mov':
        #machinecode[i].append(ISA['mov'])
        if(input_list[i][2][0] == "$"):
            machinecode[i].append("00010")
            machinecode[i].append("0")
            machinecode[i].append(regs[input_list[i][1]])
            machinecode[i].append(dec_to_bin(input_list[i][2]))
        else:
            machinecode[i].append("00011")
            machinecode[i].append("00000")
            machinecode[i].append(regs[input_list[i][1]])
            machinecode[i].append(regs[input_list[i][2]])
    elif input_list[i][0] == 'ld':
        machinecode[i].append(ISA['ld'])
        machinecode[i].append("0")
        machinecode[i].append(regs[input_list[i][1]])
        machinecode[i].append(variables[input_list[i][2]])
        #machinecode[i].append("Memory location")
    elif input_list[i][0] == 'st':
        machinecode[i].append(ISA['st'])
        machinecode[i].append("0")
        machinecode[i].append(regs[input_list[i][1]])
        machinecode[i].append(variables[input_list[i][2]])
        #machinecode[i].append("Memory location")
    elif input_list[i][0] == 'mul':
        machinecode[i].append(ISA['mul'])
        machinecode[i].append("00")
        machinecode[i].append(regs[input_list[i][1]])
        machinecode[i].append(regs[input_list[i][2]])
        machinecode[i].append(regs[input_list[i][3]])
    elif input_list[i][0] == 'div':
        machinecode[i].append(ISA['div'])
        machinecode[i].append("00000")
        machinecode[i].append(regs[input_list[i][1]])
        machinecode[i].append(regs[input_list[i][2]])
    elif input_list[i][0] == 'rs':
        machinecode[i].append(ISA['rs'])
        machinecode[i].append("0")
        machinecode[i].append(regs[input_list[i][1]])
        machinecode[i].append(dec_to_bin(input_list[i][2]))
    elif input_list[i][0] == 'ls':
        machinecode[i].append(ISA['ls'])
        machinecode[i].append("0")
        machinecode[i].append(regs[input_list[i][1]])
        machinecode[i].append(dec_to_bin(input_list[i][2]))
    elif input_list[i][0] == 'xor':
        machinecode[i].append(ISA['xor'])
        machinecode[i].append("00")
        machinecode[i].append(regs[input_list[i][1]])
        machinecode[i].append(regs[input_list[i][2]])
        machinecode[i].append(regs[input_list[i][3]])
    elif input_list[i][0] == 'or':
        machinecode[i].append(ISA['or'])
        machinecode[i].append("00")
        machinecode[i].append(regs[input_list[i][1]])
        machinecode[i].append(regs[input_list[i][2]])
        machinecode[i].append(regs[input_list[i][3]])
    elif input_list[i][0] == 'and':
        machinecode[i].append(ISA['and'])
        machinecode[i].append("00")
        machinecode[i].append(regs[input_list[i][1]])
        machinecode[i].append(regs[input_list[i][2]])
        machinecode[i].append(regs[input_list[i][3]])
    elif input_list[i][0] == 'not':
        machinecode[i].append(ISA['not'])
        machinecode[i].append("00000")
        machinecode[i].append(regs[input_list[i][1]])
        machinecode[i].append(regs[input_list[i][2]])
    elif input_list[i][0] == 'cmp':
        machinecode[i].append(ISA['cmp'])
        machinecode[i].append("00000")
        machinecode[i].append(regs[input_list[i][1]])
        machinecode[i].append(regs[input_list[i][2]])
    elif input_list[i][0] == 'jmp':
        machinecode[i].append(ISA['jmp'])
        machinecode[i].append("0000")
        machinecode[i].append(lables_dict[input_list[i][1]+':'])
    elif input_list[i][0] == 'jlt':
        machinecode[i].append(ISA['jlt'])
        machinecode[i].append("0000")
        machinecode[i].append(lables_dict[input_list[i][1]+':'])
    elif input_list[i][0] == 'jgt':
        machinecode[i].append(ISA['jgt'])
        machinecode[i].append("0000")
        machinecode[i].append(lables_dict[input_list[i][1]+':'])
    elif input_list[i][0] == 'je':
        machinecode[i].append(ISA['je'])
        machinecode[i].append("0000")
        machinecode[i].append(lables_dict[input_list[i][1]+':'])
    elif input_list[i][0] == 'hlt':
        machinecode[i].append(ISA['hlt'])    
        machinecode[i].append("00000000000")

# print(total)
# print(num_vars)
# print(variables)
