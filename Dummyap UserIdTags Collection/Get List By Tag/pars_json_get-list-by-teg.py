import json

json_pars = []

with open(r" Прописать путь до файла get_list.json", "r", encoding="utf-8") as f:
    jp = json.load(f)
    for i in jp["data"]:
        for j in i["tags"]:
            tag_j = dict({"tags": j})
            if tag_j not in json_pars:
                json_pars.append(tag_j)

with open("get-list-by-tag.json", "w") as file:
    json.dump(json_pars, file, indent=2)


