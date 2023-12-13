# https://bpm.qust.edu.cn/bpmx/platform/form/bpmDataTemplate/editData_xsjkdk.ht
import requests
requests.packages.urllib3.disable_warnings()
#cookie
cookiee='JSESSIONID=6104C486A9B9ED0825503BF7CB86D079; route=fc52df5debaf0ea17e83f3271767ddb1'
xuehao="XXXXXXX"

#请求地址
url = 'https://bpm.qust.edu.cn/bpmx/platform/bpm/bpmFormQuery/doQuery.ht'
#请求头
headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36\
         (KHTML, like Gecko) Chrome/83.0.2785.104',
        'cookie':cookiee
}
def checkone():
    # ======================查询不同日期内是否都打卡
    for i in range(10,32):
        riqi=i
        # 表单
        query = '{{"F_XH":"{xuehao}","F_TJSJ":"2022-10-{riqi}"}}'.format(xuehao=xuehao, riqi=riqi)
        data = {'alias': 'cxxsjtsfyjdk', 'page': 1, 'pagesize': 1, 'querydata': query}
        #开始请求
        m = requests.post(url,data=data,headers=headers,verify=False)
        #返回响应码
        print("打卡情况：",m.text)

def checktwo():
    for i in range(1,10):
        riqi=i
        # 表单
        query = '{{"F_XH":"{xuehao}","F_TJSJ":"2022-05-0{riqi}"}}'.format(xuehao=xuehao, riqi=riqi)
        data = {'alias': 'cxxsjtsfyjdk', 'page': 1, 'pagesize': 1, 'querydata': query}
        #开始请求
        m = requests.post(url,data=data,headers=headers,verify=False)
        #返回响应码
        print("打卡情况：",m.text)
    for i in range(10,29):
        riqi=i
        # 表单
        query = '{{"F_XH":"{xuehao}","F_TJSJ":"2022-05-{riqi}"}}'.format(xuehao=xuehao, riqi=riqi)
        data = {'alias': 'cxxsjtsfyjdk', 'page': 1, 'pagesize': 1, 'querydata': query}
        #开始请求
        m = requests.post(url,data=data,headers=headers,verify=False)
        #返回响应码
        print("打卡情况：",m.text)


checkone()

