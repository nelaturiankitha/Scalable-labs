from time import perf_counter
from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Pool
from multiprocessing import cpu_count
start_time = perf_counter()

 
def square(number):
    return number ** 2 

if __name__ == "__main__":
    numbers = range(1000)

    with Pool(processes=1) as pool:
        results = pool.map(square, numbers) 

    print(sorted(results))

finish_time = perf_counter()
print( "Code took {} seconds".format(finish_time-start_time))
print(cpu_count()) # the result is 12

#####################################################################################################################################################################

# The result for first is :- Code took 0.0023865000111982226 seconds

# def square(number):
#     return number ** 2

# numbers = range(1000)

# results = list()
# for number in numbers:
#     result = results.append(square(number))

# print(results)

#####################################################################################################################################################################

# The result for second is :- Code took 0.015215200022794306 seconds

# def square(number):
#     return number ** 2

# numbers = range(1000)

# with ThreadPoolExecutor(max_workers=3) as executor:
#     results = executor.map(square, numbers)

# print(sorted(results))


#####################################################################################################################################################################

# Result of third scenario :- Code took 0.09379490010906011 seconds

#  def square(number):
#     return number ** 2 

# if __name__ == "__main__":
#     numbers = range(1000)

#     with Pool(processes=1) as pool:
#         results = pool.map(square, numbers) 

#     print(sorted(results))


# I had a error related to Pool module; wrapping the main part of the script in the if __name__ == "__main__": block. This is necessary to prevent the multiprocessing code from being executed when the script is imported as a module.