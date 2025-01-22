import random

def generate_random_arr(lenght:int):
    arr = []
    for i in range(lenght):
        arr.append(random.uniform(0, 1))

    return arr

def Py_Sort(L:list):
    if any(L):
        delta_minus = min(L)
        delta_max = max(L)

        print(delta_max)
        L.remove(delta_minus)
        L.remove(delta_max)

        delta_i = random.choice(L)
        L.remove(delta_i)

        interval = [delta_minus, delta_i, delta_max]

        for i in range(len(interval)-1):
            L_delta = Py_Sort(L)
            for delta in L_delta:
                interval.insert(delta, i)

    return interval
