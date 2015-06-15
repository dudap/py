import sys
import string
login = sys.argv[1]
username = {}
passwd = open('passwd')
for line in passwd.readlines():
        rec = string.split(line, ':')
        username[rec[0]] = rec[4]
print "%s to %s" % (login, username[login])
