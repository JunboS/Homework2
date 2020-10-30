import random
if __name__ == '__main__':
    f = open("1a.csv", "a")
    numbers = []
    for x in range(1000):
        numbers.append(random.randint(0, 100))
    #sort
    numbers.sort()
    for num in numbers:
        f.write(str(num)+'\n')

    print(numbers)
    f.close()
