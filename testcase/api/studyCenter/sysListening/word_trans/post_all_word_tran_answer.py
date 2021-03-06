import requests
import json
# from utils.logger import logger


class PostAllWordTransAnswers(object):
    def __init__(self, common, headers, accesstoken):
        self.headers = headers
        self.baseUrl = common.get('baseUrl')
        self.headers.update({'Content-Length': '90'})
        self.accesstoken = accesstoken
        self.headers.update({"accesstoken": self.accesstoken})
        self.headers.update({"Host": common.get("baseProxy")})

    def post_all_word_tran_answer(self, taskID, user_answer):
        url = "{}/userListening/{}/wordTransAnswers".format(self.baseUrl, taskID)
        data = user_answer
        response = requests.request("POST", url, headers=self.headers, json=data)
        answer = response.text
        # if answer.get("message") == "success".upper():
        #     logger.info("[PASS] == {},{}", taskID, user_answer)
        # if answer.get("message") != "success".upper():
        #     logger.info("[FAIL] == {},{}", taskID, user_answer)

    def put_word_tran_words(self, data):
        # print("====================",data)
        url = "{}/vocabularies/familiarity".format(self.baseUrl)
        response = requests.request("PUT", url, headers=self.headers, json=data)
        return response