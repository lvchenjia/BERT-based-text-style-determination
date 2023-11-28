import torch
from transformers import BertTokenizer, BertForSequenceClassification
import os

# 加载模型和分词器
path = os.getcwd()
model_path = os.path.join(path, "model")
test_file = os.path.join(path, "test.txt")

tokenizer = BertTokenizer.from_pretrained(model_path)
model = BertForSequenceClassification.from_pretrained(model_path)

# 准备数据
test_texts = []
with open(test_file, "r", encoding="utf-8") as file:
    test_texts = file.read().splitlines()

# 对测试数据进行编码
test_encodings = tokenizer(test_texts, truncation=True, padding='max_length', max_length=128, return_tensors='pt')

# 使用模型进行预测
model.eval()
with torch.no_grad():
    outputs = model(test_encodings['input_ids'], attention_mask=test_encodings['attention_mask'])
    logits = outputs.logits
    predictions = logits.argmax(dim=1).tolist()

# 将预测结果转化为文本标签
predicted_labels = ["三国演义" if label == 0 else "水浒传" for label in predictions]
# print("Predicted labels:", predicted_labels)
for i in len(predicted_labels):
    print(test_texts[i],predicted_labels[i])