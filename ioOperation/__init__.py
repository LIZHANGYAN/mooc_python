import datetime

def main():
    f1 = "..\data\8Kints.txt"
    f2 = "..\data\8Kints2.txt"

    infile = open(f1,"r")
    outfile = open(f2,"w")
    countLines = countChars = 0
    starttime = datetime.datetime.now()
    for line in infile.readlines():
        outfile.write(line)
        countLines+=1;
        countChars+=len(line);
    endtime = datetime.datetime.now()
    totaltime = (endtime-starttime).seconds
    print(countLines," lines and ",countChars," chars\n total time",totaltime,"s")
    infile.close()
    outfile.close()

main()