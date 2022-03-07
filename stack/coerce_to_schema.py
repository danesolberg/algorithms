def normalize_beverages(raw):
    new = {}

    for row in raw:
        store_id = row["storeId"]
        if store_id not in new:
            new[store_id] = {
                "storeId": store_id,
                "beverages": []
            }
        beverage_obj = {}
        for k, v in row.items():
            if k == 'storeId':
                continue
            beverage_obj[k] = v
        new[store_id]["beverages"].append(beverage_obj)

    return list(new.values())


if __name__ == "__main__":
    raw = [
        {"beverageId": 1, "storeId": 1, "price": 1.00},
        {"beverageId": 1, "storeId": 2, "price": 1.00},
        {"beverageId": 2, "storeId": 2, "price": 2.00},
    ]

    out1 = [
        {"storeId": 1, "beverages": [{"beverageId": 1, "price": 1.00}]},
        {
            "storeId": 2,
            "beverages": [
                {"beverageId": 1, "price": 1.00},
                {"beverageId": 2, "price": 2.00},
            ],
        },
    ]

    assert normalize_beverages(raw) == out1
