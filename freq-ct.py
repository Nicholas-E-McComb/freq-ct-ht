import hashtable
import sys
import os.path
import re


if(len(sys.argv) != 2):
    print("I'm sorry, please run this program with only one extra input, the filename in question.")
    quit()

if not (os.path.isfile(sys.argv[1])):
    print("I'm sorry, that is not a valid file name.")
    quit()
else:
    fname = sys.argv[1]

t = hashtable.hashtable()

with open(fname) as f:
    for line in f:
        p = re.compile(r"[^a-zA-Z0-9'_]+")
        stripped = p.sub(" ", line)
        temp = stripped.split()
        for word in temp:
            word = word.lower()
            if(word[0] == "'" or word[len(word)-1] == "'"):
                word = word.strip("'")
            if t.contains(word):
                val = t.get(word)
                val += 1
                t.put(word, val)
            else:
                t.put(word,1)
    print("This text contains %d distinct words." % t.size())
    print("Please enter a word to get its frequency, or just hit enter to leave")
    while True:
        cmnd = input().lower()
        if cmnd == '':
            print("Goodbye!")
            quit()
        elif cmnd[0] == "-":
            cmnd = cmnd.strip("-")
            t.delete(cmnd)
            print("%s has been deleted" % cmnd)
        else:
            ct = t.get(cmnd)
            if ct is 0:
                print("%s does not appear" % cmnd)
            else:
                print("%s appeared %d time(s)" %(cmnd,ct))
