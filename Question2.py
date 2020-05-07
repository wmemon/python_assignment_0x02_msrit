def collatz_length(num):
    if not (isinstance(num, int)):
        return "This function accepts an integer only."
    length = 1
    answer = num
    while answer != 1:
        if answer % 2 == 0:
            answer = answer / 2
            length += 1
        elif answer % 2 == 1:
            answer = ((3 * answer) + 1)
            length += 1
    return length


def main():
    print("Please note that we consider 1 as a part of collatz length here.")
    num_list = []
    for number in range(1, 21):
        num_list.append(collatz_length(number))
    print(num_list)
    print(max(num_list))
    print(num_list.index(max(num_list)))


if __name__ == "__main__":
    main()
