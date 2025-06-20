
import numpy as np

def find_students(table, min_score):
    id_num = []
    for row in table:
        student_id = row[0]
        scores = row[1:]
        if np.any(scores >= min_score):
            id_num.append(student_id)
    id_num_array = np.array(id_num, dtype=np.int64)
    tot_std = np.int64(len(id_num_array))
    return id_num_array, tot_std

if __name__ == "__main__":
    table = np.loadtxt("scores.csv", delimiter=",")
    min_score = 90
    id_num, tot_std = find_students(table, min_score)
    print("IDs:", id_num)
    print("Total:", tot_std)
