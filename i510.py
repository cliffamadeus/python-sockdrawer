import multiprocessing
import time

def partial_sum(start, end):
    return sum(range(start, end + 1))

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
    num_cores = multiprocessing.cpu_count()  # Your CPU has 12 threads
    ranges = chunkify(n, num_cores)

    start_time = time.time()

    with multiprocessing.Pool(processes=num_cores) as pool:
        results = pool.starmap(partial_sum, ranges)

    total = sum(results)
    elapsed = time.time() - start_time

    print(f"✅ Total Sum: {total}")
    print(f"⏱️ Time Elapsed with {num_cores} processes: {elapsed:.6f} seconds")
