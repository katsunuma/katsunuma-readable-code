import json

#辞書データの読み込み
with open('./word_data.json') as f:
    dic_data = json.load(f)

#単語idを指定して出力
print(dic_data[0]["word"])