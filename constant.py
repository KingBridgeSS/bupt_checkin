import os
import time

USERS = eval(os.environ['USERS'])
SERVER_KEY = os.environ['SERVER_KEY']


LOGIN_API = 'https://app.bupt.edu.cn/uc/wap/login/check'
GET_API = 'https://app.bupt.edu.cn/ncov/wap/default/index'
REPORT_API = 'https://app.bupt.edu.cn/ncov/wap/default/save'

# 当今日没有填报时，在https://app.bupt.edu.cn/ncov/wap/default/index下进行填报，
# 全部填完，不要提交，f12打开控制台，在Console页面下输入代码 console.log(vm.info) 就会得到以下信息，之后每天就默认填以下信息
mytime=int(time.time())#时间戳不用倒时差
mytime+=86400#为什么时间戳永远慢一天？？？
mydate=time.strftime("%Y%m%d",time.localtime(mytime+28800))#localtime要倒时差
INFO = r'{"ismoved":0,"jhfjrq":"","jhfjjtgj":"","jhfjhbcc":"","sfxk":0,"xkqq":"","szgj":"","szcs":"","zgfxdq":"0","mjry":"0","csmjry":"0","ymjzxgqk":"","xwxgymjzqk":3,"tw":"3","sfcxtz":"0","sfjcbh":"0","sfcxzysx":"0","qksm":"","sfyyjc":"0","jcjgqr":"0","remark":"","address":"广西壮族自治区柳州市柳南区鹅山街道革新路17号柳州市第四十七中学","geo_api_info":"{\"type\":\"complete\",\"info\":\"SUCCESS\",\"status\":1,\"fEa\":\"jsonp_61172_\",\"position\":{\"Q\":24.3,\"R\":109.37200000000001,\"lng\":109.372,\"lat\":24.3},\"message\":\"Get ipLocation success.Get address success.\",\"location_type\":\"ip\",\"accuracy\":null,\"isConverted\":true,\"addressComponent\":{\"citycode\":\"0772\",\"adcode\":\"450204\",\"businessAreas\":[],\"neighborhoodType\":\"\",\"neighborhood\":\"\",\"building\":\"\",\"buildingType\":\"\",\"street\":\"革新路\",\"streetNumber\":\"17号\",\"country\":\"中国\",\"province\":\"广西壮族自治区\",\"city\":\"柳州市\",\"district\":\"柳南区\",\"towncode\":\"450204005000\",\"township\":\"鹅山街道\"},\"formattedAddress\":\"广西壮族自治区柳州市柳南区鹅山街道革新路17号柳州市第四十七中学\",\"roads\":[],\"crosses\":[],\"pois\":[]}","area":"广西壮族自治区 柳州市 柳南区","province":"广西壮族自治区","city":"柳州市","sfzx":0,"sfjcwhry":"0","sfjchbry":"0","sfcyglq":"0","gllx":"","glksrq":"","jcbhlx":"","jcbhrq":"","bztcyy":"","sftjhb":"0","sftjwh":"0","sfsfbh":0,"xjzd":"广西壮族自治柳州市柳南区永前东四区15-1-602","jcwhryfs":"","jchbryfs":"","szsqsfybl":0,"sfygtjzzfj":0,"gtjzzfjsj":"","sfjzxgym":1,"sfjzdezxgym":1,"jcjg":"","date":"'+str(mydate)+'","uid":"83242","created":'+str(mytime)+',"jcqzrq":"","sfjcqz":"","sfsqhzjkk":0,"sqhzjkkys":"","created_uid":0,"id":16878191,"gwszdd":"","sfyqjzgc":"","jrsfqzys":"","jrsfqzfy":""}'
print(INFO)

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
