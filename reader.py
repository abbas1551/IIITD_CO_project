f = open("input.txt", "r")
data = f.read()



def reader(data):
    intermediate_data = data.split("\n")
    final_list = []
    counter = 0
    for i in range(len(intermediate_data)):
        if intermediate_data[i] == '':
            continue
        else:
            final_list.append([])
            element = intermediate_data[ i].split()
            for j in range(len(element)):
                final_list[counter].append(element[j])
            counter+=1
    return final_list


final_data = reader(data)


f.close()
