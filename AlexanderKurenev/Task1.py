def rep_quotes(s):
    """Function receives a string and replaces all " symbols with ' and vise versa"""
    table = str.maketrans('\"\'', '\'\"')
    s = s.translate(table)
    return s


if __name__ == '__main__':
    print(rep_quotes(input()))
