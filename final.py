import json
from sentence_splitter import SentenceSplitter
from paraphrase import *
import warnings

warnings.filterwarnings("ignore")
# text1 = q1 + q2 + q3 + q4 + q5
# text2 = q6 + q7 + q8
# text3 = q9 + q10 + q11 + q12
text1 = [input("Q1- What data are you exploring? Ans: ")]
text2 = [input("Q2- What data are you exploring? Ans: ")]
text3 = [input("Q3- What data are you exploring? Ans: ")]
    # text1A = [''.join(text1)]
context1 = str(text1).strip('[]').strip("'")
splitter1 = SentenceSplitter(language='en')
sentence_list1 = splitter1.split(context1)

paraphrase1 = []
#paraphrase11 = []
#paraphrase12 = []

for i in sentence_list1:
    a = get_response(i, 1)

    paraphrase1.append(a[0])
    #paraphrase11.append(a[1])
    #paraphrase12.append(a[2])

    # paraphrase1A = [''.join(x) for x in paraphrase1]
    # paraphrase11A = [''.join(x) for x in paraphrase11]
    # paraphrase12A = [''.join(x) for x in paraphrase12]
paraphrase1A = [' '.join(x for x in paraphrase1)]
paraphrased_text1 = str(paraphrase1A).strip('[]').strip("'").strip('"')
#paraphrase11A = [' '.join(x for x in paraphrase11)]
#paraphrased_text11 = str(paraphrase11A).strip('[]').strip("'").strip('"')
#paraphrase12A = [' '.join(x for x in paraphrase12)]
#paraphrased_text12 = str(paraphrase12A).strip('[]').strip("'").strip('"')

    # text2A = [''.join(text2)]
context2 = str(text2).strip('[]').strip("'")
splitter2 = SentenceSplitter(language='en')
sentence_list2 = splitter2.split(context2)

paraphrase2 = []
#paraphrase21 = []
#paraphrase22 = []

for i in sentence_list2:
    b = get_response(i, 1)

    paraphrase2.append(b[0])
    #paraphrase21.append(b[1])
    #paraphrase22.append(b[2])

    # paraphrase2A = [''.join(x) for x in paraphrase2]
    # paraphrase21A = [''.join(x) for x in paraphrase21]
    # paraphrase22A = [''.join(x) for x in paraphrase22]

paraphrase2A = [' '.join(x for x in paraphrase2)]
paraphrased_text2 = str(paraphrase2A).strip('[]').strip("'").strip('"')
#paraphrase21A = [' '.join(x for x in paraphrase21)]
#paraphrased_text21 = str(paraphrase21A).strip('[]').strip("'").strip('"')
#paraphrase22A = [' '.join(x for x in paraphrase22)]
#paraphrased_text22 = str(paraphrase22A).strip('[]').strip("'").strip('"')

    # text3A = [''.join(text3)]
context3 = str(text3).strip('[]').strip("'")
splitter3 = SentenceSplitter(language='en')
sentence_list3 = splitter3.split(context3)

paraphrase3 = []
#paraphrase31 = []
#paraphrase32 = []

for i in sentence_list3:
    c = get_response(i, 1)

    paraphrase3.append(c[0])
    #paraphrase31.append(c[1])
    #paraphrase32.append(c[2])

    # paraphrase3A = [''.join(x) for x in paraphrase3]
    # paraphrase31A = [''.join(x) for x in paraphrase31]
    # paraphrase32A = [''.join(x) for x in paraphrase32]
paraphrase3A = [' '.join(x for x in paraphrase3)]
paraphrased_text3 = str(paraphrase3A).strip('[]').strip("'").strip('"')
#paraphrase31A = [' '.join(x for x in paraphrase31)]
#paraphrased_text31 = str(paraphrase31A).strip('[]').strip("'").strip('"')
#paraphrase32A = [' '.join(x for x in paraphrase32)]
#paraphrased_text32 = str(paraphrase32A).strip('[]').strip("'").strip('"')

#print(paraphrased_text1, paraphrased_text11, paraphrased_text12, paraphrased_text2, paraphrased_text21, paraphrased_text22, paraphrased_text3, paraphrased_text31, paraphrased_text32)
print(paraphrased_text1)
print(paraphrased_text2)
print(paraphrased_text3)
    # return json.dumps({
      #  "paragraphSuggestions": [
      #      {"options": [paraphrased_text1, paraphrased_text11, paraphrased_text12]},
       #     {"options": [paraphrased_text2, paraphrased_text21, paraphrased_text22]},
       #     {"options": [paraphrased_text3, paraphrased_text31, paraphrased_text32]}
       # ]
   # })

