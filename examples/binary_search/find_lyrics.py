import re

words = ['frodo','front','frost','frozen','frame','kakao'] # 가사집
words.sort()
queries = ['fro??','????o','fr???','fro???','pro?']# 쿼리
queries_len = [len(i) for i in queries] # 각 쿼리의 길이
result =[0]*len(queries) # 쿼리별로 몇개있는지 정리하는 리스트

for i in range(len(queries)):
    queries[i] = queries[i].replace('?','[a-z]') # 쿼리를 정규식 패턴으로 바꾼다

for i in range(len(queries)):
    p = re.compile(queries[i])
    for word in words:
        m = p.search(word)
        if len(word) == queries_len[i] and  m != None:
            result[i] +=1
print(result)