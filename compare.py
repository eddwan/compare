import sys
import os

compareDir = os.environ["COMPARE_DIR"]
sourceFile = sys.argv[1]
compareFile = compareDir + sys.argv[1]

print "Source file:  " + sourceFile
print "Compare file: " + compareFile

output = ['\n\n# ------ NEW PROPERTIES BELOW --------']

with open(sourceFile) as fp:
   line = fp.readline()
   found = False
   while line:
        if ( not line.startswith("#") ) and ( len(line.strip()) > 0 ) :
            property = line.strip()
            property = property.split("=")
            if property[0] not in open(compareFile).read():
                found = True
                output.append(line.strip())
        line = fp.readline()

#print output

if found:
    with open(compareFile, "a") as cpfW:
        for item in output:
            cpfW.write('%s\n' % item)
else:
    print "There is no new properties on source File"
