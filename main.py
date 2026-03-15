import json
from fastapi import FastAPI, Depends
from fastapi.openapi.models import APIKey
from sentence_splitter import SentenceSplitter
from authorizer import get_api_key
from paraphraser import *
from schemas import ParaphraseRequest

app = FastAPI()


@app.post("/api/paraphrase")
async def paraphrase(request: ParaphraseRequest, api_key: APIKey = Depends(get_api_key)):
    # text1 = q1 + q2 + q3 + q4 + q5
    # text2 = q6 + q7 + q8
    # text3 = q9 + q10 + q11 + q12
    text1 = request.paraphrase[0]
    text2 = request.paraphrase[1]
    text3 = request.paraphrase[2]

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

    return json.dumps({
        "paragraphSuggestions": [
            {"options": [paraphrased_text1]},
            {"options": [paraphrased_text2]},
            {"options": [paraphrased_text3]}
        ]
    })
