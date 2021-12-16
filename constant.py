import os

USERS = eval(os.environ['USERS'])
SERVER_KEY = os.environ['SERVER_KEY']


LOGIN_API = 'https://app.bupt.edu.cn/uc/wap/login/check'
GET_API = 'https://app.bupt.edu.cn/ncov/wap/default/index'
REPORT_API = 'https://app.bupt.edu.cn/ncov/wap/default/save'

# 当今日没有填报时，在https://app.bupt.edu.cn/ncov/wap/default/index下进行填报，
# 全部填完，不要提交，f12打开控制台，在Console页面下输入代码 console.log(vm.info) 就会得到以下信息，之后每天就默认填以下信息
INFO = r"""{
        address: "北京市昌平区沙河镇北京邮电大学沙河校区雁北园男生宿舍",
​
area: "北京市  昌平区",
​
bztcyy: "",
​
city: "北京市",
​
created: 1639585453,
​
created_uid: 0,
​
csmjry: "0",
​
date: "20211216",
​
geo_api_info: "{\"type\":\"complete\",\"position\":{\"Q\":40.157922634549,\"R\":116.28848578559098,\"lng\":116.288486,\"lat\":40.157923},\"location_type\":\"html5\",\"message\":\"Get ipLocation failed.Get geolocation success.Convert Success.Get address success.\",\"accuracy\":76,\"isConverted\":true,\"status\":1,\"addressComponent\":{\"citycode\":\"010\",\"adcode\":\"110114\",\"businessAreas\":[{\"name\":\"沙河\",\"id\":\"110114\",\"location\":{\"Q\":40.134237,\"R\":116.28009600000001,\"lng\":116.280096,\"lat\":40.134237}},{\"name\":\"百善\",\"id\":\"110114\",\"location\":{\"Q\":40.175749,\"R\":116.32030500000002,\"lng\":116.320305,\"lat\":40.175749}}],\"neighborhoodType\":\"\",\"neighborhood\":\"\",\"building\":\"\",\"buildingType\":\"\",\"street\":\"南丰路\",\"streetNumber\":\"1号\",\"country\":\"中国\",\"province\":\"北京市\",\"city\":\"\",\"district\":\"昌平区\",\"towncode\":\"110114123000\",\"township\":\"沙河镇\"},\"formattedAddress\":\"北京市昌平区沙河镇北京邮电大学沙河校区雁北园男生宿舍\",\"roads\":[],\"crosses\":[],\"pois\":[],\"info\":\"SUCCESS\"}"
​
,glksrq: "",
​
gllx: "",
​
gtjzzfjsj: "",
​
gwszdd: "",
​
id: 16000670,
​
ismoved: 0,
​
jcbhlx: "",
​
jcbhrq: "",
​
jchbryfs: "",
​
jcjg: "",
​
jcjgqr: "0",
​
jcqzrq: "",
​
jcwhryfs: "",
​
jhfjhbcc: "",
​
jhfjjtgj: "",
​
jhfjrq: "",
​
jrsfqzfy: "",
​
jrsfqzys: "",
​
mjry: "0",
​
province: "北京市",
​
qksm: "",
​
remark: "",
​
sfcxtz: "0",
​
sfcxzysx: "0",
​
sfcyglq: "0",
​
sfjcbh: "0",
​
sfjchbry: "0",
​
sfjcqz: "",
​
sfjcwhry: "0",
​
sfjzdezxgym: 1,
​
sfjzxgym: 1,
​
sfsfbh: 0,
​
sfsqhzjkk: 0,
​
sftjhb: "0",
​
sftjwh: "0",
​
sfxk: 0,
​
sfygtjzzfj: 0,
​
sfyqjzgc: "",
​
sfyyjc: "0",
​
sfzx: 1,
​
sqhzjkkys: "",
​
szcs: "",
​
szgj: "",
​
szsqsfybl: 0,
​
tw: "3",
​
uid: "83242",
​
xjzd: "",
​
xkqq: "",
​
xwxgymjzqk: 3,
​
ymjzxgqk: "",
​
zgfxdq: "0",
        }"""

REASONABLE_LENGTH = 24
TIMEOUT_SECOND = 25

class HEADERS:
    REFERER_LOGIN_API = 'https://app.bupt.edu.cn/uc/wap/login'
    REFERER_POST_API = 'https://app.bupt.edu.cn/ncov/wap/default/index'
    ORIGIN_BUPTAPP = 'https://app.bupt.edu.cn'

    UA = ('Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) '
          'Mobile/15E148 MicroMessenger/7.0.11(0x17000b21) NetType/4G Language/zh_CN')
    ACCEPT_JSON = 'application/json'
    ACCEPT_HTML = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
    REQUEST_WITH_XHR = 'XMLHttpRequest'
    ACCEPT_LANG = 'zh-cn'
    CONTENT_TYPE_UTF8 = 'application/x-www-form-urlencoded; charset=UTF-8'

    def __init__(self) -> None:
        raise NotImplementedError

COMMON_HEADERS = {
    'User-Agent': HEADERS.UA,
    'Accept-Language': HEADERS.ACCEPT_LANG,
}
COMMON_POST_HEADERS = {
    'Accept': HEADERS.ACCEPT_JSON,
    'Origin': HEADERS.ORIGIN_BUPTAPP,
    'X-Requested-With': HEADERS.REQUEST_WITH_XHR,
    'Content-Type': HEADERS.CONTENT_TYPE_UTF8,
}

from typing import Optional
from abc import ABCMeta, abstractmethod

class INotifier(metaclass=ABCMeta):
    @property
    @abstractmethod
    def PLATFORM_NAME(self) -> str:
        """
        将 PLATFORM_NAME 设为类的 Class Variable，内容是通知平台的名字（用于打日志）。
        如：PLATFORM_NAME = 'Telegram 机器人'
        :return: 通知平台名
        """
    @abstractmethod
    def notify(self, *, success, msg, data,username, name) -> None:
        """
        通过该平台通知用户操作成功的消息。失败时将抛出各种异常。
        :param success: 表示是否成功
        :param msg: 成功时表示服务器的返回值，失败时表示失败原因；None 表示没有上述内容
        :return: None
        """

