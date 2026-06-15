import time

def func():
    a = 6
    a = 6 * 2
    return a

if __name__=='__main__':
    start = time.time()

    result = func()

    end = time.time()

    print(f'\n\nProgram returned: {result}\n=== Executed in {round((end - start) * 1000, 6)} ms. ===')