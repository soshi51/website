IDL Support Status (2013 Jan.)
------------------------------

現在、Jubatus は 6 種類の機械学習タスク (Classifier, Regression, Recommender, Stat, Graph, Anomaly) をサポートしています。
:ref:`how_to_get_clients-ja` で紹介している通り、クライアントコードは、 msgpack-idlで生成されています。
以下はそのサポート状況です。

+------------+------------+-------------+--------------+--------------+--------------+--------------+
|            | Classifier | Regression  | Recommender  | Stat         | Graph        | Anomaly      |
+------------+------------+-------------+--------------+--------------+--------------+--------------+
| C++        | ok         | ok          | ok           | ok           | ok           | ok           |
+------------+------------+-------------+--------------+--------------+--------------+--------------+
| Java       | needs fix  | needs fix   | needs fix    | needs fix    | needs fix    | needs fix    |
+------------+------------+-------------+--------------+--------------+--------------+--------------+
| Python     | ok         | ok          |  ok          | ok           | ok           | ok           |
+------------+------------+-------------+--------------+--------------+--------------+--------------+
| Ruby       | ok         | ok          |  ok          | ok           | needs fix    | ok           |
+------------+------------+-------------+--------------+--------------+--------------+--------------+

- ok：生成したそのままを利用できます。

- needs fix：自動生成したコードから少し変更が必要です。

以下の環境でテストを行なっています。

- Jubatus : Jubatus 0.4.0

- Server : 上記レポジトリで生成されたサーバ

- Client : IDLによって生成されたコード

- IDL : 上記レポジトリのIDLファイル
