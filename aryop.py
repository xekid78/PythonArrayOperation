team = ["佐藤","鈴木","田中","岸田","有森"]
print(team)
print("チームは" + str(len(team)) + "人です。")
print()

print("*** 追加 ***")
team.append("田川")
print(team)
print("チームは" + str(len(team)) + "人です。")
print()

print("*** 変更 ***")
team[0] = "後藤"
print(team)
print("チームは" + str(len(team)) + "人です。")
print()

print("*** 削除 ***")
team.pop(2)
print(team)
print("チームは" + str(len(team)) + "人です。")
