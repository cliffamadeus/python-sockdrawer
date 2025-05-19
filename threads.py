import threading
import time

def add_range(start, end, result, index, lock):
    partial = sum(range(start, end + 1))
    with lock:
        result[index] = partial

def run_sum_with_threads(num_threads, n=1_000_000):
    chunk_size = n // num_threads
    result = [0] * num_threads
    threads = []
    lock = threading.Lock()

    start_time = time.time()

    for i in range(num_threads):
        start_val = i * chunk_size + 1
        end_val = (i + 1) * chunk_size if i < num_threads - 1 else n
        thread = threading.Thread(target=add_range, args=(start_val, end_val, result, i, lock))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    total = sum(result)
    elapsed = time.time() - start_time
    return total, elapsed

if __name__ == "__main__":
    print("🧵 Summing numbers from 1 to 1,000,000 using multiple threads\n")
    for threads in range(2, 7):  # From 2 to 6 threads
        total, elapsed = run_sum_with_threads(threads)
        print(f"{threads} thread(s): Total = {total}, Time = {elapsed:.6f} seconds")
