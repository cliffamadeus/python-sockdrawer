import threading
import time

def partial_sum(start, end, result, index, lock):
    partial = sum(range(start, end + 1))
    with lock:
        result[index] = partial

def chunkify(n, num_chunks):
    chunk_size = n // num_chunks
    ranges = []
    for i in range(num_chunks):
        start = i * chunk_size + 1
        end = (i + 1) * chunk_size if i < num_chunks - 1 else n
        ranges.append((start, end))
    return ranges

if __name__ == "__main__":
    n = 1_000_000
    num_threads = 12
    ranges = chunkify(n, num_threads)
    result = [0] * num_threads
    lock = threading.Lock()
    threads = []

    start_time = time.time()

    for i, (start, end) in enumerate(ranges):
        t = threading.Thread(target=partial_sum, args=(start, end, result, i, lock))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    total = sum(result)
    elapsed = time.time() - start_time

    print(f"✅ Total Sum: {total}")
    print(f"⏱️ Time Elapsed with {num_threads} threads: {elapsed:.6f} seconds")
