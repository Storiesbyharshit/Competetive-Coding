import string

numalpha = dict(zip(range(1, 27), string.ascii_uppercase))

inp = int(input())

def convert(inp):
    res = []
    inp = str(inp)
    for i in inp:
        res.append(numalpha[int(i)])
    return "".join(res)

result = convert(inp)
print(result)
    
