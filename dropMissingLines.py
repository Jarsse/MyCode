import argparse

# construct argument parser
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--data", help="path to the data file")
ap.add_argument("-n", "--new", help="name of the new file")
ap.add_argument("-e", "--emptyMark",default="?", help="marker for the empty data point")
args = vars(ap.parse_args())

try:
    print("Removing empty files from {} and saving the cleaned data into {}".format(args.get("data"), args.get("new")))
    # file that will be cleaned
    if args.get("data", None) is None:
        fileName = "breast-cancer-wisconsin.data.txt"
    else:
        fileName = args.get("data")
    # new file where we write the cleaned data
    if args.get("new", None) is None:
        newFileName = "cleanedFile.data.txt"
    else:
        newFileName = args.get("new")
    f = open(fileName, "r")
    fNew = open(newFileName, "w+")
    if f.readable():
        # read first line and continue while loop while there are lines
        line = f.readline()
        while line:
            # don't write line if it contains "?"
            if not line.__contains__(args.get("emptyMark")):
                # remove ID column
                splitted = line.split(",")
                splitted.pop(0)
                if fNew.writable():
                    st = ""
                    for txt in splitted:
                        st += txt + ","
                    # remove last ","
                    st = st[:-1]
                    # write line to new file
                    fNew.write(st)
            # read next line
            line = f.readline()
finally:
    # close files
    f.close()
    fNew.close()
