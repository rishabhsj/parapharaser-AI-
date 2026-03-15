from sentence_splitter import SentenceSplitter
from flask import Flask, jsonify, redirect, url_for, render_template, request, json
from flask_restful import Api, Resource
from paraphrase import *
import warnings

warnings.filterwarnings("ignore")

#  Run paraphrase.py before running this file.

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def home():
    return render_template("index.html")


@app.route("/para", methods=["POST", "GET"])
def main():
    # text1 = q1 + q2 + q3 + q4 + q5
    # text2 = q6 + q7 + q8
    # text3 = q9 + q10 + q11 + q12

    text1 = request.form['t1']
    text2 = request.form['t2']
    text3 = request.form['t3']

    ######  Text 1 #####
    print("\n * * * * * * * * * * ANSWER 1 * * * * * * * * * * \n")

    print("\nInput into paraphraser 1 :\n")
    text1A = [''.join(text1)]
    context1 = str(text1A).strip('[]').strip("'")
    print(context1)
    print()

    # Takes the input paragraph and splits it into a list of sentences
    splitter1 = SentenceSplitter(language='en')

    sentence_list1 = splitter1.split(context1)
    print(sentence_list1)

    # Do a for loop to iterate through the list of sentences and paraphrase each sentence in the iteration
    paraphrase1 = []
    paraphrase11 = []
    paraphrase12 = []

    for i in sentence_list1:
        a = get_response(i, 3)
        paraphrase1.append(a[0])
        paraphrase11.append(a[1])
        paraphrase12.append(a[2])

    print("\nthe paraphrased text:\n")
    # This is the paraphrased text
    print(paraphrase1)
    print(paraphrase11)
    print(paraphrase12)

    # Joining paraphrased text
    print("\nJoining Paraphrased text:\n")
    paraphrase1A = [''.join(x) for x in paraphrase1]
    print(paraphrase1A)

    paraphrase11A = [''.join(x) for x in paraphrase11]
    print(paraphrase11A)

    paraphrase12A = [''.join(x) for x in paraphrase12]
    print(paraphrase12A)

    # Combines the above list into a paragraph
    paraphrase1B = [' '.join(x for x in paraphrase1A)]
    paraphrased_text1 = str(paraphrase1B).strip('[]').strip("'").strip('"')
    print(paraphrased_text1)

    paraphrase11B = [' '.join(x for x in paraphrase11A)]
    paraphrased_text11 = str(paraphrase11B).strip('[]').strip("'").strip('"')
    print(paraphrased_text11)

    paraphrase12B = [' '.join(x for x in paraphrase12A)]
    paraphrased_text12 = str(paraphrase12B).strip('[]').strip("'").strip('"')
    print(paraphrased_text12)

    # Comparison of the original (context variable) and the paraphrased version (paraphrase3 variable)
    print(".......................................................................")
    print("\noriginal Text 1:")
    print(context1)
    print("\nParaphrased Paragraph, Answer 1 - option 1:\n")
    print(paraphrased_text1)
    print("\nParaphrased Paragraph, Answer 1 - option 2:\n")
    print(paraphrased_text11)
    print("\nParaphrased Paragraph, Answer 1 - option 3:\n")
    print(paraphrased_text12)
    print(".......................................................................")

    ######  Text 2 #####

    print("\n * * * * * * * * * * ANSWER 2 * * * * * * * * * * \n")
    text2 = request.form['t2']
    print("\nInput into paraphraser 2 :\n")
    text2A = [''.join(text2)]
    context2 = str(text2A).strip('[]').strip("'")
    print(context2)
    print()

    # Takes the input paragraph and splits it into a list of sentences
    splitter2 = SentenceSplitter(language='en')

    sentence_list2 = splitter2.split(context2)
    print(sentence_list2)

    # Do a for loop to iterate through the list of sentences and paraphrase each sentence in the iteration
    paraphrase2 = []
    paraphrase21 = []
    paraphrase22 = []

    for i in sentence_list2:
        b = get_response(i, 3)
        paraphrase2.append(b[0])
        paraphrase21.append(b[1])
        paraphrase22.append(b[2])

    print("\nthe paraphrased text:\n")
    # This is the paraphrased text
    print(paraphrase2)
    print(paraphrase21)
    print(paraphrase22)

    print("\nJoining Paraphrased text:\n")
    # Joining paraphrased text
    paraphrase2A = [''.join(x) for x in paraphrase2]
    print(paraphrase2A)

    paraphrase21A = [''.join(x) for x in paraphrase21]
    print(paraphrase21A)

    paraphrase22A = [''.join(x) for x in paraphrase22]
    print(paraphrase22A)

    # Combines the above list into a paragraph
    paraphrase2B = [' '.join(x for x in paraphrase2A)]
    paraphrased_text2 = str(paraphrase2B).strip('[]').strip("'").strip('"')
    print(paraphrased_text2)

    paraphrase21B = [' '.join(x for x in paraphrase21A)]
    paraphrased_text21 = str(paraphrase21B).strip('[]').strip("'").strip('"')
    print(paraphrased_text21)

    paraphrase22B = [' '.join(x for x in paraphrase22A)]
    paraphrased_text22 = str(paraphrase22B).strip('[]').strip("'").strip('"')
    print(paraphrased_text22)

    # Comparison of the original (context variable) and the paraphrased version (paraphrase3 variable)
    print("\noriginal Text 2 :\n")
    print(context2)
    print("\nParaphrased Paragraph, Answer 2 - option 1:\n")
    print(paraphrased_text2)
    print("\nParaphrased Paragraph, Answer 2 - option 2:\n")
    print(paraphrased_text21)
    print("\nParaphrased Paragraph, Answer 2 - option 3:\n")
    print(paraphrased_text22)
    print("........................................................")


    ######  Text 3 #####
    print("\n * * * * * * * * * * ANSWER 3 * * * * * * * * * * \n")
    text3 = request.form['t3']
    print("\nInput into paraphraser 3 :\n")
    text3A = [''.join(text3)]
    context3 = str(text3A).strip('[]').strip("'")
    print(context3)
    print()

    # Takes the input paragraph and splits it into a list of sentences
    splitter3 = SentenceSplitter(language='en')

    sentence_list3 = splitter3.split(context3)
    print(sentence_list3)

    # Do a for loop to iterate through the list of sentences and paraphrase each sentence in the iteration
    paraphrase3 = []
    paraphrase31 = []
    paraphrase32 = []

    for i in sentence_list3:
        c = get_response(i, 3)
        paraphrase3.append(c[0])
        paraphrase31.append(c[1])
        paraphrase32.append(c[2])

    print("\nthe paraphrased text:\n")
    # This is the paraphrased text
    print(paraphrase3)
    print(paraphrase31)
    print(paraphrase32)

    print("\nJoining Paraphrased text:\n")
    # Joining paraphrased text
    paraphrase3A = [''.join(x) for x in paraphrase3]
    print(paraphrase3A)

    paraphrase31A = [''.join(x) for x in paraphrase31]
    print(paraphrase31A)

    paraphrase32A = [''.join(x) for x in paraphrase32]
    print(paraphrase32A)

    # Combines the above list into a paragraph
    paraphrase3B = [' '.join(x for x in paraphrase3A)]
    paraphrased_text3 = str(paraphrase3B).strip('[]').strip("'").strip('"')
    print(paraphrased_text3)

    paraphrase31B = [' '.join(x for x in paraphrase31A)]
    paraphrased_text31 = str(paraphrase31B).strip('[]').strip("'").strip('"')
    print(paraphrased_text31)

    paraphrase32B = [' '.join(x for x in paraphrase32A)]
    paraphrased_text32 = str(paraphrase32B).strip('[]').strip("'").strip('"')
    print(paraphrased_text32)

    # Comparison of the original (context variable) and the paraphrased version (paraphrase3 variable)
    print("original Text 3 :\n")
    print(context3)
    print("\nParaphrased Paragraph, Answer 3 - option 1:\n")
    print(paraphrased_text3)
    print("\nParaphrased Paragraph, Answer 3 - option 2:\n")
    print(paraphrased_text31)
    print("\nParaphrased Paragraph, Answer 3 - option 3:\n")
    print(paraphrased_text32)

    return json.dumps({'pt1': paraphrased_text1, 'pt11': paraphrased_text11, 'pt12': paraphrased_text12, 'pt2': paraphrased_text2, 'pt21': paraphrased_text21, 'pt22': paraphrased_text22, 'pt3': paraphrased_text3, 'pt31': paraphrased_text31, 'pt32': paraphrased_text32});


if __name__ == "__main__":
    app.run(debug=True)