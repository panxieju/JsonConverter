import json
from functools import reduce


def sortJsonData(data):
    assert isinstance(data, dict)
    sorted(data.items(), key=lambda data: data[0])
    for k, v in data.items():
        if isinstance(v, dict):
            v = sortJsonData(v)
            data[k] = v
        elif isinstance(v, list):
            for item in v:
                if isinstance(item, dict):
                    v.remove(item)
                    item = sortJsonData(item)
                    v.append(item)
    return data

def jsonFormater(data, inden=0):
    result = ''
    if isinstance(data, str):
        data = json.loads(data, encoding='utf-8')
    keyInden = inden + 1
    dictInden = inden + 2
    if isinstance(data, dict):
        result += inden * '\t' + '{\n'
        primaryKeys = data.keys()
        primaryKeys = list(primaryKeys)
        primaryKeys.sort()
        lastIndex = len(primaryKeys) - 1
        index = 0
        for key in primaryKeys:
            result += '{}"{}":'.format(keyInden * '\t', key)
            value = data[key]
            if isinstance(value, dict):
                result += jsonFormater(value, keyInden)
            elif isinstance(value, list):
                result += jsonFormater(value, keyInden)
            elif isinstance(value, str):
                result += '"{}"'.format(value)
            else:
                result += '{}'.format(value)
            if index != lastIndex:
                result += ',\n'
            index += 1
        result += '\n' + '\t' * inden + '}'
    elif isinstance(data, list):
        result += ' ['
        if data:
            result += '\n'
            # result += '\t' * (inden)
            lastSubIndex = len(data) - 1
            subIndex = 0
            for item in data:
                if isinstance(item, str):
                    result += '{}"{}"'.format('\t' * keyInden, item)
                elif isinstance(item, dict):
                    result += jsonFormater(item, inden + 1)
                elif isinstance(item, list):
                    result += jsonFormater(item, inden + 1)
                else:
                    result += '{}{}'.format('\t' * keyInden, item)
                if subIndex != lastSubIndex:
                    result += ',\n'
                else:
                    result += '\n'
                subIndex += 1
            result += inden * '\t' + ']'
        else:
            result += ']'
    else:
        raise ValueError("错误的数据")
    return result


def jsonHtmlFormater(data, inden=0):
    result = ''
    if isinstance(data, str):
        data = json.loads(data, encoding='utf-8')
    keyInden = inden + 1
    dictInden = inden + 2
    if isinstance(data, dict):
        result += inden * '\t' + '{\n'
        primaryKeys = data.keys()
        primaryKeys = list(primaryKeys)
        primaryKeys.sort()
        lastIndex = len(primaryKeys) - 1
        index = 0
        for key in primaryKeys:
            result += '{}"{}":'.format(keyInden * '\t', key)
            value = data[key]
            if isinstance(value, dict):
                result += jsonFormater(value, keyInden)
            elif isinstance(value, list):
                result += jsonFormater(value, keyInden)
            elif isinstance(value, str):
                result += '"{}"'.format(value)
            else:
                result += '{}'.format(value)
            if index != lastIndex:
                result += ',\n'
            index += 1
        result += '\n' + '\t' * inden + '}'
    elif isinstance(data, list):
        result += ' ['
        if data:
            result += '\n'
            # result += '\t' * (inden)
            lastSubIndex = len(data) - 1
            subIndex = 0
            for item in data:
                if isinstance(item, str):
                    result += '{}"{}"'.format('\t' * keyInden, item)
                elif isinstance(item, dict):
                    result += jsonFormater(item, inden + 1)
                elif isinstance(item, list):
                    result += jsonFormater(item, inden + 1)
                else:
                    result += '{}{}'.format('\t' * keyInden, item)
                if subIndex != lastSubIndex:
                    result += ',\n'
                else:
                    result += '\n'
                subIndex += 1
            result += inden * '\t' + ']'
        else:
            result += ']'
    else:
        raise ValueError("错误的数据")
    return result

def getStandardListItem(listData):
    assert isinstance(listData, list)
    result = {}
    for item in listData:
        if isinstance(item, dict):
            for k,v in item.items():
                result[k] = v
    return result


