from time import time
from matplotlib import pyplot as plt


def fibonacci(steps):
    numbers = [1, 2]

    for step in range(steps):
        numbers.append(numbers[-1] + numbers[-2])


def main():
    step = int(input("Step:"))
    times = []
    iterations = []
    max_tests = int(input("Max tests: "))
    for i in range(1, max_tests):
        fibonacci_cap = i * step

        time_start = time()

        fibonacci(fibonacci_cap)

        time_end = time()

        time_taken = time_end - time_start

        times.append(time_taken)

        iterations.append(fibonacci_cap)

        percentage_done = ((i/max_tests)*100)
        print("%.2f" % round(percentage_done, 2) + "%")

    total_time = 0
    for i in times:
        total_time + int(i)

    print("==================================")
    print(f"Total time: {total_time}")

    # Matplotlib
    x = iterations
    y = times

    plt.plot(x, y)
    plt.xlabel("Fibonacci Iterations")
    plt.ylabel("Time taken")
    plt.title("Fibonacci Iterations / Time")
    plt.show()


if __name__ == "__main__":
    main()
