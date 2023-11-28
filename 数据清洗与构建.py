import re
import os
cur_path = os.getcwd()
# 从文件中读取文本
input_file_path = '3.txt'
output_file_path = 'c.txt'

# 三国演义 测试数据为44-48回
# 水浒传 测试

input_file_path = os.path.join(cur_path, input_file_path)
output_file_path = os.path.join(cur_path, output_file_path)

with open(input_file_path, 'r', encoding='utf-8') as file:
    text = file.read()

# 划分为句子
sentences = re.split(r'(?<=[。！？])', text)

# 去除标点符号
sentences = [re.sub(r'[，：‘’“”；。、？！\n]', '', sentence) for sentence in sentences if sentence.strip() != '']

# 将处理后的结果写入文件
with open(output_file_path, 'w', encoding='utf-8') as file:
    for sentence in sentences:
        if len(sentence)>4:
            file.write(sentence + '\n')