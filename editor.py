import json

json_str = '''
{
    "glossary": {
        "title": "example glossary",
		"GlossDiv": {
            "title": "S",
			"GlossList": {
                "GlossEntry": {
                    "ID": "SGML",
					"SortAs": "SGML",
					"GlossTerm": "Standard Generalized Markup Language",
					"Acronym": "SGML",
					"Abbrev": "ISO 8879:1986",
					"GlossDef": {
                        "para": "A meta-markup language, used to create markup languages such as DocBook.",
						"GlossSeeAlso": ["GML", "XML"]
                    },
					"GlossSee": "markup"
                }
            }
        }
    }
}
'''

json_dict = json.loads(json_str)

json_dict["glossary"]["title"] = "Paulo Teste"
json_dict["glossary"]["GlossDiv"]["new_item"] = "value for new item"

new_json_str = json.dumps(json_dict, indent=4)

print(new_json_str)
