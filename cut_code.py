if practiceType == 14:
    st = AllReadInterface(common, headers, access_token)
    all_answer = st.get_all_sec_train_answer(groupID, taskID)
    print("all_answer", all_answer)
    for a in all_answer:
        if "newF" in list(a.keys()):
            stars_3 = st.get_sec_train_words(groupID, taskID, practiceType)
            for star in stars_3:
                ne_re = st.put_sec_train_words(star)
            st_data = st.get_sec_train_word_done_data(groupID, taskID, practiceType)
            re = st.put_sec_train_words_done(taskID, st_data)
        else:
            st.post_all_sec_train_answer(taskID, a)