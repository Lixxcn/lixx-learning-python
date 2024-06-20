import pytest
from survey import AnonymousSurvey

@pytest.fixture
def language_survey():
    """一个实例"""
    question = "你的第一语言是什么？"
    language_survey = AnonymousSurvey(question)
    return language_survey

def test_store_single_response(language_survey):
    """测试单个答案会被妥善地存储"""
    # question = "你的第一语言是什么？"
    # language_survey = AnonymousSurvey(question)
    language_survey.store_response('中文')
    assert '中文' in language_survey.responses

def test_store_three_responses(language_survey):
    """测试三个答案会被妥善的保存"""
    # question = "你的第一语言是什么？"
    # language_survey = AnonymousSurvey(question)
    responses = ['中文', '英语', '法语']
    for response in responses:
        language_survey.store_response(response)

    for response in responses:
        assert response in language_survey.responses