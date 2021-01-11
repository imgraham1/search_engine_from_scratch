import os
import json
import numpy as np
from collections import Counter
from nltk.corpus import stopwords



with open("filtered_id_to_text.json", "r") as read_file:
    filtered_id_to_text = json.load(read_file)

with open("id_to_text.json", "r") as read_file:
    id_to_text = json.load(read_file)

filtered_ids = list(filtered_id_to_text.keys())

# with open("tf_counts.json", "r") as read_file:
#     tf_counts = json.load(read_file)

with open("tf_counts1.json", "r") as read_file:
    tf_counts1 = json.load(read_file)

with open("tf_counts2.json", "r") as read_file:
    tf_counts2 = json.load(read_file)

tf_counts = dict(tf_counts1, **tf_counts2)

corpus = list(filtered_id_to_text.values())

filtered_doc_lengths = [len(x.split()) for x in corpus]
avg_dl = sum(filtered_doc_lengths)/len(filtered_doc_lengths)
N = len(corpus)

with open("vocab.json", "r") as read_file:
    vocab = json.load(read_file)

# with open("doc_f.txt", "r") as read_file:
#     doc_f = json.load(read_file)
# doc_f = list(doc_f)
doc_f = []
f = open("doc_f.txt", "r")
for x in f:
    doc_f.append(int(x.replace('\n','')))

stops = stopwords.words('english')
punct = ['.', '?', '/', ':', ';', ',', '!', '@', '#', '$', '%', '&', '(', ')', "'", '"', '^', '_', '\\']
def clean(text):
    text = str(text)
    text = text.split()
    text = [word.lower() for word in text]
    text = [word.replace('-', ' ') for word in text]
    no_punct = []
    for x in text:
        new_text = []
        for y in x:
            if y not in punct:
                new_text.append(y)
        new_text = "".join(new_text)
        no_punct.append(new_text)

    filtered_text = [w for w in no_punct if not w in stops]
    final = " ".join(filtered_text)
    return final




query = 'sally bacon ride elephant space'


def retreive(query):
    returned_text = []
    query = str(query)
    filtered_query = []

    for x in query.split():
        if x in vocab:
            filtered_query.append(x)

    if not filtered_query:
        returned_text.append('No results found')
    else:
        query = ' '.join([str(elem) for elem in filtered_query])
        res = {}
        print('Test query: '+ query)
        query = clean(query)


        query_split = query.split()
        query_word_counts = dict(Counter(query_split))

        query_scores = []
        for doc_id in filtered_ids:

            d = filtered_id_to_text[doc_id]
            dl = len(d.split())
            # avg_dl

            doc_word_counts = tf_counts[doc_id]
        #         print(len(doc_word_counts))

            query_score = []
            for word in query_split:
                idx = vocab.index(word)
                t_f_d_t = doc_word_counts[idx]
                t_f_q_t = query_word_counts[word]
                d_f_t = doc_f[idx]
                # dl
                # avg_dl

                dfr = (((t_f_d_t*np.log(1+(avg_dl/dl)))/(1+t_f_d_t*np.log(1+(avg_dl/dl))))*np.log((N+1)/(d_f_t+0.5))*t_f_q_t)

                query_score.append(dfr)

            doc_score_for_query = sum(query_score)
            res[doc_id] = doc_score_for_query

        #sort res

        sorted_scores = dict(sorted(res.items(), key=lambda x: x[1], reverse=True))
        # sorted_scores.keys()
        returned_ids = list(sorted_scores.keys())[:10]
        # print(returned_ids)


        for x in returned_ids:
            returned_text.append(id_to_text[x])

    return returned_text


retreive(query)
