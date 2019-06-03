
def pascal_jesse(lookup_line):
    append_one = [1]
    if lookup_line == 1:
        # First line needs special treatment since it is just a value of "1" in a list. It doesn't follow any calculations.
        return [1]
    else:
        pascal_line = []
        for iteration in range(2,lookup_line+1):
            # iteration doesn't actually do anything. We just want the program to calculate each line of Pascal's triangle until the desired line is hit.
            # We also use range 2 to lookup_line + 1 for a more intuitive approach. In a literal sense, it means from the second line to the last line. We do this because first line is already accounted for.

            pascal_line = append_one+[pascal_line[i]+pascal_line[i+1] for i in range(len(pascal_line)-1)]+append_one
            # List comprehension to continuously updating the pascal_line variable until the desired line is hit. Then we return the last line.
        return pascal_line


line = input("Which Pascal Line do you want to see? Enter here: ")

if int(line) > 0:
    print(pascal_jesse(int(line)))
else:
    raise Exception("Bad entry!")