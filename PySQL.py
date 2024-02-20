import pymysql.cursors

# データベース接続情報
# connection = pymysql.connect(host='mysql301.phy.lolipop.lan',
#                              user='LAA1042641',
#                              password='sashi3371',
#                              database='LAA1042641-application',
#                              charset='utf8mb4',
#                              cursorclass=pymysql.cursors.DictCursor)

# データベース接続情報（開発用）
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             database='development_main',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


try:
    with connection.cursor() as cursor:
        # SQL実行
        sql = 'SELECT * FROM 楽天商品管理番号マスタ'
        cursor.execute(sql)

        # 結果の取得
        result = cursor.fetchall()
        for row in result:
            print(row['manageID'])

finally:
    connection.close()

