
import csv
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.tokenize import word_tokenize
import Queue
import pickle
g = open("stop-word-list.csv", "r")
stop_csv = csv.reader(g)
for line in stop_csv:
    invalid_words = line
invalid_words.append(".")
invalid_words.append(",")
f = open("patientdata.csv", "rb")
our_csv = csv.DictReader(f)

all_documents = []
for line in our_csv:
    our_results = word_tokenize(line["Impression"])
    output_str = ""
    for word in our_results:
        if word.lower() == "electronically":
            break
        output_str += word
    all_documents.append(output_str)
            

sklearn_tfidf = TfidfVectorizer(norm='l2',min_df=0, use_idf=True, smooth_idf=False, sublinear_tf=True, stop_words = invalid_words)
sklearn_representation = sklearn_tfidf.fit_transform(all_documents)


########### END BLOG POST 1 #############

def cosine_similarity(vector1, vector2):
    # dot_product = sum(p*q for p,q in zip(vector1, vector2))
    dot_product = np.dot(vector1,vector2.T)
    magnitude = np.sqrt((vector1.dot(vector1.T).sum())) * np.sqrt(vector2.dot(vector2.T).sum())
    # magnitude = math.sqrt(sum([val**2 for val in vector1])) * math.sqrt(sum([val**2 for val in vector2]))
    if not magnitude:
        return 0
    return dot_product/magnitude

print("Shape of matrix is", sklearn_representation.shape)
best_vals = dict()
for v1 in range(sklearn_representation.shape[0]):
    best_match = []
    our_queue = Queue.PriorityQueue()
    vector1 = sklearn_representation[v1,:]
    for v2 in range(sklearn_representation.shape[0]):
        vector2 = sklearn_representation[v2,:]
        # print("Vector 2 shape is", vector2.shape)
        # print("Vector 2 is {0} on iteration {1}".format(vector2,v1))
        if v1 != v2:
            our_queue.put((-1*cosine_similarity(vector1,vector2),v2))
    for _ in range(5):
        best_match.append(our_queue.get()[1])
    best_vals[v1] = best_match[:]
    print(best_match)
    print("v1 is ", v1)

pickle.dump(best_vals, open("true_match.p", "wb"))

    # top_indices = []
    # for key2,val2 in our_model_dict.items():
    #     if int(key1) != int(key2):
    #         our_queue.put((-1*np.dot(val1,val2), key2))

# skl_tfidf_comparisons = []
# for count_0, doc_0 in enumerate(sklearn_representation.toarray()):
#     for count_1, doc_1 in enumerate(sklearn_representation.toarray()):
#         skl_tfidf_comparisons.append((cosine_similarity(doc_0, doc_1), count_0, count_1))

# for x in zip(sorted(our_tfidf_comparisons, reverse = True), sorted(skl_tfidf_comparisons, reverse = True)):
# print x