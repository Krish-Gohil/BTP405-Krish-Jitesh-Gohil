# Provide your test implementation here
import random
import time
import matplotlib.pyplot as plt
from q6_sort import Vehicle, sort, selection_sort, merge_sort, bubble_sort

def main():
    #the function to select random test sets from the list
    def generate_vehicles(num_vehicles):
        manufacturers = ['Bugatti', 'Pagani', 'Koenigsegg', 'Aston Martin', 'Maserati']
        models = ['Chiron', 'Huayra', 'Jesko', 'DB11', 'Ghibli']
        types = ['sedan', 'coupe', 'SUV', 'truck']

        vehicles = [
            Vehicle(
                random.choice(manufacturers),
                random.choice(models),
                random.choice(types),
                random.randint(10000, 100000), 
                random.randint(5000, 200000),  
            )
            for _ in range(num_vehicles)
        ]
        return vehicles
    # function to measure the time taken by each of the sorting algorithms
    def measure_performance(sort_alg, lst_sizes):
        results = []
        for size in lst_sizes:
            vehicles = generate_vehicles(size)
            start_time = time.time()
            sort(vehicles, sort_alg)
            end_time = time.time()
            results.append(end_time - start_time)
        return results

    def main():
        lst_sizes = [10, 50, 100, 500, 1000]
        algorithms = {"Selection Sort": selection_sort,
                      "Merge Sort": merge_sort,
                      "Bubble Sort": bubble_sort}

        # Measure and plot performance
        for alg_name, alg_func in algorithms.items():
            times = measure_performance(alg_func, lst_sizes)
            plt.plot(lst_sizes, times, label=alg_name)

        # Plot settings
        plt.title("Sorting Algorithm Performance")
        plt.xlabel("List Size")
        plt.ylabel("Execution Time (seconds)")
        plt.legend()
        plt.grid()
        plt.show()

        # Test with random data and display sorted results
        test_vehicles = generate_vehicles(10)
        print("\nUnsorted Vehicles:")
        for vehicle in test_vehicles:
            print(vehicle)

        print("\nSorted Vehicles (by cost, using Merge Sort):")
        sorted_vehicles = sort(test_vehicles, merge_sort)
        for vehicle in sorted_vehicles:
            print(vehicle)

    if __name__ == "__main__":
        main()
if __name__ == "__main__":
    main()
