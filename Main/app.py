# Flaskフレームワークと必要なモジュールをインポート
from flask import Flask, render_template, request
from datetime import datetime

# Flaskアプリケーションの作成
app = Flask(__name__)

# 投稿を格納するリスト
posts = []

# ルートパスへのGETとPOSTメソッドの処理を行う関数
@app.route('/', methods=['GET', 'POST'])
def index():
    # POSTメソッドでリクエストが送られた場合
    if request.method == 'POST':
        # フォームに'delete_post'が含まれていれば、投稿を削除
        if 'delete_post' in request.form:
            delete_index = int(request.form['delete_post'])
            delete_post(delete_index)
        else:
            # フォームから受け取った投稿内容を取得
            post_content = request.form['post_content']
            # 投稿内容が空でない場合、新しい投稿を追加
            if post_content.strip():
                posts.insert(0, {'content': post_content, 'timestamp': format_datetime()})
    
    # index.htmlテンプレートにpostsの内容を渡してレンダリング
    return render_template('index.html', posts=posts)

# 日時をフォーマットする関数
def format_datetime():
    now = datetime.now()
    return now.strftime("%Y/%m/%d %H:%M")

# 指定されたインデックスの投稿を削除する関数
def delete_post(index):
    if 0 <= index < len(posts):
        del posts[index]

# アプリケーションを実行
if __name__ == '__main__':
    app.run(debug=True)

