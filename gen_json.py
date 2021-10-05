import json

result = [
    {
        "name": "delhi09",
        "age": 100,
        "height": 175.5,
        "prefecture": {"name": "tokyo", "code": 13},
        "telephone number": ["111-1111-1111", "222-2222-2222"],
        "mail_address": [
            {"private": "hoge@example.com"},
            {"business": "fuga@example.com"},
        ],
        "is_adult": True,
    }
]

with open("sample.json", "w") as f:
    json.dump(result, f)
