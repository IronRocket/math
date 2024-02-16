import multiprocessing,os

mem = ''

def stresser():
    global mem
    f = 0.234
    while True:
        f = f * 0.6723 + 2.3431
        mem += str(f)*90000
    return
if __name__ == '__main__':
    for _ in range(os.cpu_count()):
        multiprocessing.Process(target=stresser).start()