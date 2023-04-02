import genetic_algorithm
import brute_force
import local_beam
import branch_and_bound
import time
import tracemalloc


if __name__ == "__main__":
    opt = int(input("Nhập lựa chọn 1. bruteforce 2. branch&bound 3. localbeam 4. geneticalgo: "))
    if opt == 1:
        start_time = time.time()
        tracemalloc.start()
        brute_force.solve(opt)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        end_time = time.time()
        print(f"Thời gian chạy của hàm: {(end_time - start_time) * 1000} ms")
        print(f"Bộ nhớ đã sử dụng: {current / 1024**2:.2f} MB")
    elif opt == 4:
        start_time = time.time()
        tracemalloc.start()
        genetic_algorithm.solve(opt)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        end_time = time.time()
        print(f"Thời gian chạy của hàm: {(end_time - start_time) * 1000} ms")
        print(f"Bộ nhớ đã sử dụng: {current / 1024**2:.2f} MB")
    elif opt == 3:
        start_time = time.time()
        tracemalloc.start()
        local_beam.solve(opt)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        end_time = time.time()
        print(f"Thời gian chạy của hàm: {(end_time - start_time) * 1000} ms")
        print(f"Bộ nhớ đã sử dụng: {current / 1024**2:.2f} MB")
    elif opt == 2:
        start_time = time.time()
        tracemalloc.start()
        branch_and_bound.solve(opt)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        end_time = time.time()
        print(f"Thời gian chạy của hàm: {(end_time - start_time) * 1000} ms")
        print(f"Bộ nhớ đã sử dụng: {current / 1024**2:.2f} MB")
    else:
        print("Không hợp lệ")