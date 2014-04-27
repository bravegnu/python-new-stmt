import tokenize
import token
import sys

with open(sys.argv[1]) as fp:
    for ttype, tval, _, _, _ in tokenize.generate_tokens(fp.readline):
        print "%-10s: %s" % (token.tok_name[ttype], tval)
