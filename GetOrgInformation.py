import requests
import json
from pgdb import Connection
from tqdm import tqdm

if __name__ == "__main__":
    fp = open("TotalOrgInformation.json", "w")
    org_list = []
    for page1 in tqdm(range(21),desc="获取所有机构信息"):  # 首页分页
        #print("第{}页".format(page1 + 1))
        url = "https://gs.amac.org.cn/amac-infodisc/api/pof/personOrg?rand=0.21821422787959&page={}&size=10".format(page1)
        payload = "{\"page\":1,\"orgType\":\"公募基金管理公司\"}"
        payload = payload.encode("utf-8")
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
            'Content-Type': 'application/json',
        }
        verify = False
        dic_obj = requests.post(url=url, headers=headers, data=payload,verify=verify)

        dic_obj=dic_obj.json()
        for dic in dic_obj["content"]:
            info_dic = {
                "机构名称":dic["orgName"],
                #"机构ID":dic["userId"],
                "机构类型":dic["orgType"],
                "员工人数":dic["extWorkerTotalNum"],
                "从业资格人数":dic["operNum"],
                "销售业务资格人数":dic["salesmanNum"],
                "基金经理数目":dic["fundManagerNum"],
                "投资经理数目":dic["investmentManagerNum"]
            }
            org_list.append(info_dic)
    json.dump(org_list,fp,ensure_ascii=False)
    fp.close()