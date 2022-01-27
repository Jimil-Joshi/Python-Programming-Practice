punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

my_str = "Hii, My name is &J(&i}m^i)l"
char = ""
for p in my_str:
    if p not in punctuations:
        char = char + p
print(char)