def flatten(prefix, obj):
    nobj = {}

    def merge(sub_obj):
        for k_sub, v_sub in sub_obj.items():
            i = 2
            while k_sub in obj:
                k_sub = k_sub + str(i)
                i += 1
            nobj[prefix + k_sub] = v_sub

    for k, v in obj.items():
        if type(v) == dict:
            sub_obj = flatten(k + "_", v)
            merge(sub_obj)
        elif type(v) == list:
            for i, el in enumerate(v):
                sub_obj = flatten(k + str(i) + "_", el)
                merge(sub_obj)
        else:
            nobj[prefix + k] = v

    return nobj


if __name__ == "__main__":
    obj = {
        "name": "bobby",
        "lastName": "tables",
        "age": 20,
        "siblings": [
            {
                "name": "alice",
                "lastName": "tables",
                "age": 25
            },
            {
                "name": "cindy",
                "lastName": "tables",
                "age": 40
            },
        ],
        "occupation": {
            "title": "database admin",
            "experience": 5,
            "compensation": {
                "type": "salary",
                "amount": 3e5
            }
        }
    }

    print(flatten("", obj))