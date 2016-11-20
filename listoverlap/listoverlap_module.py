import random

def listoverlap(list1, list2):
    common_list = []
    for i in list1:
        if i in list2:
            if i not in common_list:
                common_list.append(i)
    return common_list


def main():
    return


if __name__ == '__main__':
    list1 = []
    for i in range(10):
        list1.append(random.randint(1, 20))
    list2 = []
    for i in range(10):
        list2.append(random.randint(1, 20))
    main()
    print(listoverlap(list1, list2))
