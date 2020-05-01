import sys

dirname = sys.argv[1]
dirname = dirname[:-1]
print(dirname)
with open(dirname + "/.mbedignore", "w") as fp:
    fp.write(dirname + ".c")
    
