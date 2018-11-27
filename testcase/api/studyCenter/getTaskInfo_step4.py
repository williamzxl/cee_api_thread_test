import requests
from utils.config import NewConfig


class GetTaskInfo2(object):
    def __init__(self, common, headers, accesstoken):
        self.headers = headers
        self.baseUrl = common.get('baseUrl')
        try:
            self.headers.pop('Content-Length')
        except:
            pass
        self.accesstoken = accesstoken
        self.headers.update({"accesstoken": self.accesstoken})
        self.headers.update({"Host": common.get("baseProxy")})

    def get_all_tasks_id(self, sevicesID=None):
        url = "{}/userStudyCenter/{}/taskInfo".format(self.baseUrl, sevicesID)
        querystring = {"taskID": ""}
        response = requests.request("GET", url, headers=self.headers, params=querystring)
        data = eval(response.text).get("data")
        message = eval(response.text).get("message")
        if message == "success":
            practice = data.get('practice')
            all_tasks = []
            for p in practice:
                print("P", p)
                if p.get("studyType") == "VOC":
                    lists = p.get("questGuide")
                    voc = {"VOC": lists}
                    all_tasks.append(voc)
                if p.get("studyType") == "LIS":
                    listens = p.get("questGuide")
                    listen = {"LIS": listens}
                    all_tasks.append(listen)
                if p.get("studyType") == "RID":
                    reads = p.get("questGuide")
                    read = {"RID": reads}
                    all_tasks.append(read)
                if p.get("studyType") == "WRI":
                    writes = p.get("questGuide")
                    write = {"WRI": writes}
                    all_tasks.append(write)
                if p.get("studyType") == "GRA":
                    gras = p.get("questGuide")
                    gra = {"GRA": gras}
                    all_tasks.append(gra)
            return all_tasks


if __name__ == '__main__':
    cfg_info = NewConfig()
    devices = cfg_info.get_info('vivox6')
    c, h = cfg_info.get_info("vivox6")
    print(c)
    print(h)
    a = 'a29316f8-16a5-4073-b784-ce206dcb92ea'
    mI = GetTaskInfo(c,h,a)
    a = mI.get_task_id("P90")
    print(a)
