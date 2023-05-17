import error_gen

con = error_gen.error_present

if con == False:
    from translator import machinecode

    def write(filename, list):
        file = open(filename, 'w')
        for i in range(len(list)):
            if list[i] == []:
                continue
            for j in range(len(list[i])):

                file.write(list[i][j])
                #file.write("_")
            file.write("\n")
        file.close()

    output_file_name = "output.txt"
    output_list = machinecode




    write(output_file_name, output_list)


    out = open("output.txt", 'r')
    out = out.read()
    import sys
    sys.stdout.write(out)
