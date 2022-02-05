import zlib
n = 'hello world!hello world!hello world!hello world!'
n = bytes(n, 'utf-8')
comp = zlib.compress(n)
print(comp)

decomp = zlib.decompress(comp)
print(decomp)


