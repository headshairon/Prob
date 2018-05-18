# パズドラのガチャ確率計算機
## 作者の戯言
<p>2018年、パズドラでは魔法石を消費するガチャに対する確率が表示されるようになりました。しかし、たくさんガチャをした場合の確率はあまり見ないのではないか...と思いまして、確率を計算するコードを作ってしまいました。~~作者は暇人ですね(殴~~<br>　このコードはPythonを用いて記述されています。作者はPython初体験かつプログラミングスキルがまだまだなので、変な書き方・アルゴリズムがあるかもしれないです（笑）。「こっちの方が速い」「もっと単純に書ける」「もっと正確に計算できる」「機能追加してみた」ということがありましたら、ガンガンプルリクエストをお願いします！</p>

## 機能の説明
<p>今回は2つのコードを用意しましたが、それぞれ独立した別物です。 </p>
- prob.py
- 次の数を指定することで、コマンドプロンプト上に確率を表示します。
  - ガチャの回数 n
  - 最低限何体引きたいか ( r )
  - 確率 p (%)
  - リストの行数 d
    - 最後に登場するdの値を指定することで、およそ(n / d)回ごとに、暫定の確率を表示します。
<br><br>
- prob2.py
- 次の数を指定することで、コマンドプロンプト上に確率を表示します。1セットごとに暫定の確率が表示されます。
  - ガチャのセット数 n
    - 5000円分17回を1セットとして何セット分回すかを指定します。
  - 最低限何体引きたいか ( r )
  - 確率 p (%)

## ご注意
- このコードは**確率の精度について何ら保証もしません**。あくまでご参考程度にお願いします！
- ガチャにかかる費用について
  - 5000円で魔法石が85個が最安値ですので、その価格を前提として計算しています。
- 確率表示について
  - 確率がえげつなく低い場合、カッコ内に表示されている確率が0％になります。その場合は左側の指数表記を利用ください。
  - ここでの「確率が100％である」とは、**「ほとんど100％に近い確率」のことであって、必ず引けるという意味ではありません。**
- 重ねてのお願いですが、確率の精度を上げられる書き方をご存知でしたら、プルリクエストをしていただけると幸いです！

## 環境について
- PCのコマンドライン上で動きます。
- 実行するには [**Python3**](https://www.python.org/) をインストールしてください。
  - 参考：[Pythonインストールと環境設定 - PythonWeb](https://www.pythonweb.jp/tutorial/install/)

## 利用方法
1. ページ右側にある"Clone or download"より zip ファイルとしてダウンロードし、解凍してください。
2. コマンドプロンプトを呼び出し、ダウンロードしたファイルのディレクトリまで移動します。
  - 参考：[Windowsのコマンドプロンプトでディレクトリを移動する方法](https://tonari-it.com/windows-cmd-cd/)
  - 参考：[コマンドプロンプトでCドライブからDドライブへ移動 – webdev](http://webdev.jp.net/cmd-cd-drive/)
3. 次のどちらかのコマンドを選んで実行してください。
 - py prob.py
 - py prob2.py

### リリースノート【prob.py】
- 2018/05/18 : Ver.1.0 : prob.py リリース

### リリースノート【prob2.py】
- 2018/05/18 : Ver.1.0 : prob2.py リリース

連絡先：[@headshairon_pad](https://twitter.com/headshairon_pad)

<style>
p{
  text-indent: 1em;
}
</style>
