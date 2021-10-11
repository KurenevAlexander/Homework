import threading
from time import sleep


def philosophers_dinner(right_fork, left_fork, philosopher):
    while True:
        # Take forks
        first_fork = min(right_fork, left_fork)
        second_fork = max(right_fork, left_fork)
        forks_lock[first_fork].acquire()
        forks_lock[second_fork].acquire()
        print(f'Philosopher {philosopher} is eating! ')
        sleep(1)
        # Put forks
        forks_lock[second_fork].release()
        forks_lock[first_fork].release()
        print(f'Philosopher {philosopher} is thinking! ')
        sleep(1)


if __name__ == '__main__':
    forks = 5
    philosophers = 5

    forks_lock = [threading.Lock() for n in range(forks)]

    for philosopher in range(philosophers):
        right_fork = philosopher
        left_fork = (philosopher + 1) % philosophers
        threading.Thread(target=philosophers_dinner, args=(right_fork, left_fork, philosopher)).start()
