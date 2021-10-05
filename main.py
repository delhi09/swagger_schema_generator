import json
import oyaml as yaml


def main(input):
    output = {}
    if type(input) is list:
        output["type"] = "array"
        if input and type(input[0]) is dict:
            output["items"] = {}
            output["items"]["type"] = "object"
            output["items"]["properties"] = main(input[0])
        elif input and type(input[0]) is str:
            output["items"] = {}
            output["items"]["type"] = "string"
            output["items"]["description"] = "todo"
            output["items"]["example"] = input
        elif input and type(input[0]) is int:
            output["items"] = {}
            output["items"]["type"] = "integer"
            output["items"]["description"] = "todo"
            output["items"]["example"] = input
        elif input and type(input[0]) is float:
            output["items"] = {}
            output["items"]["type"] = "integer"
            output["items"]["format"] = "float"
            output["items"]["description"] = "todo"
            output["items"]["example"] = input
        elif input and type(input[0]) is bool:
            output["items"] = {}
            output["items"]["type"] = "boolean"
            output["items"]["description"] = "todo"
            output["items"]["example"] = input

    elif type(input) is dict:
        for k, v in input.items():
            output[k] = {}
            if type(v) is str:
                output[k]["type"] = "string"
                output[k]["description"] = "todo"
                output[k]["example"] = v
            elif type(v) is int:
                output[k]["type"] = "integer"
                output[k]["description"] = "todo"
                output[k]["example"] = v
            elif type(v) is float:
                output[k]["type"] = "integer"
                output[k]["format"] = "float"
                output[k]["description"] = "todo"
                output[k]["example"] = v
            elif type(v) is bool:
                output[k]["type"] = "boolean"
                output[k]["description"] = "todo"
                output[k]["example"] = v
            elif type(v) is dict:
                output[k]["type"] = "object"
                output[k]["properties"] = main(v)
            elif type(v) is list:
                output[k] = main(v)

    return output


if __name__ == "__main__":
    with open("sample.json", mode="r", encoding="utf-8") as f:
        input = json.load(f)
    output = main(input)
    print(output)
    result = {
        "paths": {
            "/todo/": {
                "get or post or delete": {
                    "summary": "todo",
                    "description": "todo",
                    "tags": ["todo"],
                    "parameters": "todo",
                    "responses": {
                        "200": {
                            "description": "リクエスト成功",
                            "content": {"application/json": {"schema": output}},
                        }
                    },
                }
            }
        }
    }
    with open("swagger.yml", mode="w", encoding="utf-8") as f:
        yaml.dump(result, f, allow_unicode=True)
