import time

def time_function_execution():
    # Replace the following line with the function or operation you want to measure
    # For example, you can replace it with a function call like: my_function()
    result = sum(range(1, 1000001))

    return result

if __name__ == "__main__":
    start_time = time.time()

    # Call the function or perform the operation you want to measure
    result = time_function_execution()

    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"Result: {result}")
    print(f"Time Elapsed: {elapsed_time} seconds")
