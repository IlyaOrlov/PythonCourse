# Файл test_copy_file.robot

*** Settings ***
Documentation  Check file actions

Library        OperatingSystem

Test Setup     On Test Setup
Test Teardown  On Test Teardown


*** Variables ***
${copy_script}  python ./copy_file_task.py
${src_file}     ./source.txt
${dst_file}     ./destination.txt
${exp_content}  hello


*** Keywords ***
On Test Setup
    Create File  ${src_file}  ${exp_content}
    File Should Exist  ${src_file}

On Test Teardown
    Remove File  ${src_file}
    Remove File  ${dst_file}


*** Test Cases ***
Test File Copy
    [Documentation]  Test file copy script
    [Tags]    DEBUG
    File Should Not Exist  ${dst_file}
    Run  ${copy_script}
    File Should Exist  ${dst_file}
    ${content}=  Get File  ${dst_file}
    Should Be True	'${content}' == '${exp_content}'
