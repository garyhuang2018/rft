*** Settings ***
Suite Setup       打开应用
Library           OperatingSystem
Library           AppiumLibrary

*** Variables ***
${mobile}         M7BBB18A06151861

*** Test Cases ***
login
    Clear Text    id = com.gemvary.phone.cloudcall:id/login_et_phonenumber
    Input Text    id = com.gemvary.phone.cloudcall:id/login_et_phonenumber    13823199026
    Input Text    id = com.gemvary.phone.cloudcall:id/messageCode    66
    Click Text    登录

wall_swtich_control
    Click Element    xpath=//*[@content-desc='智能插座']

*** Keywords ***
打开应用
    Open Application    http://localhost:4723/wd/hub    platformName=Android    udid=${mobile}
