def main():

    global R_sorted
    global S_sorted
    global RjoinS

    open_files()

    max_buffer_len = 0
    buffer = []
    R = ""
    R_sorted_line = R_sorted.readline()
    S_sorted_line = S_sorted.readline()

    while(R_sorted_line):

        R_sorted_split = R_sorted_line.split()
        R_sorted_first = R_sorted_split[0]
        if(R_sorted_first != R):

            buffer = []
            R = R_sorted_first
            while(S_sorted_line):
                S_sorted_split = S_sorted_line.split()
                S_sorted_first = S_sorted_split[0]

                if(R_sorted_first < S_sorted_first):
                    break
                if(R_sorted_first == S_sorted_first):
                    buffer.append(S_sorted_split[1])
                    if(len(buffer) > max_buffer_len):
                        max_buffer_len = len(buffer)
                    RjoinS.write(R_sorted_first+"\t"+R_sorted_split[1]+"\t"+S_sorted_split[1]+"\n")
                S_sorted_line = S_sorted.readline()
        else:
            for x in buffer:
                RjoinS.write(R_sorted_first+"\t"+R_sorted_split[1]+"\t"+x+"\n")

        R_sorted_line = R_sorted.readline()
        if not S_sorted_line:
            RdifferenceS.write(R_sorted_first + "\t" + R_sorted_second+"\n")

    print("Max buffer lenght: " + str(max_buffer_len))

    R_sorted.close()
    S_sorted.close()
    RjoinS.close()

def open_files():

    global R_sorted
    global S_sorted
    global RjoinS

    inputfile1 = input("enter first sorted file ")
    while True:   # repeat until the try statement succeeds
        try:
            R_sorted = open(inputfile1,"r")
            break                             # exit the loop
        except IOError:
            inputfile1 = input("Could not open file! Please try again: ")
            # restart the loop

    inputfile2 = input("enter second sorted file ")
    while True:   # repeat until the try statement succeeds
        try:
            S_sorted = open(inputfile2,"r")
            break                             # exit the loop
        except IOError:
            inputfile2 = input("Could not open file! Please try again: ")
            # restart the loop

    outputfile = input("enter output filename ")
    while True:   # repeat until the try statement succeeds
        try:
            RjoinS  = open(outputfile,"w")
            break                             # exit the loop
        except IOError:
            outputfile = input("Could not open file! Please try again: ")
            # restart the loop


if __name__ == "__main__":
    main()
