from functools import reduce

from utils.common import hump
from utils.formater import getStandardListItem



classNames = []

def generateGoStruct(data, key='DEMO', inden=0):
    assert isinstance(data, dict)
    classInden = inden
    methodInden = inden + 1
    result = ''
    if inden == 0:
        result += '''
//package info here

/**
Created By JsonAll
Copyright@Nexttec Inc, 2020.

{}
*/
type JsonData struct$1
'''.format(data).replace('$1','{')
    else:
        result += '\n\n' + '/**\n'
        result += '{}\n'.format(data)
        result += '*/\n'
        result += 'type {0} struct$1\n'.format(hump(key)).replace('$1','{')
    innerClass = {}
    setterAndGetters = []
    index = 0
    lastIndex = len(data.keys()) - 1
    keys = list(data.keys())
    keys.sort()
    for key in keys:
        value = data[key]
        result += '\t'
        if isinstance(value, str):
            result += '{} string `json:"{}"`'.format(hump(key), key)
        elif isinstance(value, float):
            result +='{} float64 `json:"{}"`'.format(hump(key), key)
        elif isinstance(value, bool):
            result += '{} bool `json:"{}"`'.format(hump(key), key)
        elif isinstance(value, int):
            result += '{} int64 `json:"{}"`'.format(hump(key), key)
        elif isinstance(value, bytes):
            result += '{} []byte `json:"{}"`'.format(hump(key), key)
        elif isinstance(value, dict):
            innerClass[key] = value
            result += '{} {} `json:"{}"`'.format(hump(key), hump(key),key)
        elif isinstance(value, list):
            types = set()
            for item in value:
                types.add(type(item))
            if len(types) > 1:
                print(types)
                return key + "对应的数据类型不一致", 1
            if value:
                valueItem = value[0]
                if isinstance(valueItem, str):
                    result += '{} []string `json:"{}"`'.format(hump(key), key)
                elif isinstance(valueItem, float):
                    result += '{} []float64 `json:"{}"`'.format(hump(key), key)
                elif isinstance(valueItem, bool):
                    result += '{} []bool `json:"{}"`'.format(hump(key), key)
                elif isinstance(valueItem, int):
                    result += '{} []int64 `json:"{}"`'.format(hump(key), key)
                elif isinstance(valueItem, bytes):
                    result += '{} [][]byte `json:"{}"`'.format(hump(key), key)
                elif isinstance(valueItem, dict):
                    result += '{0} []{0} `json:"{1}"`'.format(hump(key),key)
                    standardValue = getStandardListItem(value)
                    innerClass[key] = standardValue
            else:
                result += '{0} []interface$0$1 `json:"{1}"`'.format(hump(key),key).replace('$0','{').replace('$1','}')
        result += '\n'
    result += '}'

    if innerClass:
        for k, v in innerClass.items():
            if k in classNames:
                continue
            classNames.append(k)
            ret, err = generateGoStruct(v, k, inden + 1)
            if err == 0:
                result += ret

    return result, 0


if __name__ == '__main__':
    person ={
    "success": 1,
    "count": 1,
    "pUses": [
        {
            "name": "方案1：顺铂",
            "pid": "5e1ae294dd3c13006ac7e6a6",
            "beginTime": "2020-01-12",
            "sideEffectLevel": [
                {
                    "level": "2级",
                    "detail": "中度；需要内科治疗",
                    "system": "CACTE",
                    "name": "内分泌疾病-甲状旁腺功能亢进"
                }
            ],
            "result": {
                "system": "WHO",
                "result": "NC"
            },
            "alphabet": "A",
            "subIndex": 1,
            "index": 1,
            "prescriptionId": "5e0782977796d9006a741355",
            "showTitle": 1
        }
    ],
    "lastUse": {
        "name": "方案1：顺铂",
        "patient": "5e1ae28d43c257006ff040f8",
        "sideEffectLevel": [
            {
                "level": "2级",
                "detail": "中度；需要内科治疗",
                "system": "CACTE",
                "name": "内分泌疾病-甲状旁腺功能亢进"
            }
        ],
        "cycle": 0,
        "creator": "5c26f53a67f356005f513dea",
        "age": 0,
        "cr": 0,
        "sent": 0,
        "weight": 66,
        "list": [
            {
                "remark2": "配合放疗",
                "unit2": "mg",
                "dosage": "100",
                "unit": "mg/㎡",
                "name": "顺铂",
                "time": "第1,22,43天",
                "route": "静脉滴注",
                "trueDosage": "178.0",
                "remark1": "",
                "formula": 1,
                "interval": ""
            }
        ],
        "status": 0,
        "overallResponse": {
            "system": "WHO",
            "result": "NC"
        },
        "literature": [],
        "prescriptionId": "5e0782977796d9006a741355",
        "nextTime": "2020-02-01",
        "beginTime": "2020-01-12",
        "height": 172,
        "objectId": "5e1ae294dd3c13006ac7e6a6"
    }
}
    ret, err = generateGoStruct(person)
    print(ret)
