inputs = "cat32dog16cow5"

def find_string(inputs):
    temp = ""
    result = []
    numbers = ['0','1','2','3','4','5','6','7','8','9']

    for i in range(len(inputs)):
        if inputs[i] in numbers:
            if temp != "":
                result.append(temp)
            temp = ""
        else:
            temp += inputs[i]
    return result
            

string_list = find_string(inputs)
print(string_list)