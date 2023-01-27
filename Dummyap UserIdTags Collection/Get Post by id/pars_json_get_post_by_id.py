import json

json_pars = []

with open(r"D:\Для Git\Postman_collections\dummyap\Post Data\Get Post by id\get_list.json", "r", encoding="utf-8") as f:
    jp = json.load(f)
    for i in jp["data"]:
        id_j = dict({"id": i["id"]})
        if id_j not in json_pars:
            json_pars.append(id_j)

with open("get_post_by_id.json", "w") as file:
    json.dump(json_pars, file, indent=2)


