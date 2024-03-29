import time
import numpy as np
from tqdm import tqdm
import multiprocessing
from tqdm.contrib.concurrent import process_map

N_PROCESS = 20
tasks = np.arange(100)


def run(task):
    print(f'start processing task {task} ...')
    time.sleep(10)
    print(f'finish processing task {task} .')


if __name__ == "__main__":

    if N_PROCESS > 0:
        with multiprocessing.Pool(N_PROCESS) as pool:
            list(tqdm(pool.imap(run, tasks), total=len(tasks), desc='overall'))
    else:
        for scene in tqdm(tasks, desc='overall'):
            run(scene)
    
    # using tqdm process_map would be much much simpler
    process_map(run, tasks, max_workers=N_PROCESS)
