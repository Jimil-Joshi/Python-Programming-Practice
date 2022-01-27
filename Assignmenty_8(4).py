my_str = "Hello, My name Is Jimil"


new_word =[word.lower() for word in my_str.split()]
new_word.sort()
for w in new_word:
    print(w)
