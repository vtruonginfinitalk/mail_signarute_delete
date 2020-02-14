from cerberus import Validator

import re
from datetime import datetime, date
from pprint import pprint

# バリデーション定義
schema = {
    'name': {
        'type': 'string',
        'required': True,
        'empty': False,
    },
    'email': {
        'type': 'string',
        'required': True,
        'regex': '^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$',
    },
    'age': {
        'type': 'integer',
        'min': 0,
    },
    'phones': {
        'type': 'list',
        'schema': {
            'type': 'string',
            'regex': '^[0-9]{2,4}-[0-9]{2,4}-[0-9]{3,4}$',
        }
    },
    'address': {
        'type': 'string',
        'empty': True,
    },
    'birthday': {
        'type': 'date',
    }
}

# バリデータを作成
v = Validator(schema)

# 入力値1(バリデーションOK)
data_ok = {
    'name': '田中一郎',
    'email': 'tanaka@test.co.jp',
    'age': 30,
    'phones': [
        '012-3456-7890',
        '0120-444-444',
    ],
    'address': '',
    'birthday': date(1990, 7, 7),
}

# 入力値2(バリデーションNG)
data_ng = {
    'name': '',
#    'email': 'tanaka@test.co.jp',
    'age': -300,
    'phones': [
        '01234567890',
        'skype',
    ],
    'address': None,
    'birthday': '1990-07-07',
    'sex': 'male',
}

# バリデーション実施、結果表示
print("-----------------------------------------")
print("OK")
print("-----------------------------------------")
pprint(v.validate(data_ok))
pprint(v.errors)

print("-----------------------------------------")
print("NG")
print("-----------------------------------------")
pprint(v.validate(data_ng))
pprint(v.errors)