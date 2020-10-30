if __name__ == '__main__':
    input_file = open("1a.csv", "r")
    output_file = open("1b.csv", "a")
    lines = input_file.readlines()
    numbers =[]
    for line in lines:
        x=int(line.strip())
        y = 3*x+6
        output_file.write(str(y)+'\n')
        numbers.append(y)
    print(numbers)
    input_file.close()
    output_file.close()
