#Implementation of Quick Sort
#arr[] -- array to sort; low -- starting index; high -- ending index
from random import seed
from random import randint


def partition(arr, low, high):
    i = (low -1)
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] <= pivot:
            i=i+1
            arr[i], arr[j]=arr[j], arr[i]
    arr[i+1], arr[high]= arr[high], arr[i+1]
    return (i+1)

def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        pivot = partition(arr, low, high)
        quickSort(arr, low, pivot-1)
        quickSort(arr, pivot+1, high)

def listConverter(array_values):
    n=len(array_values)
    arr = [None]*n
    #for i in range(n):
    #    arr[i] = (int(array_values[i])
    arr=list(map(int, array_values))
    #array=[int(num) for num in array_values]
    return arr

def fileInput():
    fileName = 'list-data.txt'
    fileObject = open(fileName, "r")
    array_values = fileObject.read().splitlines()
    fileObject.close()
    print("The values in the array from the file are", array_values)
    return listConverter(array_values)

def randomGenerator(n):
    seed(1)
    print("Generating " + str(n) + " Random Numbers into an array")
    array_values = [None] * n
    for i in range(n):
        array_values[i] = randint(0, n)
    print("The Random Numbers are",array_values)
    return array_values

def consoleInput():
    array_values=input("Enter all the values of arrays (separated by space):")
    n=len(array_values)
    print("The list you entered on the console are", array_values)
    return listConverter(array_values.strip().split()[:n])

def main():
    #to accept an array from the console and sort it
    arr = consoleInput()
    #to accept an array of numbers from a file 'list-data.txt'
    #arr = fileInput()
    #to randomly generate numbers into an array and sort them
    #arr = randomGenerator(30)
    n=len(arr)
    quickSort(arr, 0, n-1)
    print("Sorted Array is:")
    for i in range(n):
        print(arr[i])

if __name__ == '__main__':
    main()