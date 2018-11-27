import requests
import json
# prep-appwb.langlib.com
host = "https://appwb.langlib.com"
# host = "https://prep-appwb.langlib.com"

accesstoken = '7e77ca72-72e2-437c-9363-738f0a01f327'
headers = {
    'content-type': 'application/json',
    'appkey': 'WB_8AB3C7DA2F31',
    'appversion': '2017121201',
    'accesstoken': accesstoken,
    'Host': 'appwb.langlib.com',
    'Connection': 'Keep-Alive',
    'Accept-Encoding': 'gzip',
    'User-Agent': 'okhttp/3.6.0',
}


def get_all_word_books(host, headers):
    url = "{}/wordBooks/findUserWordBooks".format(host)
    response = requests.request("GET", url, headers=headers)
    answer = response.text
    json_data = json.loads(answer)
    return json_data.get("UserWordBookList")

def get_WordBook(all_books, WordBookName):
    for book in all_books:
        if WordBookName in list(book.values()):
            UserWordBookID = book.get("UserWordBookID")
            WordBookType = book.get("WordBookType")
            return UserWordBookID, WordBookType

def findAllTask(host, headers, UserWordBookID):
    url = "{}/wordBooks/{}/findTasks".format(host, UserWordBookID)
    response = requests.request("GET", url, headers=headers)
    answer = response.text
    json_data = json.loads(answer)
    # print(json_data.get("CurrentTask"))
    currentTask = []
    ct = json_data.get("CurrentTask")
    currentTask.append(str(ct.get("RoutineIdx")))
    all_new_task = []
    for unit in json_data.get("TaskInfos"):
        for task in unit:
            if task.get("R") == 0:
                all_new_task.append(task)
            # if task.get("C") == 0 and task.get("R") == 0:
            #     all_new_task.append(task)
            # if task.get("C") == 1:
            #     all_new_task.append(task)
            if task.get("R") != 0:
                task.update({'R': "00"})
                all_new_task.append(task)
    # print(len(all_new_task))
    # print(all_new_task)
    return all_new_task, currentTask

def get_words_info(host, headers, UserWordBookID, index):
    url = "{}/wordBooks/{}/findP1Words?unitIdx={}".format(host, UserWordBookID, index)
    try:
        headers.pop('Content-Length')
    except:
        pass
    # print(headers)
    response = requests.request("GET", url, headers=headers)
    answer = response.text
    # print(answer)
    json_data = json.loads(answer)
    # print(json_data)
    return json_data.get("WordInfos")

def put_words_to_3_star(host, headers, UserWordBookID, id):
    url = "{}/wordBooks/{}/updateFamiliarity".format(host, UserWordBookID)
    data = {"SysWordID": "{}".format(id), "Phase": 2, "OldFamiliarity": 1, "NewFamiliarity": 2}
    response = requests.request("PUT", url, headers=headers, json=data)
    return response

def post_6_done(host, headers, UserWordBookID, index, RID):
    url = "{}/wordBooks/{}/markTaskItemComplete".format(host, UserWordBookID)
    data = {"UnitIdx":int("{}".format(index)),"RoutineIdx":int("{}".format(int(RID)))}
    headers.update({'Content-Length': '71'})
    print("*" * 50)
    print(headers)
    print(data)
    response = requests.request("POST", url, headers=headers, json=(data))
    try:
        headers.pop('Content-Length')
    except:
        pass
    print("Done", response, response.status_code)
    return response.status_code


all_books = get_all_word_books(host, headers)
print(all_books)
UserWordBookID, WordBookType = get_WordBook(all_books, "四级高频 2000 词")
# print(UserWordBookID, WordBookType)
while True:
    all_new_task, current_task = findAllTask(host, headers, UserWordBookID)
    print("all_new_task", all_new_task)
    print("current_task", current_task)
    RID = "".join(current_task)
    Flag = 1
    while Flag:
        for new_task in all_new_task[:]:
            print("NewTask", new_task)
            index = new_task.get("U")
            if new_task.get("C") == 1:
                print("Begin to change to 3 stars", index)
                if new_task.get("R") == "00":
                    try:
                        status = post_6_done(host, headers, UserWordBookID, index, RID)
                        print("Status", status)
                        if status != 200:
                            Flag = 0
                    except:
                        pass
                try:
                    post_6_done(host, headers, UserWordBookID, index, RID)
                except:
                    pass
                ids = get_words_info(host, headers, UserWordBookID, index)
                for id in ids:
                    res = put_words_to_3_star(host, headers, UserWordBookID, id.get("Id"))
                    print(res)
            # index = new_task.get("U")
            if new_task.get("C") == 0:
                print("Begin to change to 3 stars", index)
                if new_task.get("R") == "00":
                    try:
                        status = post_6_done(host, headers, UserWordBookID, index, RID)
                        print("Status" , status)
                        if status != 200:
                            Flag = 0
                    except:
                        pass
                else:
                    ids = get_words_info(host,headers, UserWordBookID, index)
                    print("IDS", ids)
                    for id in ids:
                        res = put_words_to_3_star(host, headers, UserWordBookID, id.get("Id"))
                    try:
                        status = post_6_done(host, headers, UserWordBookID, index, RID)
                        if status != 200:
                            Flag = 0
                    except:
                        pass