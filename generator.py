from memory_profiler import memory_usage # 計算記憶體用量
import time # 計算程式耗時

# # 普通讀檔案
# def readfile():
#     data = []
#     with open('reviews.txt', 'r') as f:
#         for line in f:
#             data.append(line.strip())
#     return data

# # 用generator
# def readfile_gen():
#     with open('reviews.txt', 'r') as f:
#         for line in f:
#             yield line
#     return line


# data = readfile()
# print(data[3])

# data_gen = readfile_gen()
# print(next(data_gen))
# print(next(data_gen))
# print(next(data_gen))



print(f'初始記憶體用量為: {memory_usage()} MB')
start = time.time()
# list comprehension (清單快寫法)
data = [line.strip() for line in open('reviews.txt')]
count = 0
leng = 0
for i in data:
    leng += len(i)
    count += 1
print(f'共有 {count} 筆留言,平均長度為 {leng / count} 個字')
end = time.time()
print(f'執行總耗時 {end - start} 秒')
print(f'記憶體用量為: {memory_usage()} MB')

# 初始記憶體用量為: [22.15234375] MB
# 共有 1000000 筆留言,平均長度為 365.84584 個字
# 執行總耗時 1.4837939739227295 秒
# 記憶體用量為: [445.84765625] MB



print(f'初始記憶體用量為: {memory_usage()} MB')
start = time.time()
# generator expression (generator快寫法)
data = (line.strip() for line in open('reviews.txt'))
count = 0
leng = 0
for i in data:
    leng += len(i)
    count += 1
print(f'共有 {count} 筆留言,平均長度為 {leng / count} 個字')
end = time.time()
print(f'執行總耗時 {end - start} 秒')
print(f'記憶體用量為: {memory_usage()} MB')

# 初始記憶體用量為: [22.09765625] MB
# 共有 1000000 筆留言,平均長度為 366.84585 個字
# 執行總耗時 1.1762585639953613 秒
# 記憶體用量為: [22.44921875] MB


