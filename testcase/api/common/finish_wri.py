import multiprocessing
from testcase.api.login.login_all_api import LoginApi
from utils.config import NewConfig
from testcase.api.studyCenter.getServiceInfo_step1 import GetServiceInfo
from testcase.api.studyCenter.getTaskInfo_step2 import GetTaskInfo
from testcase.api.studyCenter.startLearning_step3 import StartLearning
from testcase.api.studyCenter.getTaskInfo_step4 import GetTaskInfo2

from testcase.api.studyCenter.words_lists.all_cihui import AllCihuiInterface
from testcase.api.studyCenter.sysListening.all_listening_interface import AllListenInterface
from testcase.api.studyCenter       .reading.all_reading_interface import AllReadInterface
from testcase.api.studyCenter.grammar.all_gra_interface import AllGraInterface
from testcase.api.studyCenter.writing.all_wrt_interface import AllWrtInterface


def finish_wri(task, common, headers, access_token):
    if task.get('currStatus') == 0 or task.get('currStatus') == 1:
        practiceType = task.get("practiceType")
        currStatus = task.get("currStatus")
        taskID = task.get("taskID")
        groupID = task.get("groupID")
        if currStatus == 0:
            if practiceType == 9:
                # print(practiceType, currStatus, taskID, groupID)
                word_spell = AllWrtInterface(common, headers, access_token)
                word_spell_answers = word_spell.get_all_word_spell_answer(groupID, taskID)
                for answer in word_spell_answers:
                    post_word_spell_answer = word_spell.post_all_word_spell_answer(taskID, answer)
                word_spell_words = word_spell.get_word_spell_words(groupID, taskID, practiceType)
                ws_words = word_spell.get_word_spell_words(groupID, taskID, practiceType)
                for star in ws_words:
                    r = word_spell.put_word_spell_words(star)
            if practiceType == 12:
                print("真题写作")
                zhenti_xiezuo = AllWrtInterface(common, headers, access_token)
                zhenti_xiezuo_answers = zhenti_xiezuo.get_all_zhenti_xiezuo_answer(groupID, taskID)
                for answer in zhenti_xiezuo_answers:
                    print("Answer", answer)
                    post_word_spell_answer = zhenti_xiezuo.post_all_zhenti_xiezuo_answer(taskID, answer)
        if currStatus == 1:
            word_lists_to_3start = AllWrtInterface(common, headers, access_token)
            if practiceType == 9:
                word_spell_words = word_lists_to_3start.get_word_spell_words(groupID, taskID,
                                                                             practiceType)
                ws_words = word_lists_to_3start.get_word_spell_words(groupID, taskID, practiceType)
                for star in ws_words:
                    if star.get("oldF") == 3:
                        pass
                    else:
                        word_lists_to_3start.put_word_spell_words(star)