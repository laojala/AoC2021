# inspired by https://github.com/timrprobocom/advent-of-code/blob/master/2021/day18.py

# read input
# perform addition
# split + explode loop (unsure about order)
# when all additions are done, magnitude
# https://github.com/timrprobocom/advent-of-code/blob/master/2021/day18.py

def add(n1, n2):
    result = ['['] + n1 + [','] + n2 + [']']
    #print(result)
    #print(out(result))
    return result


# TODO next: loop that explodes repeatedly
def explode(item):
    print(item)
    nested = 0
    index = 0
    # item explodes if it has 5 opening tags on its left without closing tags
    for i, char in enumerate(item):
        index = i
        if nested == 5:
            break
        elif char == "[":
            nested += 1
        elif char == "]":
            nested -= 1
    if nested < 5:
        print("don't explode")
        #return None
    # else, we start to explode the item. We know index that needs to be exploded.
    print(f"explode at {index}, {item[index:index+5]}")
    left = item[index+1]
    right = item[index+3]
    print("left, right", left, right)

    # Search backwards for a digit.
    for nn in range(index-1, -1, -1):
        print(item[nn])
        if isdigit(item[nn]):
            print("l adding",left,"to",item[nn])
            item[nn] += left
            break

    # Search forwards for a digit.
    for nn in range(index+5, len(item)):
        if isdigit(item[nn]):
            print("r adding",right,"to",item[nn])
            item[nn] += right
            break
    # Remove the pair.
    return item[:index] + "0" + item[index+5:]



def isdigit(k):
    return isinstance(k, int)


def out(item):
    return ''.join(str(t) for t in item)


def item_to_list(item):
    return [int(s) if s.isdigit() else s for s in item.replace(" ", "")]


def read_file(filename="test/addition.data"):
    with open(filename, 'r') as f:
        all_lines = [d.rstrip() for d in f.readlines()]
        lines = []
        for line in all_lines:
            lines.append(item_to_list(line))
        return lines




#[[[[[9,8],1],2],3],4] becomes [[[[0,9],2],3],4]
thing = explode("[[[[[9,8],1],2],3],4]")
print(thing)