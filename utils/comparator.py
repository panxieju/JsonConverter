def compare(data1, data2,level=0):
    assert isinstance(data1, dict)
    assert isinstance(data2, dict)
    keys1 = list(data1.keys())
    keys2 = list(data2.keys())
    keys1.sort()
    keys2.sort()
    err = ''
    if len(keys1) != len(keys2):
        err += '错误: KEY长度不一致\n'
    for key in keys1:
        if key not in keys2:
            err += '错误: {}不包含{}键\n'.format(data2, key)
    for key in keys1:
        if key not in keys1:
            err += '错误: {}不包含{}键\n'.format(data1, key)
    if err:
        return False, err

    for key in keys1:
        type1 = type(data1[key])
        type2 = type(data2[key])
        if type1 != type2:
            err += '错误: {}对应的值数据类型不一致\n'.format(key)
    if err:
        return False, err

    for key in keys1:
        value1 = data1[key]
        value2 = data2[key]
        if isinstance(value1, dict):
            isSame, err = compare(value1, value2, level+1)
        if isinstance(value1, list):
            isSame, err = compareList(value1, value2, key, level+1)
    if err:
        return False, err
    else:
        return True, ''



def compareList(data1, data2, key='',level=0):
    assert isinstance(data1, list)
    assert isinstance(data2, list)

    if data1 and not data2:
        return False, "错误: {} 对应的空值无法判断类型和进行比较\n".format(key)
    if data2 and not data1:
        return False, "错误: {} 对应的空值无法判断类型和进行比较\n".format(key)
    if not data1 and not data2:
        return True, ''

    types = set()
    for item in data1:
        types.add(type(item))
    for item in data2:
        types.add(type(item))
    if len(types) != 1:
        return False, "错误: {}键对应列表数据类型不一致".format(key)
    item1 = data1[0]
    item2 = data2[0]
    if isinstance(item1, dict):
        return compare(item1, item2)
    if isinstance(item1, list):
        return compareList(item1, item2)
    return True, ''


if __name__ == '__main__':
    d1 ={
  "count": 1,
  "lastUse": {
    "age": 0,
    "beginTime": "2020-01-12",
    "cr": 0,
    "creator": "5c26f53a67f356005f513dea",
    "cycle": 0,
    "height": 172,
    "list": [
      {
        "dosage": "100",
        "formula": 1,
        "interval": "",
        "name": "顺铂",
        "remark1": "",
        "remark2": "配合放疗",
        "route": "静脉滴注",
        "time": "第1,22,43天",
        "trueDosage": "178.0",
        "unit": "mg/㎡",
        "unit2": "mg"
      }
    ],
    "literature": [],
    "name": "顺铂",
    "nextTime": "2020-02-01",
    "objectId": "5e1ae294dd3c13006ac7e6a6",
    "overallResponse": {
      "result": "NC",
      "system": "WHO"
    },
    "patient": "5e1ae28d43c257006ff040f8",
    "prescriptionId": "5e0782977796d9006a741355",
    "sent": 0,
    "sideEffectLevel": [
      {
        "detail": "中度；需要内科治疗",
        "level": "2级",
        "name": "内分泌疾病-甲状旁腺功能亢进",
        "system": "CACTE"
      }
    ],
    "status": 0,
    "weight": 66
  },
  "pUses": [
    {
      "alphabet": "A",
      "beginTime": "2020-01-12",
      "index": 1,
      "name": "顺铂",
      "nextTime": "2020-02-01",
      "pid": "5e1ae294dd3c13006ac7e6a6",
      "prescriptionId": "5e0782977796d9006a741355",
      "result": {
        "result": "NC",
        "system": "WHO"
      },
      "showTitle": 1,
      "sideEffectLevel": [
        {
          "detail": "中度；需要内科治疗",
          "level": "2级",
          "name": "内分泌疾病-甲状旁腺功能亢进",
          "system": "CACTE"
        }
      ],
      "subIndex": 1
    }
  ],
  "success": 1
}
    d2 = {
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
    isSame, err = compare(d1,d2)
    print(err)
