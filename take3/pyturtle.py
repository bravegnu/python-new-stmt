import tokenize
import token
import codecs, cStringIO, encodings
from encodings import utf_8

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

class StreamReader(utf_8.StreamReader):
    def __init__(self, *args, **kwargs):
        codecs.StreamReader.__init__(self, *args, **kwargs)
        data = convert(self.stream.readline)
        self.stream = cStringIO.StringIO(data)

def search_function(s):
    if s != 'pyturtle':
        return None

    utf8 = encodings.search_function('utf8') # Assume utf8 encoding
    return codecs.CodecInfo(
        name='pyturtle',
        encode = utf8.encode,
        decode = utf8.decode,
        incrementalencoder=utf8.incrementalencoder,
        incrementaldecoder=utf8.incrementaldecoder,
        streamreader=StreamReader,
        streamwriter=utf8.streamwriter)

codecs.register(search_function)
