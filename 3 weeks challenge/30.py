# query 로 들어오는 문자열의 경우는 세가지 뿐임
# 1. ???xx      ?가 앞쪽에
# 2. XX???      ?가 뒷쪽에
# 3. ?????      ?가 전체에

def solution(words, queries):
    head, head_rev = {}, {}  # 문자열 앞에서부터 트라이, 뒤에서부터 트라이
    lengths = []  # 문자열 길이 모두 저장

    def trie(head, word):  # 트라이구조로 문자열 연결관계 저장
        node = head
        for w in word:
            if w not in node:
                node[w] = {}

            node = node[w]

            if 'len' not in node:  # 문자열 길이 저장
                node['len'] = [len_word]
            else:
                node['len'].append(len_word)

        node['end'] = True  # 문자열 종료

    for word in words:
        len_word = len(word)
        trie(head, word)
        trie(head_rev, word[::-1])
        lengths.append(len_word)

    # ---------------------- words 문자열 연결 관계 저장 -----------------------

    def search(head, query):  # 문자열 탐색
        node = head
        for q in query:
            if q == '?':
                return node['len'].count(len_query)
            elif q not in node:
                break

            node = node[q]

        return 0

    result = []
    for query in queries:
        len_query = len(query)
        if query[0] == '?':
            if query[-1] == '?':  # query 전체가 ? 로 이루어져있는 경우
                result.append(lengths.count(len_query))
            else:  # 뒤에서부터 문자열 탐색
                result.append(search(head_rev, query[::-1]))
        else:  # 앞에서부터 문자열 탐색
            result.append(search(head, query))

    return result


# 참고. https://velog.io/@hope1213/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EA%B0%80%EC%82%AC%EA%B2%80%EC%83%89-%ED%8C%8C%EC%9D%B4%EC%8D%AC