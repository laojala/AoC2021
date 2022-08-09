def read_data(file="day24.data"):
    with open(file) as f:
        input_data = [d.rstrip() for d in f.readlines()]
        print(input_data[0])

        temp = []


        for line in input_data:
            # instruction "add z y" is always before new inp so we stop there
            if line == "add z y":
                continue


            temp.append(line)

read_data()