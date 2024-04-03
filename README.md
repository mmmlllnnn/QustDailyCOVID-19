# QustDailyCOVID-19

2020年青岛科技大学自动每日疫情填报

---
显然，疫情早就过去了。<br>
我最近在整理自己的代码库，就把这个传上来了。<br>
<br>


---
<br>
<br>
<br>
<br>
<br>
<br>

## 曾写拙劣文章如下
代码编辑于寒假时期，距离今天已经2个多月，本来以为疫情已经过去，谁曾想新的一波病势从青岛席卷山东，在这样的情况下，每日健康信息的准确填报变得异常重要，我们所提交的每一张form也绝对不是应付上级的一纸空文，而是对自己和他人生命的一种负责。

------------

### 用到的库
python语言
```
import requests
```

------------

### 思路

- 	提交健康打卡数据时抓个包。
- 	用requests库构造一个一样的表单，往服务器接口发送就完事了。
-	改一下表单里的日期，就可以打不同天数的了。

------------


### 过程

 

 1. 点击提交，开始抓包

![1](https://s1.ax1x.com/2022/03/15/bvO44s.png)

 2. 分析包里的字段

![2](https://s1.ax1x.com/2022/03/15/bvOLbF.png "2")

发现没有任何验证，直接构造form表单就行。

------------


### 代码

#### 1. 打卡代码：
```
# https://bpm.qust.edu.cn/bpmx/platform/form/bpmDataTemplate/editData_xsjkdk.ht		
#登录上边获取cookie
import requests
requests.packages.urllib3.disable_warnings()

cookiee='填写你的cookie'	#cookie
xmm="王大炮"		        #姓名
xuehao="1005050104"	     #学号
xy="信息学院" 	 	     #学院
bj="暴富学191" 		     #班级
zy="暴富工程" 			  #专业
nj="2077"			       #年级
sjh="110xxx"   			 #手机号
dizhi="山东省青岛市xxx"     #打卡地址
dm="1026259" 			   #班级代码
zydm="0001" 				#专业代码
#========================上面这些是需要自己改的第一个地方

#请求地址
url = 'https://bpm.qust.edu.cn/bpmx/platform/form/bpmFormHandler/save.ht'
#请求头
headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36\
         (KHTML, like Gecko) Chrome/83.0.2785.104',
        'cookie':cookiee
}
def one():
#============在这改日期，(1,32)指从1号一直打卡到31号，下面的2022-03，需要自己改月份
        for i in range(1,32):
                riqi=i
                fdata='{{"main":{{"fields":{{"xm":"{xmm}",\
                "xh":"{xuehao}",\
                "xy":"{xy}",\
                "bj":"{bj}",\
                "zy":"{zy}",\
                "nj":"{nj}",\
                "sjh":"{sjh}",\
                "tjsj":"2022-03-{riqi} 10:25:32",\
                "jssj":"2022-03-{riqi} 10:25:32",\
                "xydm":"203",\
                "zydm":"{zydm}",\
                "bjdm":"{dm}",\
                "dqszdz":"{dizhi}",\
                "stzkqt":"","jrtw":"37.2℃及以下","jrstzk":"健康","gfxqyjcs":"否","ysbrjcs":"否","ysbl":"否",\
                "yxgl":"否","jkmys":"绿色","brcn":"是"}}}},"sub":[],"opinion":[]\
                }}'.format(xmm=xmm,xuehao=xuehao,xy=xy,bj=bj,zy=zy,nj=nj,sjh=sjh,riqi=riqi,dizhi=dizhi,dm=dm,zydm=zydm)

                data={'formData':fdata,'tableId':'2000000000030000'}

                #开始请求
                m = requests.post(url,data=data,headers=headers,verify=False)
                #返回响应码
                print(m.text)
                print("第",i,"日打卡成功")
                # print(m.status_code)

one()#开始运行

```

<font color=#FF1493>需要修改两个地方：<br>
一是提交的信息，像姓名、学号、学院等等，代码的开头标出来了。<br>
二是提交的日期，在 one() 这个函数里。<br>
日期没有做验证，修改不同日期即可以提前打卡</font>


------------


#### 2.	我还抓了另外一个接口，检测是否打卡成功

```
# https://bpm.qust.edu.cn/bpmx/platform/form/bpmDataTemplate/editData_xsjkdk.ht
import requests
requests.packages.urllib3.disable_warnings()

cookiee='填写你的cookie'	#cookie
xuehao="123456789"		 #你的学号

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
    for i in range(1,10):							#1号到9号
        riqi=i
        query = '{{"F_XH":"{xuehao}","F_TJSJ":"2022-03-0{riqi}"}}'.format(xuehao=xuehao, riqi=riqi)
        data = {'alias': 'cxxsjtsfyjdk', 'page': 1, 'pagesize': 1, 'querydata': query}
        m = requests.post(url,data=data,headers=headers,verify=False)
        print("打卡情况：",m.text)

    for i in range(10,32):							#10号到31号
        riqi=i
        query = '{{"F_XH":"{xuehao}","F_TJSJ":"2022-03-{riqi}"}}'.format(xuehao=xuehao, riqi=riqi)
        data = {'alias': 'cxxsjtsfyjdk', 'page': 1, 'pagesize': 1, 'querydata': query}
        m = requests.post(url,data=data,headers=headers,verify=False)
        print("打卡情况：",m.text)


checkone()
```

<font color=#FF1493>这个简单，<br>填写学号和cookie就行了</font>



------------



### 结果

打卡成功：
![3](https://s1.ax1x.com/2022/03/15/bxPIdx.png "3")

检测结果：

![4](https://s1.ax1x.com/2022/03/15/bxPbWD.png "4")



本篇结束，下次见。









