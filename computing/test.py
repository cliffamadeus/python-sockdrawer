import multiprocessing
import time

# Function to sum a range of numbers
def add_range(start, end, result, index):
    result[index] = sum(range(start, end + 1))

if __name__ == "__main__":
    # Number of processes (use your 6 cores)
    num_processes = 6
    n = 1_000_000
    chunk_size = n // num_processes

    # Shared memory array to store partial sums
    manager = multiprocessing.Manager()
    result = manager.list([0] * num_processes)

    processes = []
    start_time = time.time()

    for i in range(num_processes):
        start_val = i * chunk_size + 1
        end_val = (i + 1) * chunk_size if i < num_processes - 1 else n
        p = multiprocessing.Process(target=add_range, args=(start_val, end_val, result, i))
        processes.append(p)
        p.start()

    # Wait for all processes to finish
    for p in processes:
        p.join()

    total = sum(result)
    end_time = time.time()

    print(f"Total sum: {total}")
    print(f"Time elapsed using {num_processes} processes: {end_time - start_time:.4f} seconds")
