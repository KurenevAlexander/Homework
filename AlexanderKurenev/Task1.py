if __name__ == '__main__':
    with open('data/unsorted_names.txt', 'r') as f:
        s = f.readlines()
    s.sort()
    with open('data/sorted_names.txt', 'w') as f:
        f.writelines(s)

