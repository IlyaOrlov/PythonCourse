*** Settings ***
Documentation       Test google search
Library             SeleniumLibrary


*** Test Cases ***
Test Google Search
    Open Browser	http://www.google.com	chrome
    Input Text	name=q	Cheese!
    Submit Form
    Wait Until Keyword Succeeds  10s  2s
    ...  Title Should Be  Cheese! - Поиск в Google
