def combine_dicts(*args):
    """Receives changeable number of dictionaries (keys - letters, values - numbers)
    and combines them into one dictionary. Dict values summary in case of identical keys"""
    out = {}
    for d in args:
        for k, v in d.items():
            if k in out:
                out[k] += v
            else:
                out[k] = v
    return out


if __name__ == '__main__':
    dict_1 = {'a': 100, 'b': 200}
    dict_2 = {'a': 200, 'c': 300}
    dict_3 = {'a': 300, 'd': 100}
    print(combine_dicts(dict_1, dict_2))
    print(combine_dicts(dict_1, dict_2, dict_3))
