import pickle #(객체, 텍스트) 직렬화, 역직렬화

# 파일 이름과 데이터
bfileName = 'D:/Atom WorkSpace/section4/test.bin'
tfileName = 'D:/Atom WorkSpace/section4/test.txt'

data1 = 77
data2 = "Hello, World!"
data3 = ["car", "apple", "house"]

with open(bfileName, 'wb') as f :
    pickle.dump(data1,f) #dumps(문자열 직렬화)
    pickle.dump(data2,f)
    pickle.dump(data3,f)

#텍스트 쓰기
with open(tfileName, 'wt') as f :
    f.write(str(data1))
    f.write('\n')
    f.write(data2)
    f.write('\n')
    f.writelines('\n'.join(data3))

#바이너리 읽기
with open(bfileName, 'rb') as f:
    b = pickle.load(f) #Loads(문자열 역직렬화)
    print(type(b), 'Binary Read1 | ' , b)
    b = pickle.load(f)
    print(type(b), 'Binary Road2 | ', b)
    b = pickle.load(f)
    print(type(b), 'Binary Road3 | ', b)

# 택스트 읽기
with open(tfileName, 'rt') as f :
    for i, line in enumerate(f,1) :
        print(type(line), 'Text Read' + str(i) + ' | ', line, end='')
