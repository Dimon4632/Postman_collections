import json

json_pars = []

with open(r" Прописать путь до файла get_list.json ", "r", encoding="utf-8") as f:
    jp = json.load(f)
    for i in jp["data"]:
        json_pars.append(dict({"id": i["owner"]["id"]}))

with open("get-list-by-user.json", "w") as file:
    json.dump(json_pars, file, indent=2)
