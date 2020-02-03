from functools import reduce

from utils.common import hump
from utils.formater import getStandardListItem


def generateSetterAndGetter(key, type, inden=0):
    assert isinstance(key, str)
    setFunctionName = 'set%s' % hump(key)
    getFunctionName = 'get%s' % hump(key)
    if type == 'boolean':
        if key[:2] != 'is':
            setFunctionName = 'set%s' % hump(key)
            getFunctionName = 'is%s' % hump(key)
        else:
            setFunctionName = 'set%s' % hump(key[2:])
            getFunctionName = key

    fun = '''
public void {0}({2} {1})$1
    this.{1} = {1};
$2

public {2} {3}()$1
    return this.{1};
$2
'''.format(setFunctionName, key, type, getFunctionName).replace('$1', '{').replace('$2', '}')
    ret = []
    for line in fun.split('\n'):
        ret.append('\t' * (inden) + line)
    return reduce(lambda x, y: '{}\n{}'.format(x, y), ret)

classNames = []

def generateKotlinClass(data, key='DEMO', inden=0):
    assert isinstance(data, dict)
    classInden = inden
    methodInden = inden + 1
    result = ''
    if inden == 0:
        result += '''
//package info here

import java.io.Serializable
import java.util.List

/**
Created By JsonAll
Copyright@Nexttec Inc, 2020.

{}
*/
data class JsonData(
'''.format(data)
    else:
        result += '\n\n' + '/**\n'
        result += '{}\n'.format(data)
        result += '*/\n'
        result += 'data class {0}(\n'.format(hump(key))
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
            result += 'val '+ key + ': String'
        elif isinstance(value, float):
            result += 'val '+key + ': Float,'
        elif isinstance(value, bool):
            result += 'val '+key + ': Boolean'
        elif isinstance(value, int):
            result += 'val '+key + ': Int'
        elif isinstance(value, bytes):
            result += 'val '+key +': ByteArray'
        elif isinstance(value, dict):
            innerClass[key] = value
            result += 'val '+key + ': '+ hump(key)
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
                    result += 'val {}: List<{}>'.format(key, 'String')
                elif isinstance(valueItem, float):
                    result += 'val {}: List<{}>'.format(key, 'Float')
                elif isinstance(valueItem, bool):
                    result += 'val {}: List<{}>'.format(key, 'Boolean')
                elif isinstance(valueItem, int):
                    result += 'val {}: List<{}>'.format(key, 'Int')
                elif isinstance(valueItem, bytes):
                    result += 'val {}: List<{}>'.format(key, 'ByteArray')
                elif isinstance(valueItem, dict):
                    result += 'val {}: List<{}>'.format(key, hump(key))
                    standardValue = getStandardListItem(value)
                    innerClass[key] = standardValue
            else:
                result += 'val {}:List<Any>'.format(key)
        if index != lastIndex:
            result += ','
        index += 1
        result += '\n'
    result += ') : Serializable'

    if innerClass:
        for k, v in innerClass.items():
            if k in classNames:
                continue
            classNames.append(k)
            ret, err = generateKotlinClass(v, k, inden + 1)
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
    ret, err = generateKotlinClass(person)
    print(ret)
    print(err)
