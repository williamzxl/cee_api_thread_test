import requests
from utils.config import NewConfig


class PostMeasureWrite(object):
    def __init__(self, common, headers, accesstoken):
        self.headers = headers
        self.baseUrl = common.get('baseUrl')
        self.accesstoken = accesstoken
        self.headers.update({"accesstoken": self.accesstoken})

    def post_measure_Write(self, measureID, userAnswer):
        url = "{}/userMeasure/{}/measureData".format(self.baseUrl, measureID)
        for u in userAnswer:
            data = {"elapsedSec":29,"stepType":0}
            data.update(u)
            response = requests.request("POST", url, headers=self.headers, json=data)
            print("response.text", response.text)
            print(eval(response.text).get('data') != None)
            if len(eval(response.text).get('data')) != 0:
                return eval(response.text).get('data')


if __name__ == '__main__':
    cfg_info = NewConfig()
    devices = cfg_info.get_info('vivox6')
    c, h = cfg_info.get_info("vivox6")
    print(c)
    print(h)
    a = 'dad46a52-0542-4f39-a371-3b47e05af4b8'
    at = PostMeasureRead(c, h, a)
    s = at.post_measure_read()
