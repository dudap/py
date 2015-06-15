import sys
import string
text = sys.argv[1]
counter = 0
for line in sys.stdin.readlines():
        if string.count(line, text):
                print line
                counter += 1
    
print "Znaleziono %d linii zawierajacych %s" % (counter, text)
