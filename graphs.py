import matplotlib.pyplot as plt
 

n_threads = [1, 2, 4, 8, 16, 32, 64]

strong_execution_time = [232.35049,143.01559,122.61784,127.49436, 127.84637, 130.88936,132.10750]

weak_execution_times = {
    500:[1.20321, 0.75635, 0.62305, 0.77873, 1.01364, 1.30851, 2.03356],
    1000:[9.73181, 5.31618, 4.66866, 5.97572, 5.20906, 6.64351, 7.75238],
    2000:[71.91449, 38.74901, 35.88454, 38.18606, 38.94682, 40.09959, 43.42272],
    3000:[228.07297, 124.44515, 115.93783, 121.36709, 119.50104, 121.72322, 127.62453],
    4000:[530.41616, 280.25995, 264.38530, 273.01334, 271.05800, 272.29612, 274.04530]  
}

ideal_strong = strong_execution_time[0]
ideal_weak = [(n,times[0]) for n,times in weak_execution_times.items()]
ideal_weak = dict(ideal_weak)

def speedup_data_weak(n,times,ideal):
    
    if type(ideal) == list:
        for t in times:
            t = ideal[n] / t
    return times



def strong_graph():

    data = [ideal_strong/time for time in strong_execution_time]

    plt.figure(figsize=(10, 6))
    plt.xlabel("Number of Threads")
    plt.ylabel("Speedup")
    plt.title("Speedup vs. Number of Threads")
    plt.xticks(n_threads)
    plt.legend()
    plt.grid(True)
    plt.plot(n_threads, data, marker='o', linestyle='-')
    plt.show()


def weak_graph():

    plt.figure(figsize=(10, 6))
    plt.xlabel("Number of Threads")
    plt.ylabel("Speedup")
    plt.title("Speedup vs. Number of Threads")
    plt.xticks(n_threads)
    plt.grid(True)

    for n,ideal_t in ideal_weak.items():
        n_times = [ideal_t/time for time in weak_execution_times[n]]
        plt.plot(n_threads, n_times, marker='o', linestyle='-', label=f"N dimension = {n}")
        
    plt.legend()
    plt.show()

weak_graph()