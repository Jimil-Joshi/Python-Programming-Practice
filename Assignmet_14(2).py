input = input("Enter The String: ")
word_dict = {}

for word in input.split():
    word_dict[word] = word_dict.get(word,0)+1

for key in sorted(word_dict):
    print(f"{key}:{word_dict[key]}")

