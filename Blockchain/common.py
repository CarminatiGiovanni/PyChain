def list_to_str(l: list):
    if len(l) == 0:
        return "[]"
    if type(l[0]) == list:
        for sub_list in l:
            list_to_str(sub_list)

    def call_str(o):
        return str(o)

    str_list_iter = map(call_str, l)
    list_str = list(str_list_iter)

    return str(list_str)


def list_to_dict(l: list) -> list[dict]:
    if len(l) == 0:
        return []
    if type(l[0]) == list:
        for sub_list in l:
            list_to_dict(sub_list)

    def call_as_dict(o):
        return o.ad_dict()

    dict_list_iter = map(call_as_dict, l)
    list_dict = list(dict_list_iter)

    return list_dict


'''
models A:
    def __init__(self,n):
        self.n = n

    def __str__(self):
        return str(self.n)

l = [A(1),A(2),A(3)]

print(type(list_to_str(l)))
'''