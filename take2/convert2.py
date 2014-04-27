import tokenize
import token
import sys

def convert(readline):
    result = []
    in_repeat = False

    for ttype, tval, _, _, _ in tokenize.generate_tokens(readline):
        if ttype == token.NAME and tval == "repeat":
            result.extend([
                (token.NAME, "for"),
                (token.NAME, "_"),
                (token.NAME, "in"),
                (token.NAME, "range"),
                (token.OP, "(")
            ])
            in_repeat = True

        elif in_repeat and ttype == token.OP and tval == ":":
            result.extend([
                (token.NAME, ")"),
                (token.OP, ":")
            ])

        else:
            result.append((ttype, tval))

    return tokenize.untokenize(result)
        
if __name__ == "__main__":
    ifp = open(sys.argv[1])
    ofp = open("out.py", "w")

    out = convert(ifp.readline)
    ofp.write(out)

    ofp.close()
    ifp.close()
