import random
import time

def selection_sort(list):
    comparsionCount = 0
    for i in range(len(list) - 1):
        #compare list[i] with next index, if smaller -> continue, if larger -> swap
        smallest = i
        # comparing rest of the list with current index
        for restIndex in range(i + 1, len(list)):
            #add one to comparison counter
            comparsionCount += 1
            if list[smallest] > list[restIndex]:
                smallest = restIndex
        if i != smallest:
            swap(list, i, smallest)
    #selection sort goes through the whole list!
    return comparsionCount

def swap(list, i, smallest):
    #create temporary saved value of larger number
    temp = list[i]
    #set the current index spot to the smallest number
    list[i] = list[smallest]
    #set the new index to the larger number
    list[smallest] = temp
    

def insertion_sort(list):
    comparsionCount = 0

    for i in range(1, len(list)):
        for j in range(i):
            comparsionCount += 1
            if list[i - j] < list[i - j - 1]:
                temp = list[i - j]
                temp2 = list[i - j - 1]
                list[i-j-1] = temp
                list[i-j] = temp2
            else:
                break

    return comparsionCount
   

def main():
    # Code coverage NOT required for main
    # Give the random number generator a seed, so the same sequence of 
    # random numbers is generated at each run
    random.seed(1234) 
    
    # Generate 5000 random numbers from 0 to 999,999
    randoms = random.sample(range(1000000), 1000)
    start_time = time.time() 
    comps = insertion_sort(randoms)
    stop_time = time.time()
    print(comps, stop_time - start_time)

if __name__ == '__main__': 
    main()

