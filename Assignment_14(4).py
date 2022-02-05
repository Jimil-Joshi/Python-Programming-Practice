sub = ["I","You"]
verb = ["play","love"]
object = ["hockey","Football"]


sentence_list = [(sb+" "+vb+" "+ob) for sb in sub for vb in verb for ob in object]
for sentence in sentence_list:
    print(sentence)