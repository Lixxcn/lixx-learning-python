from survey import AnonymousSurvey

question = "你的第一语言是什么？"
language_survey = AnonymousSurvey(question)

language_survey.show_question()

print("输入“q”结束\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    language_survey.store_response(response)

print("\n感谢每位参与问卷调查的人！")
language_survey.show_results()