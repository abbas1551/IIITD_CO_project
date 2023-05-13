import reader


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

print(regs)

f = open("ISA.txt", "r")
ISA = f.read()
ISA = eval(ISA)

input_list = reader.final_data

registors = [R0, R1, R2, R3, R4, R5, R6, FLAG]

#print(ISA)
#print(reader.final_data)

machinecode = []


for i in range(len(input_list)):
    machinecode.append([])
    if input_list[i][0] == 'add':
        machinecode[i].append(ISA['add'])
        machinecode[i].append("00")
        print("\n")
        print(input_list[i[1]])
        print("look here!!")
        #machinecode[i].append()
    elif input_list[i][0] == 'sub':
        machinecode[i].append(ISA['sub'])
        
    elif input_list[i][0] == 'mov':
        machinecode[i].append(ISA['mov'])
    elif input_list[i][0] == 'ld':
        machinecode[i].append(ISA['ld'])
    elif input_list[i][0] == 'st':
        machinecode[i].append(ISA['st'])
    elif input_list[i][0] == 'mul':
        machinecode[i].append(ISA['mul'])
        machinecode[i].append("00")
        print("\n")
        print(regs[input_list[i][1]])
        print("look here!!")
    elif input_list[i][0] == 'div':
        machinecode[i].append(ISA['div'])
    elif input_list[i][0] == 'rs':
        machinecode[i].append(ISA['rs'])
    elif input_list[i][0] == 'ls':
        machinecode[i].append(ISA['ls'])
    elif input_list[i][0] == 'xor':
        machinecode[i].append(ISA['xor'])
    elif input_list[i][0] == 'or':
        machinecode[i].append(ISA['or'])
    elif input_list[i][0] == 'and':
        machinecode[i].append(ISA['and'])
    elif input_list[i][0] == 'not':
        machinecode[i].append(ISA['not'])
    elif input_list[i][0] == 'cmp':
        machinecode[i].append(ISA['cmp'])
    elif input_list[i][0] == 'jmp':
        machinecode[i].append(ISA['jmp'])
    elif input_list[i][0] == 'jlt':
        machinecode[i].append(ISA['jlt'])
    elif input_list[i][0] == 'jgt':
        machinecode[i].append(ISA['jgt'])
    elif input_list[i][0] == 'je':
        machinecode[i].append(ISA['je'])
    elif input_list[i][0] == 'hlt':
        machinecode[i].append(ISA['hlt'])    
        machinecode[i].append("00000000000")
    
    
print(machinecode)
