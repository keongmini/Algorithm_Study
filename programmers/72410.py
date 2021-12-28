import re

def step2(id):
    # alphabet = [chr(i) for i in range(97, 123)]
    # alphabet.extend(['-', '_', '.'])
    # tmp_id = id
    # for i in id:
    #     if i not in alphabet:
    #         if not i.isdigit():
    #             tmp_id = tmp_id.replace(i,"")
    # return tmp_id
    tmp_id = ""
    for i in id:
        if i.isalnum() or i=="-" or i=="_" or i==".":
            tmp_id += i
    return tmp_id

def step4(id):
    for i in range(len(id)):
        if id[0] == '.':
            id = id[1:]
        elif id[-1] == '.':
            id = id[:-1]
        else:
            break
    return id
    # id_list = [i for i in id]
    # for i in id_list:
    #     if i == '.':
    #         id_list = id_list[1:]
    #     else:
    #         break
    # for i in range(len(id_list)-1,0, -1):
    #     if id_list[i] == '.':
    #         id_list = id_list[:-1]
    #     else:
    #         break
    # id = ''.join(id_list)
    # return id

def step7(id):
    for i in range(3):
        if len(id) == 3:
            return id
        else:
            id += id[-1]


def solution(new_id):
    new_id = new_id.lower()

    new_id = step2(new_id)

    new_id = re.sub(r'\.{2,}', '.', new_id)         # 정규표현식 확인 필요 / 다른 부분도 정규표현식으로 표현 가능
    # if '..' in new_id:
    #     new_id = new_id.replace('..', '.')

    new_id = step4(new_id)

    if not len(new_id):
        new_id += 'a'

    if len(new_id) > 15:
        new_id = new_id[:15]
        new_id = step4(new_id)

    if len(new_id) < 3:
        new_id = step7(new_id)

    return new_id

print(solution("...!@BaT#*..y.abcdefghijklm"))