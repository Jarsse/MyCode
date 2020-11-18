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
        line = f.readline()
        while line:
            if not line.__contains__(args.get("emptyMark")):
                splitted = line.split(",")
                splitted.pop(0)
                if fNew.writable():
                    st = ""
                    for txt in splitted:
                        st += txt + ","
                    st = st[:-1]
                    fNew.write(st)
            line = f.readline()
finally:
    f.close()
    fNew.close()
