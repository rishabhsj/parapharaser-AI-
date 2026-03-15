import json


from sentence_splitter import SentenceSplitter

from paraphrase import *





# text1 = q1 + q2 + q3 + q4 + q5
    # text2 = q6 + q7 + q8
    # text3 = q9 + q10 + q11 + q12
text1 = [input("Q1- What data are you exploring? Ans: ")]
text2 = [input("Q1- What data are you exploring? Ans: ")]
text3 = [input("Q1- What data are you exploring? Ans: ")]

context1 = str(text1).strip('[]').strip("'")
splitter1 = SentenceSplitter(language='en')
sentence_list1 = splitter1.split(context1)

paraphrase1 = []

for i in sentence_list1:
    a = get_response(i, 1)
    paraphrase1.append(a[0])

paraphrase1A = [' '.join(x for x in paraphrase1)]
paraphrased_text1 = str(paraphrase1A).strip('[]').strip("'").strip('"')

context2 = str(text2).strip('[]').strip("'")
splitter2 = SentenceSplitter(language='en')
sentence_list2 = splitter2.split(context2)

paraphrase2 = []

for i in sentence_list2:
    b = get_response(i, 1)
    paraphrase2.append(b[0])

paraphrase2A = [' '.join(x for x in paraphrase2)]
paraphrased_text2 = str(paraphrase2A).strip('[]').strip("'").strip('"')

context3 = str(text3).strip('[]').strip("'")
splitter3 = SentenceSplitter(language='en')
sentence_list3 = splitter3.split(context3)

paraphrase3 = []

for i in sentence_list3:
    c = get_response(i, 1)
    paraphrase3.append(c[0])

paraphrase3A = [' '.join(x for x in paraphrase3)]
paraphrased_text3 = str(paraphrase3A).strip('[]').strip("'").strip('"')

print(paraphrased_text1, paraphrased_text3, paraphrased_text2)
