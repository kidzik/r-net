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


def get_list(test_str, procedure):
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
    for _ in range(len(rows)):
        row = our_queue.get()
        row[1].append(-row[0][(0,0)])
        if procedure in row[1][3]:
            best_list.append(row[1])
            if len(best_list) == 5:
                break

    
    return best_list
