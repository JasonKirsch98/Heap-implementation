#!/usr/bin/python3

from Heap import Heap, find_median


def main(filename):
    #with open(filename, 'r') as reader:
    #    text = [line.strip() for line in reader]
    #    median = find_median(text)
    #    print('Median:', median)

    heap = Heap(lambda a, b: a <= b)
    heap.insert(2)
    heap.insert(3)
    heap.insert(1)
    heap.insert(5)
    heap.insert(0)
    heap.insert(4)
    heap.insert(3)
    heap.insert(4)
    heap.insert(1)
    heap.insert(10)

if __name__ == '__main__':
    main('alphabet.txt')
