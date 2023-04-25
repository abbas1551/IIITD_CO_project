import reader


R0 = 0
R1 = 0
R2 = 0
R3 = 0
R4 = 0
R5 = 0
R6 = 0
FLAG = 0



f = open("ISA.txt", "r")
ISA = f.read()
ISA = eval(ISA)

input_list = reader.final_data

registors = [R0, R1, R2, R3, R4, R5, R6, FLAG]

print(ISA)


machinecode = []


for i in range(len(input_list)):
    machinecode.append([])
    if input_list[i][0] == 'add':
        machinecode[i].append(ISA['add'])
    elif input_list[i][0] == 'sub':
        machinecode[i].append(ISA['sub'])
    elif input_list[i][0] == 'mov':
        machinecode[i].append(ISA['mov'])