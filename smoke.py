# coding: utf-8

import json
from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdkcore.region.region import Region
from huaweicloudsdkiotda.v5 import *
from huaweicloudsdkcore.auth.credentials import BasicCredentials
from huaweicloudsdkcore.auth.credentials import DerivedCredentials

if __name__ == "__main__":
    ak = "JVNP46FICU23CZNR5SIZ"
    sk = "UEuqBmtiGKuCWT9uIyu7MJBjBiw7mznPztMEQoJX"
    project_id = "5e4b50c40add47b6afa588e6855281a8"
    region_id = "cn-north-4"
    # endpoint：请在控制台的"总览"界面的"平台接入地址"中查看"应用侧"的https接入地址
    endpoint = "eb7d17a972.st1.iotda-app.cn-north-4.myhuaweicloud.com"

    # 标准版/企业版：需自行创建Region对象
    REGION = Region(region_id, endpoint)

    # 创建认证
    # 创建BasicCredentials实例并初始化
    credentials = BasicCredentials(ak, sk, project_id)
    
    # 标准版/企业版需要使用衍生算法，基础版请删除该配置
    credentials.with_derived_predicate(DerivedCredentials.get_default_derived_predicate())
    
    # 基础版：请选择IoTDAClient中的Region对象 如： .with_region(IoTDARegion.CN_NORTH_4)
    # 标准版/企业版：需要使用自行创建的Region对象
    client = IoTDAClient.new_builder() \
        .with_credentials(credentials) \
        .with_region(REGION) \
        .build()

    try:
        request = ShowDeviceShadowRequest()
        request.device_id = "64462a654f1d6803244f7357_wifi8266"
        response = client.show_device_shadow(request)
        print(response)
        print("================" )
        a=response
        object=a
        b=a.shadow[0].reported.properties
        print(type(b))
        print("Smoke_Value数值为：")
        print(b["Smoke_Value"])
        print("BeepStatus状态为：")
        print (b["BeepStatus"])
        print("=================")
        
    except exceptions.ClientRequestException as e:
        print(e.status_code)
        print(e.request_id)
        print(e.error_code)
        print(e.error_msg)    
    
def getDeviceShadow():
    ak = "JVNP46FICU23CZNR5SIZ"
    sk = "UEuqBmtiGKuCWT9uIyu7MJBjBiw7mznPztMEQoJX"
    project_id = "5e4b50c40add47b6afa588e6855281a8"
    region_id = "cn-north-4"
    # endpoint：请在控制台的"总览"界面的"平台接入地址"中查看"应用侧"的https接入地址
    endpoint = "eb7d17a972.st1.iotda-app.cn-north-4.myhuaweicloud.com"

    REGION = Region(region_id, endpoint)

    # 创建认证
    # 创建BasicCredentials实例并初始化
    credentials = BasicCredentials(ak, sk, project_id)
    
    # 标准版/企业版需要使用衍生算法，基础版请删除该配置
    credentials.with_derived_predicate(DerivedCredentials.get_default_derived_predicate())
    
    # 基础版：请选择IoTDAClient中的Region对象 如： .with_region(IoTDARegion.CN_NORTH_4)
    # 标准版/企业版：需要使用自行创建的Region对象
    client = IoTDAClient.new_builder() \
        .with_credentials(credentials) \
        .with_region(REGION) \
        .build()

    request = ShowDeviceShadowRequest()
    request.device_id = "64462a654f1d6803244f7357_wifi8266"
    response = client.show_device_shadow(request)
    #print(response)
    return response


def getProptiesValue_dict():
    request = ShowDeviceShadowRequest()
    request.device_id = "64462a654f1d6803244f7357_wifi8266"
    response = client.show_device_shadow(request)
    #print(response)
    return response


    #解析json数据并返回
def getProptiesValue_dict(response):
    response_dict_value = json.loads(str(response))
    print('烟感设备影子原始数据')
    print(response_dict_value)
    print('\n')
    response_list_value_shadow = response_dict_value['shadow']
    response_dict_value_shadow = response_list_value_shadow[0]
    response_dict_value_reported = response_dict_value_shadow['reported']
    properties_dict = response_dict_value_reported['properties']
    return properties_dict

def getvalue():
    shadowValue = getDeviceShadow()
    proptiesValue = getProptiesValue_dict(shadowValue)
    allKeys = proptiesValue.keys()
    value = []
    for c in allKeys:
        value.append(proptiesValue[c])
    return value


if __name__ == "__main__":
    print(getvalue())
    # try:
    #     # 实例化请求对象
    #     request = ListDevicesRequest()
    #     # 调用查询设备列表接口
    #     response = client.list_devices(request)
    #     print(response)
    # except exceptions.ClientRequestException as e:
    #     print(e.status_code)
    #     print(e.request_id)
    #     print(e.error_code)
    #     print(e.error_msg)