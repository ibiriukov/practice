import time

from multiprocess.pool import Pool


def task_a():
    time.sleep(2)
    return "A Passed"

def task_b():
    time.sleep(2)
    return "B Passed"

def task_c():
    time.sleep(2)
    return "C Passed"

if __name__ == "__main__":
    start = time.time()  # ⏱️ Start timer
    with Pool(3) as pool:
        result = pool.map(lambda f: f(), [task_a, task_b, task_a])
        end = time.time()  # ⏱️ End timer

    print(result)
    print(f"Took {end - start:.2f} seconds")
