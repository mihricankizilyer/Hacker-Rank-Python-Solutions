x = "ABCDFDFGHBGDF"
y = "DF"

def calculate(string, sub_string):
    count = 0
    for i in range(0,len(string)):
        if string[i:].startswith(sub_string):
            count+=1
    return count
calculate(x,y)


