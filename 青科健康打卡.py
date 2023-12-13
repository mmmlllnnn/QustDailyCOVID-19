# https://bpm.qust.edu.cn/bpmx/platform/form/bpmDataTemplate/editData_xsjkdk.ht
import requests
requests.packages.urllib3.disable_warnings()

cookiee='JSESSIONID=83891FF15261B77555F9F5F5E6895F4C; route=3c7e71c590814d582364198e9cffb674'
xmm="XXX"               		#姓名
xuehao="XXXXX"       			#学号
xy="高分子科学与工程学院"     		  #学院
bj="XXXXX"               		#班级
zy="XXXXX"               		#专业
nj="XXXXX"                 		#年级
sjh="XXXXX"         			#手机号
dizhi="山东省XXXXXXXXXX"                #打卡地址
dm="XXXXX"             			#班级代码
zydm="XXXXX"               		#专业代码
riqi=20                   		#打卡日期===后面在循环中又重新赋值了，不用改
#请求地址
url = 'https://bpm.qust.edu.cn/bpmx/platform/form/bpmFormHandler/save.ht'
#请求头
headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36\
         (KHTML, like Gecko) Chrome/83.0.2785.104',
        'cookie':cookiee
}
def one():
#表单==================================在这改日期
        for i in range(15,26):
                riqi=i
                fdata = '{{"main":{{"fields":{{"xm":"{xmm}",\
                "xh":"{xuehao}",\
                "xy":"{xy}",\
                "bj":"{bj}",\
                "zy":"{zy}",\
                "nj":"{nj}",\
                "sjh":"{sjh}",\
                "tjsj":"2022-12-{riqi} 07:25:32",\
                "jssj":"2022-12-{riqi} 07:25:32",\
                "xydm":"203",\
                "zydm":"{zydm}",\
                "bjdm":"{dm}",\
                "dqszdz":"{dizhi}",\
                "stzkqt":"",\
                "nzhychsjcsj":"2022-12-{riqi}",\
                "jrtw":"37.2℃及以下",\
                "jrstzk":"健康",\
                "gfxqyjcs":"否",\
                "ysbrjcs":"否",\
                "ysbl":"否",\
                "yxgl":"否",\
                "jkmys":"绿色",\
                "nlqsfybb":"未离青",\
                "nsfyjzxgym":"已接种第3针（加强针）",\
                "brcn":"是"}}}},"sub":[],"opinion":[]\
                }}'.format(xmm=xmm, xuehao=xuehao, xy=xy, bj=bj, zy=zy, nj=nj, sjh=sjh, riqi=riqi, dizhi=dizhi, dm=dm,
                           zydm=zydm)


                data = {'formData': fdata, 'tableId': '2000000000030000', 'alias': 'xsjkdk',\
'tableName': 'xsjkdk'}
                #开始请求
                m = requests.post(url,data=data,headers=headers,verify=False)
                #返回响应码
                print(m.text)
                print("12月",i,"日打卡成功")
                # print(m.status_code)


one()#




















