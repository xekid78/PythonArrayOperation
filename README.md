# PythonArrayOperation
配列操作

## 処理
配列の内容を追加、変更、削除を行います。

## コード
```
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
```

## 出力結果  
```
['佐藤', '鈴木', '田中', '岸田', '有森']
チームは5人です。

*** 追加 ***
['佐藤', '鈴木', '田中', '岸田', '有森', '田川']
チームは6人です。

*** 変更 ***
['後藤', '鈴木', '田中', '岸田', '有森', '田川']
チームは6人です。

*** 削除 ***
['後藤', '鈴木', '岸田', '有森', '田川']
チームは5人です。
```
  
## 開発環境
| 開発ツール |  |
|:-|:-|
| OS | Windows10 |
| 仮想化ソフト | Oracle VM VirtualBox 5.2 |
| 構築ソフト | Vagrant 2.0.2 |
| 仮想化上OS | CentOS 6.9 |
| SSHクライアント | PuTTY 0.6.8 |
| FTPクライアント | Cyberduck 6.3.5 |
| エディタ | Atom 1.24.0 |
| 開発言語 | Python 3.6.4 |
