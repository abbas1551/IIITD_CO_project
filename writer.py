from translator import machinecode

def write(filename, list):
    file = open(filename, 'w')
    for i in range(len(list)):
        if list[i] == []:
            continue
        file.write(list[i][0])
        file.write("\n")

output_file_name = "output.txt"
output_list = machinecode




write(output_file_name, output_list)