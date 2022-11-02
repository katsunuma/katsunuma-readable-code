import json

#辞書データの読み込み
with open('./word_data.json') as f:
    dic_data = json.load(f)

#辞書データに登録されているidと単語をすべて出力
for word_data in dic_data:
    print(str(word_data["id"])+": " + word_data["word"])