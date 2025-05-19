import multiprocessing
import time

def add_range(start, end, result, index):
    result[index] = sum(range(start, end + 1))

def run_sum_with_processes(num_procs, n=1_000_000):
    chunk_size = n // num_procs
    manager = multiprocessing.Manager()
    result = manager.list([0] * num_procs)
    processes = []

    start_time = time.time()

    for i in range(num_procs):
        start_val = i * chunk_size + 1
        end_val = (i + 1) * chunk_size if i < num_procs - 1 else n
        p = multiprocessing.Process(target=add_range, args=(start_val, end_val, result, i))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    total = sum(result)
    elapsed = time.time() - start_time
    return total, elapsed

if __name__ == "__main__":
    print("⚙️ Multiprocessing Benchmark\n")
    overall_start = time.time()

    for procs in range(2, 7):
        total, elapsed = run_sum_with_processes(procs)
        print(f"{procs} process(es): Total = {total}, Time = {elapsed:.6f} seconds")

    overall_end = time.time()
    print(f"\n🧮 Total time for all multiprocessing computations: {overall_end - overall_start:.6f} seconds")
