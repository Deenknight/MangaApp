import threading
import time
import concurrent.futures

start  = time.perf_counter()

def do_something(seconds):
    print(f'Sleep {seconds} second(s)...')
    time.sleep(seconds)
    return 'Done sleeping...'


# do_something()
# do_something()


#basic idea of threading: 

# t1 = threading.Thread(target=do_something)
# t2 = threading.Thread(target=do_something)

# t1.start()
# t2.start()

# t1.join()
# t2.join()

#------------------------------------------------------------------------------------------------

with concurrent.futures.ThreadPoolExecutor() as executor:
    # f1 = executor.submit(do_something, 1) #submit method schedules a funciton to be executed and returnes a future object.
    #                                       #A future object encapuslates the execution of a funciton and allows us to check in on it runs 
    #                                       #We can see the status of it and the result of the functioin call
    # f2 = executor.submit(do_something, 1)

    seconds = [5, 4, 3, 2, 1]

    #resluts = executor.map(do_something, seconds)

    results = [executor.submit(do_something, second) for second in seconds]

    for f in concurrent.futures.as_completed(results):
        print(f.result())


#----------------------------------------------------------------------------------------

#Threads using the threading module

# threads = []

# for _ in range(10): # _ in the for loop is just a throw away variable because we are not doing anything with it
#     t = threading.Thread(target=do_something, args=[1.5]) #args passes the parameters into the funciton thats being called 
#     t.start()
#     threads.append(t)

# for thread in threads:
#     thread.join()


finish = time.perf_counter()

print(f"Finished in {round(finish - start, 2)} second(s)")