if __name__ == '__main__':
    data = '''  {
    "count": 21,    "list": [      {
            "BriefTitle": "刘全医师：该研究尚未获得伦理委员会批准。请于批准后再开始纳入参试者，并与我们联系上传批件。 功能性内镜颅底手术联合术前诱导性介入化疗和同期放疗治疗晚期鼻腔鼻窦腺样囊性癌：前瞻性随机对照研究",
            "DrugName": "",
            "Identifier": "ChiCTR1900026122",
            "StudyPhase": "其它",
            "add_time": "2019-12-12-11:40:51"
        },   {
            "BriefTitle": "Fluorescence-guided Surgery Using cRGD-ZW800-1 in Oral Cancer",
            "DrugName": "",
            "Identifier": "NCT04191460",
            "StudyPhase": "Phase 2",
            "add_time": "2019-12-16-10:50:56"
        },   {
            "BriefTitle": "Study of INBRX-106 in Subjects With Locally Advanced or Metastatic Solid Tumors (Hexavalent OX40 Agonist)",
            "DrugName": "",
            "Identifier": "NCT04198766",
            "StudyPhase": "Phase 1",
            "add_time": "2019-12-16-11:39:12"
        },
        {
            "BriefTitle": "陈传本医师：该研究尚未获得伦理委员会批准。请于批准后再开始纳入参试者，并与我们联系上传批件。信迪利单抗联合顺铂新辅助治疗可完全切除的II-IVA期头颈鳞癌的开放式I/II期临床研究",
            "DrugName": "顺铂",
            "Identifier": "ChiCTR1900028010",
            "StudyPhase": "探索性研究/预试验",
            "add_time": "2019-12-17-09:03:50"
        },
        {
            "BriefTitle": "A Study of Anlotinib and AK105 Injection in Subjects With Advanced Head, Neck and Chest Cancer",
            "DrugName": "",
            "Identifier": "NCT04203719",
            "StudyPhase": "Phase 2",
            "add_time": "2019-12-20-15:11:00"
        },
        {
            "BriefTitle": "低剂量（50mCi）和常规剂量（100mCi）碘-131清除分化型甲状腺癌伴桥本甲状腺炎术后残留组织的随机对照临床研究",
            "DrugName": "",
            "Identifier": "ChiCTR1900027445",
            "StudyPhase": "上市后药物",
            "add_time": "2019-12-29-10:10:11"
        },
        {
            "BriefTitle": "A Study of Selpercatinib (LY3527723) in Participants With RET-Mutant Medullary Thyroid Cancer",
            "DrugName": "",
            "Identifier": "NCT04211337",
            "StudyPhase": "Phase 3",
            "add_time": "2020-01-03-11:03:15"
        },
        {
            "BriefTitle": "Natural History of Medullary Thyroid Cancer to Inform Advanced Disease Management",
            "DrugName": "",
            "Identifier": "NCT04216732",
            "StudyPhase": "",
            "add_time": "2020-01-09-10:48:48"
        },
        {
            "BriefTitle": "Radiotherapy vs. Trans-Oral Surgery for HPV-Negative Oropharyngeal Squamous Cell Carcinoma",
            "DrugName": "",
            "Identifier": "NCT04220749",
            "StudyPhase": "Phase 2",
            "add_time": "2020-01-09-10:57:00"
        },
        {
            "BriefTitle": "Radiation Therapy for the Treatment of Metastatic Gastrointestinal Cancers",
            "DrugName": "",
            "Identifier": "NCT04221893",
            "StudyPhase": "N/A",
            "add_time": "2020-01-11-09:11:25"
        },
        {
            "BriefTitle": "氟唑帕利胶囊联合化疗治疗晚期胰腺癌的Ib/II期临床研究",
            "DrugName": "氟唑帕利胶囊",
            "Identifier": "CTR20192634",
            "StudyPhase": "I期",
            "add_time": "2020-01-14-07:33:57"
        },
        {
            "BriefTitle": "C7R-GD2.CART Cells for Patients With Relapsed or Refractory Neuroblastoma and Other GD2 Positive Cancers (GAIL-N)",
            "DrugName": "Cyclophosphamide;Fludarabine",
            "Identifier": "NCT03635632",
            "StudyPhase": "Phase 1",
            "add_time": "2020-01-15-08:16:57"
        },
        {
            "BriefTitle": "Resiliency Among Older Adults Receiving Lung Cancer Treatment",
            "DrugName": "",
            "Identifier": "NCT04229381",
            "StudyPhase": "N/A",
            "add_time": "2020-01-17-12:54:55"
        },
        {
            "BriefTitle": "Clinical Sensitivity Verification Study of Circulating Tumor Cells Gene Mutation Detection From Advanced NSCLC Patients",
            "DrugName": "",
            "Identifier": "NCT04229121",
            "StudyPhase": "",
            "add_time": "2020-01-18-09:53:59"
        },
        {
            "BriefTitle": "经Ommaya囊侧脑室内注射培美曲塞二钠治疗非小细胞肺癌软脑膜转移的前瞻性临床研究",
            "DrugName": "培美曲塞",
            "Identifier": "ChiCTR2000028936",
            "StudyPhase": "探索性研究/预试验",
            "add_time": "2020-01-19-07:14:42"
        },
        {
            "BriefTitle": "LOXO-292治疗晚期或转移性RET融合阳性非小细胞肺癌3期研究",
            "DrugName": [
                "LOXO-292"
            ],
            "Identifier": "CTR20192731",
            "StudyPhase": "III期",
            "add_time": "2020-01-20-11:15:27"
        },
        {
            "BriefTitle": "迈华替尼治疗EGFR罕见突变（G719X，L861Q，S768I）的 晚期非小细胞肺癌II期开放、单臂、多中心临床试验",
            "DrugName": "",
            "Identifier": "ChiCTR2000029058",
            "StudyPhase": "II期临床试验",
            "add_time": "2020-01-22-00:43:26"
        },
        {
            "BriefTitle": "[14C] CT-707人体吸收代、谢和排泄研究",
            "DrugName": "CT-707颗粒",
            "Identifier": "CTR20192537",
            "StudyPhase": "I期",
            "add_time": "2020-01-22-03:20:47"
        },
        {
            "BriefTitle": "SCT-I10A 或安慰剂联合多西他赛二线治疗晚期肺鳞癌的III期临床研究",
            "DrugName": "重组人源化抗PD-1单克隆抗体注射液",
            "Identifier": "CTR20192593",
            "StudyPhase": "III期",
            "add_time": "2020-01-24-18:40:29"
        },
        {
            "BriefTitle": "A Phase I/II Clinical Study of Foritinib Succinate in Non-small Cell Lung Cancer (NSCLC) Patients",
            "DrugName": "",
            "Identifier": "NCT04237805",
            "StudyPhase": "Phase 1/Phase 2",
            "add_time": "2020-01-25-23:47:04"
        },
        {
            "BriefTitle": "Clinical Trial Assessing the Effecacy of Abscopal Effect Induced by SBRT and Immunotherapy in Advanced NSCLC",
            "DrugName": "",
            "Identifier": "NCT04238169",
            "StudyPhase": "Phase 2",
            "add_time": "2020-01-28-01:16:29"
        }
    ],
    "success": 1
}
    '''
    # data = '{"name":"centros","age":40,  "familyName":"pan","location":{"city":"guangzhou","province":"guangdong"},"list":["1","2"]}'
    data = '''
{
  "changeTag": 0,
  "prescriptionList": [
    {
      "stage": "ⅠB",
      "stageList": [
        {
          "tag1": "化疗",
          "tag1List": [
            {
              "click": 0,
              "list": [],
              "tag2": "一线治疗",
              "tag2List": [
                {
                  "click": 1,
                  "list": [
                    {
                      "cancer": "霍奇金淋巴瘤",
                      "ctList": [],
                      "favorite": 0,
                      "id": "5e1fdb7b7d5774006af72058",
                      "literature": [
                        "http://www.ncbi.nlm.nih.gov/m/pubmed/21873543",
                        "http://www.ncbi.nlm.nih.gov/m/pubmed/19933898 "
                      ],
                      "name": "方案1：ABVD+利妥昔单抗",
                      "nameNum": "方案1",
                      "nameTitle": "ABVD+利妥昔单抗",
                      "overallResponse": "",
                      "prescriptionVersion": "2018.V3",
                      "price": 0,
                      "remark": "",
                      "stage": "ⅠB",
                      "tag": "ⅠB化疗：一线治疗，＋ISRT",
                      "tag1": "化疗",
                      "tag2": "一线治疗",
                      "tag3": "＋ISRT",
                      "tagRemark": ""
                    },
                    {
                      "cancer": "霍奇金淋巴瘤",
                      "ctList": [],
                      "favorite": 0,
                      "id": "5e1fdb7dfc36ed006a3cf23f",
                      "literature": [
                        "https://ash.confex.com/ash/2010/webprogram/Paper30295.html"
                      ],
                      "name": "方案2：CHOP+利妥昔单抗",
                      "nameNum": "方案2",
                      "nameTitle": "CHOP+利妥昔单抗",
                      "overallResponse": "",
                      "prescriptionVersion": "2018.V3",
                      "price": 0,
                      "remark": "",
                      "stage": "ⅠB",
                      "tag": "ⅠB化疗：一线治疗，＋ISRT",
                      "tag1": "化疗",
                      "tag2": "一线治疗",
                      "tag3": "＋ISRT",
                      "tagRemark": ""
                    },
                    {
                      "cancer": "霍奇金淋巴瘤",
                      "ctList": [],
                      "favorite": 0,
                      "id": "5e1fdb805620710077ebb320",
                      "literature": [
                        "http://www.ncbi.nlm.nih.gov/m/pubmed/22093944"
                      ],
                      "name": "方案3：CVP+利妥昔单抗",
                      "nameNum": "方案3",
                      "nameTitle": "CVP+利妥昔单抗",
                      "overallResponse": "",
                      "prescriptionVersion": "2018.V3",
                      "price": 0,
                      "remark": "",
                      "stage": "ⅠB",
                      "tag": "ⅠB化疗：一线治疗，＋ISRT",
                      "tag1": "化疗",
                      "tag2": "一线治疗",
                      "tag3": "＋ISRT",
                      "tagRemark": ""
                    }
                  ],
                  "tag": "ⅠB化疗：一线治疗，＋ISRT",
                  "tag3": "＋ISRT",
                  "tagRemark": ""
                }
              ]
            },
            {
              "click": 0,
              "list": [],
              "tag2": "二线治疗",
              "tag2List": [
                {
                  "click": 1,
                  "list": [
                    {
                      "cancer": "霍奇金淋巴瘤",
                      "ctList": [],
                      "favorite": 0,
                      "id": "5e1fdb827796d9006a403ca6",
                      "literature": [
                        "http://www.ncbi.nlm.nih.gov/m/pubmed/12377653",
                        "http://www.ncbi.nlm.nih.gov/m/pubmed/18443961"
                      ],
                      "name": "方案1：DHAP",
                      "nameNum": "方案1",
                      "nameTitle": "DHAP",
                      "overallResponse": "",
                      "prescriptionVersion": "2018.V3",
                      "price": 0,
                      "remark": "",
                      "stage": "ⅠB",
                      "tag": "ⅠB化疗：二线治疗，复发/难治患者",
                      "tag1": "化疗",
                      "tag2": "二线治疗",
                      "tag3": "复发/难治患者",
                      "tagRemark": ""
                    },
                    {
                      "cancer": "霍奇金淋巴瘤",
                      "ctList": [],
                      "favorite": 0,
                      "id": "5e1fdb847796d9006a403cb4",
                      "literature": [
                        "http://www.ncbi.nlm.nih.gov/m/pubmed/10416011",
                        "http://www.ncbi.nlm.nih.gov/m/pubmed/24863692",
                        "http://www.ncbi.nlm.nih.gov/m/pubmed/19889622"
                      ],
                      "name": "方案2：ESHAP",
                      "nameNum": "方案2",
                      "nameTitle": "ESHAP",
                      "overallResponse": "",
                      "prescriptionVersion": "2018.V3",
                      "price": 0,
                      "remark": "",
                      "stage": "ⅠB",
                      "tag": "ⅠB化疗：二线治疗，复发/难治患者",
                      "tag1": "化疗",
                      "tag2": "二线治疗",
                      "tag3": "复发/难治患者",
                      "tagRemark": ""
                    },
                    {
                      "cancer": "霍奇金淋巴瘤",
                      "ctList": [],
                      "favorite": 0,
                      "id": "5e1fdb867796d9006a403cc5",
                      "literature": [
                        "http://www.ncbi.nlm.nih.gov/m/pubmed/11157476",
                        "http://www.ncbi.nlm.nih.gov/m/pubmed/18443961"
                      ],
                      "name": "方案3：ICE",
                      "nameNum": "方案3",
                      "nameTitle": "ICE",
                      "overallResponse": "",
                      "prescriptionVersion": "2018.V3",
                      "price": 0,
                      "remark": "",
                      "stage": "ⅠB",
                      "tag": "ⅠB化疗：二线治疗，复发/难治患者",
                      "tag1": "化疗",
                      "tag2": "二线治疗",
                      "tag3": "复发/难治患者",
                      "tagRemark": ""
                    },
                    {
                      "cancer": "霍奇金淋巴瘤",
                      "ctList": [],
                      "favorite": 0,
                      "id": "5e1fdb8843c257006f17a39e",
                      "literature": [
                        "http://www.ncbi.nlm.nih.gov/m/pubmed/17229633"
                      ],
                      "name": "方案4：IGEV",
                      "nameNum": "方案4",
                      "nameTitle": "IGEV",
                      "overallResponse": "",
                      "prescriptionVersion": "2018.V3",
                      "price": 0,
                      "remark": "",
                      "stage": "ⅠB",
                      "tag": "ⅠB化疗：二线治疗，复发/难治患者",
                      "tag1": "化疗",
                      "tag2": "二线治疗",
                      "tag3": "复发/难治患者",
                      "tagRemark": ""
                    }
                  ],
                  "tag": "ⅠB化疗：二线治疗，复发/难治患者",
                  "tag3": "复发/难治患者",
                  "tagRemark": ""
                }
              ]
            }
          ]
        }
      ]
    },
    {
      "stage": "ⅡB",
      "stageList": [
        {
          "tag1": "化疗",
          "tag1List": [
            {
              "click": 0,
              "list": [],
              "tag2": "一线治疗",
              "tag2List": [
                {
                  "click": 1,
                  "list": [
                    {
                      "cancer": "霍奇金淋巴瘤",
                      "ctList": [],
                      "favorite": 0,
                      "id": "5e1fdb8bfc36ed006a3cf2df",
                      "literature": [
                        "http://www.ncbi.nlm.nih.gov/m/pubmed/21873543",
                        "http://www.ncbi.nlm.nih.gov/m/pubmed/19933898 "
                      ],
                      "name": "方案1：ABVD+利妥昔单抗",
                      "nameNum": "方案1",
                      "nameTitle": "ABVD+利妥昔单抗",
                      "overallResponse": "",
                      "prescriptionVersion": "2018.V3",
                      "price": 0,
                      "remark": "",
                      "stage": "ⅡB",
                      "tag": "ⅡB化疗：一线治疗，＋ISRT",
                      "tag1": "化疗",
                      "tag2": "一线治疗",
                      "tag3": "＋ISRT",
                      "tagRemark": ""
                    },
                    {
                      "cancer": "霍奇金淋巴瘤",
                      "ctList": [],
                      "favorite": 0,
                      "id": "5e1fdb8d5620710077ebb39b",
                      "literature": [
                        "https://ash.confex.com/ash/2010/webprogram/Paper30295.html"
                      ],
                      "name": "方案2：CHOP+利妥昔单抗",
                      "nameNum": "方案2",
                      "nameTitle": "CHOP+利妥昔单抗",
                      "overallResponse": "",
                      "prescriptionVersion": "2018.V3",
                      "price": 0,
                      "remark": "",
                      "stage": "ⅡB",
                      "tag": "ⅡB化疗：一线治疗，＋ISRT",
                      "tag1": "化疗",
                      "tag2": "一线治疗",
                      "tag3": "＋ISRT",
                      "tagRemark": ""
                    },
                    {
                      "cancer": "霍奇金淋巴瘤",
                      "ctList": [],
                      "favorite": 0,
                      "id": "5e1fdb8f7d5774006af72157",
                      "literature": [
                        "http://www.ncbi.nlm.nih.gov/m/pubmed/22093944"
                      ],
                      "name": "方案3：CVP+利妥昔单抗",
                      "nameNum": "方案3",
                      "nameTitle": "CVP+利妥昔单抗",
                      "overallResponse": "",
                      "prescriptionVersion": "2018.V3",
                      "price": 0,
                      "remark": "",
                      "stage": "ⅡB",
                      "tag": "ⅡB化疗：一线治疗，＋ISRT",
                      "tag1": "化疗",
                      "tag2": "一线治疗",
                      "tag3": "＋ISRT",
                      "tagRemark": ""
                    }
                  ],
                  "tag": "ⅡB化疗：一线治疗，＋ISRT",
                  "tag3": "＋ISRT",
                  "tagRemark": ""
                }
              ]
            },
            {
              "click": 0,
              "list": [],
              "tag2": "二线治疗",
              "tag2List": [
                {
                  "click": 1,
                  "list": [
                    {
                      "cancer": "霍奇金淋巴瘤",
                      "ctList": [],
                      "favorite": 0,
                      "id": "5e1fdb935620710077ebb410",
                      "literature": [
                        "http://www.ncbi.nlm.nih.gov/m/pubmed/12377653",
                        "http://www.ncbi.nlm.nih.gov/m/pubmed/18443961"
                      ],
                      "name": "方案1：DHAP",
                      "nameNum": "方案1",
                      "nameTitle": "DHAP",
                      "overallResponse": "",
                      "prescriptionVersion": "2018.V3",
                      "price": 0,
                      "remark": "",
                      "stage": "ⅡB",
                      "tag": "ⅡB化疗：二线治疗，复发/难治患者",
                      "tag1": "化疗",
                      "tag2": "二线治疗",
                      "tag3": "复发/难治患者",
                      "tagRemark": ""
                    },
                    {
                      "cancer": "霍奇金淋巴瘤",
                      "ctList": [],
                      "favorite": 0,
                      "id": "5e1fdb955620710077ebb424",
                      "literature": [
                        "http://www.ncbi.nlm.nih.gov/m/pubmed/10416011",
                        "http://www.ncbi.nlm.nih.gov/m/pubmed/24863692",
                        "http://www.ncbi.nlm.nih.gov/m/pubmed/19889622"
                      ],
                      "name": "方案2：ESHAP",
                      "nameNum": "方案2",
                      "nameTitle": "ESHAP",
                      "overallResponse": "",
                      "prescriptionVersion": "2018.V3",
                      "price": 0,
                      "remark": "",
                      "stage": "ⅡB",
                      "tag": "ⅡB化疗：二线治疗，复发/难治患者",
                      "tag1": "化疗",
                      "tag2": "二线治疗",
                      "tag3": "复发/难治患者",
                      "tagRemark": ""
                    },
                    {
                      "cancer": "霍奇金淋巴瘤",
                      "ctList": [],
                      "favorite": 0,
                      "id": "5e1fdb965620710077ebb42f",
                      "literature": [
                        "http://www.ncbi.nlm.nih.gov/m/pubmed/11157476",
                        "http://www.ncbi.nlm.nih.gov/m/pubmed/18443961"
                      ],
                      "name": "方案3：ICE",
                      "nameNum": "方案3",
                      "nameTitle": "ICE",
                      "overallResponse": "",
                      "prescriptionVersion": "2018.V3",
                      "price": 0,
                      "remark": "",
                      "stage": "ⅡB",
                      "tag": "ⅡB化疗：二线治疗，复发/难治患者",
                      "tag1": "化疗",
                      "tag2": "二线治疗",
                      "tag3": "复发/难治患者",
                      "tagRemark": ""
                    },
                    {
                      "cancer": "霍奇金淋巴瘤",
                      "ctList": [],
                      "favorite": 0,
                      "id": "5e1fdb98dd3c13006aef55f1",
                      "literature": [
                        "http://www.ncbi.nlm.nih.gov/m/pubmed/17229633"
                      ],
                      "name": "方案4：IGEV",
                      "nameNum": "方案4",
                      "nameTitle": "IGEV",
                      "overallResponse": "",
                      "prescriptionVersion": "2018.V3",
                      "price": 0,
                      "remark": "",
                      "stage": "ⅡB",
                      "tag": "ⅡB化疗：二线治疗，复发/难治患者",
                      "tag1": "化疗",
                      "tag2": "二线治疗",
                      "tag3": "复发/难治患者",
                      "tagRemark": ""
                    }
                  ],
                  "tag": "ⅡB化疗：二线治疗，复发/难治患者",
                  "tag3": "复发/难治患者",
                  "tagRemark": ""
                }
              ]
            }
          ]
        }
      ]
    },
    {
      "stage": "ⅢA",
      "stageList": [
        {
          "tag1": "化疗",
          "tag1List": [
            {
              "click": 0,
              "list": [],
              "tag2": "一线治疗",
              "tag2List": [
                {
                  "click": 1,
                  "list": [
                    {
                      "cancer": "霍奇金淋巴瘤",
                      "ctList": [],
                      "favorite": 0,
                      "id": "5e1fdb9a7796d9006a403e24",
                      "literature": [
                        "http://www.ncbi.nlm.nih.gov/m/pubmed/21873543",
                        "http://www.ncbi.nlm.nih.gov/m/pubmed/19933898 "
                      ],
                      "name": "方案1：ABVD+利妥昔单抗",
                      "nameNum": "方案1",
                      "nameTitle": "ABVD+利妥昔单抗",
                      "overallResponse": "",
                      "prescriptionVersion": "2018.V3",
                      "price": 0,
                      "remark": "",
                      "stage": "ⅢA",
                      "tag": "ⅢA化疗：一线治疗，± ISRT",
                      "tag1": "化疗",
                      "tag2": "一线治疗",
                      "tag3": "± ISRT",
                      "tagRemark": ""
                    },
                    {
                      "cancer": "霍奇金淋巴瘤",
                      "ctList": [],
                      "favorite": 0,
                      "id": "5e1fdb9dfc36ed006a3cf3d1",
                      "literature": [
                        "https://ash.confex.com/ash/2010/webprogram/Paper30295.html"
                      ],
                      "name": "方案2：CHOP+利妥昔单抗",
                      "nameNum": "方案2",
                      "nameTitle": "CHOP+利妥昔单抗",
                      "overallResponse": "",
                      "prescriptionVersion": "2018.V3",
                      "price": 0,
                      "remark": "",
                      "stage": "ⅢA",
                      "tag": "ⅢA化疗：一线治疗，± ISRT",
                      "tag1": "化疗",
                      "tag2": "一线治疗",
                      "tag3": "± ISRT",
                      "tagRemark": ""
                    },
                    {
                      "cancer": "霍奇金淋巴瘤",
                      "ctList": [],
                      "favorite": 0,
                      "id": "5e1fdba05620710077ebb495",
                      "literature": [
                        "http://www.ncbi.nlm.nih.gov/m/pubmed/22093944"
                      ],
                      "name": "方案3：CVP+利妥昔单抗",
                      "nameNum": "方案3",
                      "nameTitle": "CVP+利妥昔单抗",
                      "overallResponse": "",
                      "prescriptionVersion": "2018.V3",
                      "price": 0,
                      "remark": "",
                      "stage": "ⅢA",
                      "tag": "ⅢA化疗：一线治疗，± ISRT",
                      "tag1": "化疗",
                      "tag2": "一线治疗",
                      "tag3": "± ISRT",
                      "tagRemark": ""
                    },
                    {
                      "cancer": "霍奇金淋巴瘤",
                      "ctList": [],
                      "favorite": 0,
                      "id": "5e1fdba17796d9006a403e6c",
                      "literature": [
                        "http://www.ncbi.nlm.nih.gov/m/pubmed/12586628",
                        "http://www.ncbi.nlm.nih.gov/m/pubmed/17938252",
                        "http://abstracts.hematologylibrary.org/cgi/content/abstract/110/11/644",
                        "http://www.ncbi.nlm.nih.gov/m/pubmed/21828141"
                      ],
                      "name": "方案4：利妥昔单抗单药",
                      "nameNum": "方案4",
                      "nameTitle": "利妥昔单抗单药",
                      "overallResponse": "",
                      "prescriptionVersion": "2018.V3",
                      "price": 0,
                      "remark": "",
                      "stage": "ⅢA",
                      "tag": "ⅢA化疗：一线治疗，± ISRT",
                      "tag1": "化疗",
                      "tag2": "一线治疗",
                      "tag3": "± ISRT",
                      "tagRemark": ""
                    }
                  ],
                  "tag": "ⅢA化疗：一线治疗，± ISRT",
                  "tag3": "± ISRT",
                  "tagRemark": ""
                }
              ]
            },
            {
              "click": 0,
              "list": [],
              "tag2": "二线治疗",
              "tag2List": [
                {
                  "click": 1,
                  "list": [
                    {
                      "cancer": "霍奇金淋巴瘤",
                      "ctList": [],
                      "favorite": 0,
                      "id": "5e1fdba17d5774006af722a1",
                      "literature": [
                        "http://www.ncbi.nlm.nih.gov/m/pubmed/12377653",
                        "http://www.ncbi.nlm.nih.gov/m/pubmed/18443961"
                      ],
                      "name": "方案1：DHAP",
                      "nameNum": "方案1",
                      "nameTitle": "DHAP",
                      "overallResponse": "",
                      "prescriptionVersion": "2018.V3",
                      "price": 0,
                      "remark": "",
                      "stage": "ⅢA",
                      "tag": "ⅢA化疗：二线治疗，复发/难治患者",
                      "tag1": "化疗",
                      "tag2": "二线治疗",
                      "tag3": "复发/难治患者",
                      "tagRemark": ""
                    },
                    {
                      "cancer": "霍奇金淋巴瘤",
                      "ctList": [],
                      "favorite": 0,
                      "id": "5e1fdba37d5774006af722ad",
                      "literature": [
                        "http://www.ncbi.nlm.nih.gov/m/pubmed/10416011",
                        "http://www.ncbi.nlm.nih.gov/m/pubmed/24863692",
                        "http://www.ncbi.nlm.nih.gov/m/pubmed/19889622"
                      ],
                      "name": "方案2：ESHAP",
                      "nameNum": "方案2",
                      "nameTitle": "ESHAP",
                      "overallResponse": "",
                      "prescriptionVersion": "2018.V3",
                      "price": 0,
                      "remark": "",
                      "stage": "ⅢA",
                      "tag": "ⅢA化疗：二线治疗，复发/难治患者",
                      "tag1": "化疗",
                      "tag2": "二线治疗",
                      "tag3": "复发/难治患者",
                      "tagRemark": ""
                    },
                    {
                      "cancer": "霍奇金淋巴瘤",
                      "ctList": [],
                      "favorite": 0,
                      "id": "5e1fdba55620710077ebb4d7",
                      "literature": [
                        "http://www.ncbi.nlm.nih.gov/m/pubmed/11157476",
                        "http://www.ncbi.nlm.nih.gov/m/pubmed/18443961"
                      ],
                      "name": "方案3：ICE",
                      "nameNum": "方案3",
                      "nameTitle": "ICE",
                      "overallResponse": "",
                      "prescriptionVersion": "2018.V3",
                      "price": 0,
                      "remark": "",
                      "stage": "ⅢA",
                      "tag": "ⅢA化疗：二线治疗，复发/难治患者",
                      "tag1": "化疗",
                      "tag2": "二线治疗",
                      "tag3": "复发/难治患者",
                      "tagRemark": ""
                    },
                    {
                      "cancer": "霍奇金淋巴瘤",
                      "ctList": [],
                      "favorite": 0,
                      "id": "5e1fdba75620710077ebb503",
                      "literature": [
                        "http://www.ncbi.nlm.nih.gov/m/pubmed/17229633"
                      ],
                      "name": "方案4：IGEV",
                      "nameNum": "方案4",
                      "nameTitle": "IGEV",
                      "overallResponse": "",
                      "prescriptionVersion": "2018.V3",
                      "price": 0,
                      "remark": "",
                      "stage": "ⅢA",
                      "tag": "ⅢA化疗：二线治疗，复发/难治患者",
                      "tag1": "化疗",
                      "tag2": "二线治疗",
                      "tag3": "复发/难治患者",
                      "tagRemark": ""
                    }
                  ],
                  "tag": "ⅢA化疗：二线治疗，复发/难治患者",
                  "tag3": "复发/难治患者",
                  "tagRemark": ""
                }
              ]
            }
          ]
        }
      ]
    },
    {
      "stage": "ⅢB",
      "stageList": [
        {
          "tag1": "化疗",
          "tag1List": [
            {
              "click": 0,
              "list": [],
              "tag2": "一线治疗",
              "tag2List": [
                {
                  "click": 1,
                  "list": [
                    {
                      "cancer": "霍奇金淋巴瘤",
                      "ctList": [],
                      "favorite": 0,
                      "id": "5e1fdbaa21460d006aba35ac",
                      "literature": [
                        "http://www.ncbi.nlm.nih.gov/m/pubmed/21873543",
                        "http://www.ncbi.nlm.nih.gov/m/pubmed/19933898 "
                      ],
                      "name": "方案1：ABVD+利妥昔单抗",
                      "nameNum": "方案1",
                      "nameTitle": "ABVD+利妥昔单抗",
                      "overallResponse": "",
                      "prescriptionVersion": "2018.V3",
                      "price": 0,
                      "remark": "",
                      "stage": "ⅢB",
                      "tag": "ⅢB化疗：一线治疗，± ISRT",
                      "tag1": "化疗",
                      "tag2": "一线治疗",
                      "tag3": "± ISRT",
                      "tagRemark": ""
                    },
                    {
                      "cancer": "霍奇金淋巴瘤",
                      "ctList": [],
                      "favorite": 0,
                      "id": "5e1fdbac7d5774006af7237f",
                      "literature": [
                        "https://ash.confex.com/ash/2010/webprogram/Paper30295.html"
                      ],
                      "name": "方案2：CHOP+利妥昔单抗",
                      "nameNum": "方案2",
                      "nameTitle": "CHOP+利妥昔单抗",
                      "overallResponse": "",
                      "prescriptionVersion": "2018.V3",
                      "price": 0,
                      "remark": "",
                      "stage": "ⅢB",
                      "tag": "ⅢB化疗：一线治疗，± ISRT",
                      "tag1": "化疗",
                      "tag2": "一线治疗",
                      "tag3": "± ISRT",
                      "tagRemark": ""
                    },
                    {
                      "cancer": "霍奇金淋巴瘤",
                      "ctList": [],
                      "favorite": 0,
                      "id": "5e1fdbae21b47e007056a36b",
                      "literature": [
                        "http://www.ncbi.nlm.nih.gov/m/pubmed/22093944"
                      ],
                      "name": "方案3：CVP+利妥昔单抗",
                      "nameNum": "方案3",
                      "nameTitle": "CVP+利妥昔单抗",
                      "overallResponse": "",
                      "prescriptionVersion": "2018.V3",
                      "price": 0,
                      "remark": "",
                      "stage": "ⅢB",
                      "tag": "ⅢB化疗：一线治疗，± ISRT",
                      "tag1": "化疗",
                      "tag2": "一线治疗",
                      "tag3": "± ISRT",
                      "tagRemark": ""
                    }
                  ],
                  "tag": "ⅢB化疗：一线治疗，± ISRT",
                  "tag3": "± ISRT",
                  "tagRemark": ""
                }
              ]
            },
            {
              "click": 0,
              "list": [],
              "tag2": "二线治疗",
              "tag2List": [
                {
                  "click": 1,
                  "list": [
                    {
                      "cancer": "霍奇金淋巴瘤",
                      "ctList": [],
                      "favorite": 0,
                      "id": "5e1fdbaf7d5774006af723c2",
                      "literature": [
                        "http://www.ncbi.nlm.nih.gov/m/pubmed/12377653",
                        "http://www.ncbi.nlm.nih.gov/m/pubmed/18443961"
                      ],
                      "name": "方案1：DHAP",
                      "nameNum": "方案1",
                      "nameTitle": "DHAP",
                      "overallResponse": "",
                      "prescriptionVersion": "2018.V3",
                      "price": 0,
                      "remark": "",
                      "stage": "ⅢB",
                      "tag": "ⅢB化疗：二线治疗，复发/难治患者",
                      "tag1": "化疗",
                      "tag2": "二线治疗",
                      "tag3": "复发/难治患者",
                      "tagRemark": ""
                    },
                    {
                      "cancer": "霍奇金淋巴瘤",
                      "ctList": [],
                      "favorite": 0,
                      "id": "5e1fdbb17d5774006af723d3",
                      "literature": [
                        "http://www.ncbi.nlm.nih.gov/m/pubmed/10416011",
                        "http://www.ncbi.nlm.nih.gov/m/pubmed/24863692",
                        "http://www.ncbi.nlm.nih.gov/m/pubmed/19889622"
                      ],
                      "name": "方案2：ESHAP",
                      "nameNum": "方案2",
                      "nameTitle": "ESHAP",
                      "overallResponse": "",
                      "prescriptionVersion": "2018.V3",
                      "price": 0,
                      "remark": "",
                      "stage": "ⅢB",
                      "tag": "ⅢB化疗：二线治疗，复发/难治患者",
                      "tag1": "化疗",
                      "tag2": "二线治疗",
                      "tag3": "复发/难治患者",
                      "tagRemark": ""
                    },
                    {
                      "cancer": "霍奇金淋巴瘤",
                      "ctList": [],
                      "favorite": 0,
                      "id": "5e1fdbb443c257006f17a5df",
                      "literature": [
                        "http://www.ncbi.nlm.nih.gov/m/pubmed/11157476",
                        "http://www.ncbi.nlm.nih.gov/m/pubmed/18443961"
                      ],
                      "name": "方案3：ICE",
                      "nameNum": "方案3",
                      "nameTitle": "ICE",
                      "overallResponse": "",
                      "prescriptionVersion": "2018.V3",
                      "price": 0,
                      "remark": "",
                      "stage": "ⅢB",
                      "tag": "ⅢB化疗：二线治疗，复发/难治患者",
                      "tag1": "化疗",
                      "tag2": "二线治疗",
                      "tag3": "复发/难治患者",
                      "tagRemark": ""
                    },
                    {
                      "cancer": "霍奇金淋巴瘤",
                      "ctList": [],
                      "favorite": 0,
                      "id": "5e1fdbb57796d9006a403f67",
                      "literature": [
                        "http://www.ncbi.nlm.nih.gov/m/pubmed/17229633"
                      ],
                      "name": "方案4：IGEV",
                      "nameNum": "方案4",
                      "nameTitle": "IGEV",
                      "overallResponse": "",
                      "prescriptionVersion": "2018.V3",
                      "price": 0,
                      "remark": "",
                      "stage": "ⅢB",
                      "tag": "ⅢB化疗：二线治疗，复发/难治患者",
                      "tag1": "化疗",
                      "tag2": "二线治疗",
                      "tag3": "复发/难治患者",
                      "tagRemark": ""
                    }
                  ],
                  "tag": "ⅢB化疗：二线治疗，复发/难治患者",
                  "tag3": "复发/难治患者",
                  "tagRemark": ""
                }
              ]
            }
          ]
        }
      ]
    },
    {
      "stage": "ⅣA",
      "stageList": [
        {
          "tag1": "化疗",
          "tag1List": [
            {
              "click": 0,
              "list": [],
              "tag2": "一线治疗",
              "tag2List": [
                {
                  "click": 1,
                  "list": [
                    {
                      "cancer": "霍奇金淋巴瘤",
                      "ctList": [],
                      "favorite": 0,
                      "id": "5e1fdbb943c257006f17a611",
                      "literature": [
                        "http://www.ncbi.nlm.nih.gov/m/pubmed/21873543",
                        "http://www.ncbi.nlm.nih.gov/m/pubmed/19933898 "
                      ],
                      "name": "方案1：ABVD+利妥昔单抗",
                      "nameNum": "方案1",
                      "nameTitle": "ABVD+利妥昔单抗",
                      "overallResponse": "",
                      "prescriptionVersion": "2018.V3",
                      "price": 0,
                      "remark": "",
                      "stage": "ⅣA",
                      "tag": "ⅣA化疗：一线治疗，± ISRT",
                      "tag1": "化疗",
                      "tag2": "一线治疗",
                      "tag3": "± ISRT",
                      "tagRemark": ""
                    },
                    {
                      "cancer": "霍奇金淋巴瘤",
                      "ctList": [],
                      "favorite": 0,
                      "id": "5e1fdbbbdd3c13006aef57a2",
                      "literature": [
                        "https://ash.confex.com/ash/2010/webprogram/Paper30295.html"
                      ],
                      "name": "方案2：CHOP+利妥昔单抗",
                      "nameNum": "方案2",
                      "nameTitle": "CHOP+利妥昔单抗",
                      "overallResponse": "",
                      "prescriptionVersion": "2018.V3",
                      "price": 0,
                      "remark": "",
                      "stage": "ⅣA",
                      "tag": "ⅣA化疗：一线治疗，± ISRT",
                      "tag1": "化疗",
                      "tag2": "一线治疗",
                      "tag3": "± ISRT",
                      "tagRemark": ""
                    },
                    {
                      "cancer": "霍奇金淋巴瘤",
                      "ctList": [],
                      "favorite": 0,
                      "id": "5e1fdbbe21b47e007056a446",
                      "literature": [
                        "http://www.ncbi.nlm.nih.gov/m/pubmed/22093944"
                      ],
                      "name": "方案3：CVP+利妥昔单抗",
                      "nameNum": "方案3",
                      "nameTitle": "CVP+利妥昔单抗",
                      "overallResponse": "",
                      "prescriptionVersion": "2018.V3",
                      "price": 0,
                      "remark": "",
                      "stage": "ⅣA",
                      "tag": "ⅣA化疗：一线治疗，± ISRT",
                      "tag1": "化疗",
                      "tag2": "一线治疗",
                      "tag3": "± ISRT",
                      "tagRemark": ""
                    },
                    {
                      "cancer": "霍奇金淋巴瘤",
                      "ctList": [],
                      "favorite": 0,
                      "id": "5e1fdbbffc36ed006a3cf575",
                      "literature": [
                        "http://www.ncbi.nlm.nih.gov/m/pubmed/12586628",
                        "http://www.ncbi.nlm.nih.gov/m/pubmed/17938252",
                        "http://abstracts.hematologylibrary.org/cgi/content/abstract/110/11/644",
                        "http://www.ncbi.nlm.nih.gov/m/pubmed/21828141"
                      ],
                      "name": "方案4：利妥昔单抗单药",
                      "nameNum": "方案4",
                      "nameTitle": "利妥昔单抗单药",
                      "overallResponse": "",
                      "prescriptionVersion": "2018.V3",
                      "price": 0,
                      "remark": "",
                      "stage": "ⅣA",
                      "tag": "ⅣA化疗：一线治疗，± ISRT",
                      "tag1": "化疗",
                      "tag2": "一线治疗",
                      "tag3": "± ISRT",
                      "tagRemark": ""
                    }
                  ],
                  "tag": "ⅣA化疗：一线治疗，± ISRT",
                  "tag3": "± ISRT",
                  "tagRemark": ""
                }
              ]
            },
            {
              "click": 0,
              "list": [],
              "tag2": "二线治疗",
              "tag2List": [
                {
                  "click": 1,
                  "list": [
                    {
                      "cancer": "霍奇金淋巴瘤",
                      "ctList": [],
                      "favorite": 0,
                      "id": "5e1fdbc043c257006f17a659",
                      "literature": [
                        "http://www.ncbi.nlm.nih.gov/m/pubmed/12377653",
                        "http://www.ncbi.nlm.nih.gov/m/pubmed/18443961"
                      ],
                      "name": "方案1：DHAP",
                      "nameNum": "方案1",
                      "nameTitle": "DHAP",
                      "overallResponse": "",
                      "prescriptionVersion": "2018.V3",
                      "price": 0,
                      "remark": "",
                      "stage": "ⅣA",
                      "tag": "ⅣA化疗：二线治疗，复发/难治患者",
                      "tag1": "化疗",
                      "tag2": "二线治疗",
                      "tag3": "复发/难治患者",
                      "tagRemark": ""
                    },
                    {
                      "cancer": "霍奇金淋巴瘤",
                      "ctList": [],
                      "favorite": 0,
                      "id": "5e1fdbc27796d9006a403ffc",
                      "literature": [
                        "http://www.ncbi.nlm.nih.gov/m/pubmed/10416011",
                        "http://www.ncbi.nlm.nih.gov/m/pubmed/24863692",
                        "http://www.ncbi.nlm.nih.gov/m/pubmed/19889622"
                      ],
                      "name": "方案2：ESHAP",
                      "nameNum": "方案2",
                      "nameTitle": "ESHAP",
                      "overallResponse": "",
                      "prescriptionVersion": "2018.V3",
                      "price": 0,
                      "remark": "",
                      "stage": "ⅣA",
                      "tag": "ⅣA化疗：二线治疗，复发/难治患者",
                      "tag1": "化疗",
                      "tag2": "二线治疗",
                      "tag3": "复发/难治患者",
                      "tagRemark": ""
                    },
                    {
                      "cancer": "霍奇金淋巴瘤",
                      "ctList": [],
                      "favorite": 0,
                      "id": "5e1fdbc37796d9006a40400e",
                      "literature": [
                        "http://www.ncbi.nlm.nih.gov/m/pubmed/11157476",
                        "http://www.ncbi.nlm.nih.gov/m/pubmed/18443961"
                      ],
                      "name": "方案3：ICE",
                      "nameNum": "方案3",
                      "nameTitle": "ICE",
                      "overallResponse": "",
                      "prescriptionVersion": "2018.V3",
                      "price": 0,
                      "remark": "",
                      "stage": "ⅣA",
                      "tag": "ⅣA化疗：二线治疗，复发/难治患者",
                      "tag1": "化疗",
                      "tag2": "二线治疗",
                      "tag3": "复发/难治患者",
                      "tagRemark": ""
                    },
                    {
                      "cancer": "霍奇金淋巴瘤",
                      "ctList": [],
                      "favorite": 0,
                      "id": "5e1fdbc57d5774006af724c8",
                      "literature": [
                        "http://www.ncbi.nlm.nih.gov/m/pubmed/17229633"
                      ],
                      "name": "方案4：IGEV",
                      "nameNum": "方案4",
                      "nameTitle": "IGEV",
                      "overallResponse": "",
                      "prescriptionVersion": "2018.V3",
                      "price": 0,
                      "remark": "",
                      "stage": "ⅣA",
                      "tag": "ⅣA化疗：二线治疗，复发/难治患者",
                      "tag1": "化疗",
                      "tag2": "二线治疗",
                      "tag3": "复发/难治患者",
                      "tagRemark": ""
                    }
                  ],
                  "tag": "ⅣA化疗：二线治疗，复发/难治患者",
                  "tag3": "复发/难治患者",
                  "tagRemark": ""
                }
              ]
            }
          ]
        }
      ]
    },
    {
      "stage": "ⅣB",
      "stageList": [
        {
          "tag1": "化疗",
          "tag1List": [
            {
              "click": 0,
              "list": [],
              "tag2": "一线治疗",
              "tag2List": [
                {
                  "click": 1,
                  "list": [
                    {
                      "cancer": "霍奇金淋巴瘤",
                      "ctList": [],
                      "favorite": 0,
                      "id": "5e1fdbc721b47e007056a503",
                      "literature": [
                        "http://www.ncbi.nlm.nih.gov/m/pubmed/21873543",
                        "http://www.ncbi.nlm.nih.gov/m/pubmed/19933898 "
                      ],
                      "name": "方案1：ABVD+利妥昔单抗",
                      "nameNum": "方案1",
                      "nameTitle": "ABVD+利妥昔单抗",
                      "overallResponse": "",
                      "prescriptionVersion": "2018.V3",
                      "price": 0,
                      "remark": "",
                      "stage": "ⅣB",
                      "tag": "ⅣB化疗：一线治疗，± ISRT",
                      "tag1": "化疗",
                      "tag2": "一线治疗",
                      "tag3": "± ISRT",
                      "tagRemark": ""
                    },
                    {
                      "cancer": "霍奇金淋巴瘤",
                      "ctList": [],
                      "favorite": 0,
                      "id": "5e1fdbc943c257006f17a6fb",
                      "literature": [
                        "https://ash.confex.com/ash/2010/webprogram/Paper30295.html"
                      ],
                      "name": "方案2：CHOP+利妥昔单抗",
                      "nameNum": "方案2",
                      "nameTitle": "CHOP+利妥昔单抗",
                      "overallResponse": "",
                      "prescriptionVersion": "2018.V3",
                      "price": 0,
                      "remark": "",
                      "stage": "ⅣB",
                      "tag": "ⅣB化疗：一线治疗，± ISRT",
                      "tag1": "化疗",
                      "tag2": "一线治疗",
                      "tag3": "± ISRT",
                      "tagRemark": ""
                    },
                    {
                      "cancer": "霍奇金淋巴瘤",
                      "ctList": [],
                      "favorite": 0,
                      "id": "5e1fdbcb21460d006aba37a2",
                      "literature": [
                        "http://www.ncbi.nlm.nih.gov/m/pubmed/22093944"
                      ],
                      "name": "方案3：CVP+利妥昔单抗",
                      "nameNum": "方案3",
                      "nameTitle": "CVP+利妥昔单抗",
                      "overallResponse": "",
                      "prescriptionVersion": "2018.V3",
                      "price": 0,
                      "remark": "",
                      "stage": "ⅣB",
                      "tag": "ⅣB化疗：一线治疗，± ISRT",
                      "tag1": "化疗",
                      "tag2": "一线治疗",
                      "tag3": "± ISRT",
                      "tagRemark": ""
                    }
                  ],
                  "tag": "ⅣB化疗：一线治疗，± ISRT",
                  "tag3": "± ISRT",
                  "tagRemark": ""
                }
              ]
            },
            {
              "click": 0,
              "list": [],
              "tag2": "二线治疗",
              "tag2List": [
                {
                  "click": 1,
                  "list": [
                    {
                      "cancer": "霍奇金淋巴瘤",
                      "ctList": [],
                      "favorite": 0,
                      "id": "5e1fdbcdfc36ed006a3cf62e",
                      "literature": [
                        "http://www.ncbi.nlm.nih.gov/m/pubmed/12377653",
                        "http://www.ncbi.nlm.nih.gov/m/pubmed/18443961"
                      ],
                      "name": "方案1：DHAP",
                      "nameNum": "方案1",
                      "nameTitle": "DHAP",
                      "overallResponse": "",
                      "prescriptionVersion": "2018.V3",
                      "price": 0,
                      "remark": "",
                      "stage": "ⅣB",
                      "tag": "ⅣB化疗：二线治疗，复发/难治患者",
                      "tag1": "化疗",
                      "tag2": "二线治疗",
                      "tag3": "复发/难治患者",
                      "tagRemark": ""
                    },
                    {
                      "cancer": "霍奇金淋巴瘤",
                      "ctList": [],
                      "favorite": 0,
                      "id": "5e1fdbcf43c257006f17a751",
                      "literature": [
                        "http://www.ncbi.nlm.nih.gov/m/pubmed/10416011",
                        "http://www.ncbi.nlm.nih.gov/m/pubmed/24863692",
                        "http://www.ncbi.nlm.nih.gov/m/pubmed/19889622"
                      ],
                      "name": "方案2：ESHAP",
                      "nameNum": "方案2",
                      "nameTitle": "ESHAP",
                      "overallResponse": "",
                      "prescriptionVersion": "2018.V3",
                      "price": 0,
                      "remark": "",
                      "stage": "ⅣB",
                      "tag": "ⅣB化疗：二线治疗，复发/难治患者",
                      "tag1": "化疗",
                      "tag2": "二线治疗",
                      "tag3": "复发/难治患者",
                      "tagRemark": ""
                    },
                    {
                      "cancer": "霍奇金淋巴瘤",
                      "ctList": [],
                      "favorite": 0,
                      "id": "5e1fdbd121b47e007056a587",
                      "literature": [
                        "http://www.ncbi.nlm.nih.gov/m/pubmed/11157476",
                        "http://www.ncbi.nlm.nih.gov/m/pubmed/18443961"
                      ],
                      "name": "方案3：ICE",
                      "nameNum": "方案3",
                      "nameTitle": "ICE",
                      "overallResponse": "",
                      "prescriptionVersion": "2018.V3",
                      "price": 0,
                      "remark": "",
                      "stage": "ⅣB",
                      "tag": "ⅣB化疗：二线治疗，复发/难治患者",
                      "tag1": "化疗",
                      "tag2": "二线治疗",
                      "tag3": "复发/难治患者",
                      "tagRemark": ""
                    },
                    {
                      "cancer": "霍奇金淋巴瘤",
                      "ctList": [],
                      "favorite": 0,
                      "id": "5e1fdbd25620710077ebb738",
                      "literature": [
                        "http://www.ncbi.nlm.nih.gov/m/pubmed/17229633"
                      ],
                      "name": "方案4：IGEV",
                      "nameNum": "方案4",
                      "nameTitle": "IGEV",
                      "overallResponse": "",
                      "prescriptionVersion": "2018.V3",
                      "price": 0,
                      "remark": "",
                      "stage": "ⅣB",
                      "tag": "ⅣB化疗：二线治疗，复发/难治患者",
                      "tag1": "化疗",
                      "tag2": "二线治疗",
                      "tag3": "复发/难治患者",
                      "tagRemark": ""
                    }
                  ],
                  "tag": "ⅣB化疗：二线治疗，复发/难治患者",
                  "tag3": "复发/难治患者",
                  "tagRemark": ""
                }
              ]
            }
          ]
        }
      ]
    }
  ],
  "prescriptionVersion": "NCCN 2018.V3",
  "success": 1,
  "type": 2
}    
'''

    data1 = '''
{
    "list": [
        {
            "BriefTitle": "刘全医师：该研究尚未获得伦理委员会批准。请于批准后再开始纳入参试者，并与我们联系上传批件。 功能性内镜颅底手术联合术前诱导性介入化疗和同期放疗治疗晚期鼻腔鼻窦腺样囊性癌：前瞻性随机对照研究",
            "DrugName": "",
            "Identifier": "ChiCTR1900026122",
            "StudyPhase": "其它",
            "add_time": "2019-12-12-11:40:51"
        },
        {
            "BriefTitle": "Fluorescence-guided Surgery Using cRGD-ZW800-1 in Oral Cancer",
            "DrugName": "",
            "Identifier": "NCT04191460",
            "StudyPhase": "Phase 2",
            "add_time": "2019-12-16-10:50:56"
        }
    ],
    "location": {
        "city": "广州",
        "province": "广东"
    },
    "count": 21,
    "success": 1
}
'''
    d = json.loads(data1, encoding='utf-8')
    sortJsonData(d)
    print(d)
