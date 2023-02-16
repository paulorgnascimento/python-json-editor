import json

with open('sample.json', 'r') as file:
    json_str = file.read()

json_dict = json.loads(json_str)

json_dict["glossary"]["title"] = "Paulo Teste 2"
json_dict["glossary"]["GlossDiv"]["new_item"] = "value for new item 2"

new_json_str = json.dumps(json_dict, indent=4)

with open('sample.json', 'w') as file:
    file.write(new_json_str)
