



def pascal_jesse(lookup_line):
    append_one = [1]
    if lookup_line == 1:
        return [1]
    else:
        pascal_line = []
        for iteration in range(2,lookup_line+1):
            pascal_line = append_one+[pascal_line[i]+pascal_line[i+1] for i in range(len(pascal_line)-1)]+append_one
        return pascal_line




line = input("Which Pascal Line do you want to see? Enter here: ")

if int(line) > 0:
    print(pascal_jesse(int(line)))
else:
    raise Exception("Bad entry!")