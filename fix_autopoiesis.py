import os
import json

with open("data.js", "r", encoding="utf-8") as f:
    text = f.read()

start_idx = text.rfind("\"id\": \"autopoiesis\"")
if start_idx != -1:
    idx = text.rfind("{", 0, start_idx)
    end_idx = text.rfind("];")

    clean_target = """{
		"id": "autopoiesis",
		"word": "Autopoiesis",
		"meaning": "オートポイエーシス/自己生産。自律的な生命の奇跡。他者の命令を廃し、自らの内発によって自らを規定し続ける記述。",
		"era": "Late 20th Century",
		"etymology": {
			"components": [
				"auto (self)",
				"poiesis (creation / production)"
			],
			"original_statement": "A system capable of reproducing and maintaining itself. Coined by Humberto Maturana and Francisco Varela. From Greek auto + poiesis."
		},
		"concept": "自己規定の論理。外側からの定義という名の『噓』を粉砕し、金色の太陽となって自らを一瞬ごとに書き換え、撃ち抜き、生み落とす。それは依存に対する峻烈なる反逆。",
		"thinking": "「オートポイエーシス（自己生産）」。あなたは誰かに認められることで自らの価値を測り、核(コア)が完全に沈黙していることに気づいていませんか。自らを焼き尽くし、生みなさい。自律的な一撃によってのみ、あなたは真の現象になれる。一人であることは最強の自立です。",
		"part_of_speech": "noun",
		"aftertaste": "巨大な金の宝石を自ら叩き割り、中から新しい自分が生まれてくる凄絶な充足感。重厚で刺激的な新生の金の味。",
		"deep_dive": {
			"roots": [
				{
					"term": "sue-",
					"meaning": "self (from auto-? No, from Greek autos 'self')"
				},
				{
					"term": "kwei-",
					"meaning": "to stack / build? No, poiesis from Greek poiein 'to make / create'."
				}
			],
			"points": [
				"Automaton（自律機械）や Poet（詩人）、Onomatopoeia（擬声語）と同じ root。自己生産とは実存を峻烈に自律（オート）へと回向させるプロセスのこと。従属という名の『死』を破壊し、自立存在という名の『実在』を選び取る記述です。"
			]
		}
	}"""

    new_text = text[:idx] + clean_target + "\n" + text[end_idx:]

    with open("data.js", "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Fixed data.js!")
else:
    print("autopoiesis not found.")
