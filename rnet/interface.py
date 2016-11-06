import csv
import pickle
import Queue
import numpy as np
import csv

def cosine_similarity(vector1, vector2):
    # dot_product = sum(p*q for p,q in zip(vector1, vector2))
    dot_product = np.dot(vector1,vector2.T)
    magnitude = np.sqrt((vector1.dot(vector1.T).sum())) * np.sqrt(vector2.dot(vector2.T).sum())
    # magnitude = math.sqrt(sum([val**2 for val in vector1])) * math.sqrt(sum([val**2 for val in vector2]))
    if not magnitude:
        return 0
    return dot_product/magnitude


test_str = "Chest cavity lung tube"


def get_list(test_str):
    storage = pickle.load(open("rnet/demo_matrix.p", "rb"))

    rows = []
    with open('data.csv', 'rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in spamreader:
            rows.append(row)

    vectorizer = storage[0]
    representation = storage[1]

    input_vector = vectorizer.transform([test_str])

    our_queue = Queue.PriorityQueue()
    for i in range(representation.shape[0]):
        val = -1 * cosine_similarity(representation[i,:],input_vector)
        our_queue.put((val, rows[i+1]))

    best_list = []
    for _ in range(5):
        best_list.append(our_queue.get()[1])

    return best_list
