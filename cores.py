import multiprocessing
import time

def add_range(start, end, result, index):
    result[index] = sum(range(start, end + 1))

def run_sum_with_cores(num_cores, n=1_000_000):
    chunk_size = n // num_cores
    manager = multiprocessing.Manager()
    result = manager.list([0] * num_cores)
    processes = []

    start_time = time.time()

    for i in range(num_cores):
        start_val = i * chunk_size + 1
        end_val = (i + 1) * chunk_size if i < num_cores - 1 else n
        p = multiprocessing.Process(target=add_range, args=(start_val, end_val, result, i))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    total = sum(result)
    elapsed = time.time() - start_time
    return total, elapsed

if __name__ == "__main__":
    print("🔢 Summing numbers from 1 to 1,000,000 using multiple cores\n")
    for cores in range(2, 7):  # 2 to 6 cores
        total, elapsed = run_sum_with_cores(cores)
        print(f"{cores} core(s): Total = {total}, Time = {elapsed:.6f} seconds")
