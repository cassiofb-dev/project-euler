def getSeries():
    file = open("solutions/8/series.txt", "r")

    file_contents = file.read()

    return file_contents

def largestProductInSeries(adjacents):
    series = getSeries()

    largest_product = 1
    current_product = 1
    for i in range(len(series) - adjacents):
        for j in range(adjacents):
            number = int(series[i + j])
            current_product *= number

        if (current_product > largest_product):
            largest_product = current_product

        current_product = 1

    return largest_product

def main():
    result = largestProductInSeries(13)

    print(result)

if __name__ == "__main__":
    main()
