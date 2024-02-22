import pymysql.cursors
import configparser
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def init():
    # 設定ファイルのパス
    config_file = '../../settings.ini'

    # コンフィグパーサーの初期化
    config = configparser.ConfigParser()
    config.read(config_file)

    # コンフィグのルート
    db_config = config['LOCAL_DB']

    # データベース接続情報（開発用）
    connection = pymysql.connect(host=db_config['host'],
                                user=db_config['user'],
                                password=db_config['password'],
                                database=db_config['database'],
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
            # SQL実行
            sql = 'SELECT * FROM 楽天商品管理番号マスタ'
            cursor.execute(sql)

            # 結果の取得
            results = cursor.fetchall()

    finally:
        connection.close()
        return render_template('index.html', results=results)

if __name__ == '__main__' :
    app.run(debug=True)

