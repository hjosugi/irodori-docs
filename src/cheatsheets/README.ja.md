<!-- i18n: language-switcher -->
[English](README.md) | [日本語](README.ja.md)

# エンジンのチートシート

1ページごとにデータベースの概要を素早く回答：**Irodoriからの接続方法は？、クエリモデルは？、そしてエンジンごとの癖は何か？** これらは、より深い `docs/engine-syntax-reference.md`（ドライバー/デコードの内部）や `docs/data-source-support-status.md`（サポート状況）の人間向け、コピー＆ペースト可能な補助資料です。

各チートシートは、`irodori-table`内のローカル知識入力（`knowledge/cheatsheets/*.json`と知識DB）から**自動生成**されることを意図しています。ページが生成されるまで、手動で種をまき`<!-- seed -->`とマークすることも可能です。生成管理とドリフトルールは[`repository-boundaries.md`](../repository-boundaries.md)に記録されています。

## 目次

| チートシート | 対応エンジン | 状況 |
|---|---|---|
| [neo4j.md](neo4j.md) | Neo4j（グラフ、Bolt/Cypher）；Memgraphのメモ | 種まき（フラッグシップ） |
| [postgres.md](postgres.md) | PostgreSQL（+ Cockroach/Yugabyte/Redshift/Timescale/Neon） | 生成済み（`knowledge/cheatsheets/postgres.json`） |
| [questdb.md](questdb.md) | QuestDB（Postgresワイヤ＋時系列SQL拡張） | 種まき |
| _mysql.md_ | MySQL / MariaDB / TiDB | 計画中 |
| _sqlite.md_ | SQLite | 計画中 |
| _sqlserver.md_ | SQL Server | 計画中 |
| _duckdb.md_ | DuckDB | 計画中 |
| _mongodb.md_ | MongoDB | 計画中 |

新しいチートシートは、`docs/data-source-support-status.md`で少なくとも**Wired**と認定されたエンジンのみ追加されます。「認識済み、コネクタなし」や「未登録」のエンジンは、実際に接続できるようになるまでサポートステータスドキュメントに行が追加されるだけです。

## ページのフォーマット（各チートシートのテンプレート）

この順序を守ることで、生成ツールが決定論的にページを作成でき、読者も習慣化しやすくなります。

1. **概要** — ワイヤ/ドライバー、デフォルトポート、クエリ言語、Irodoriのサポート状況、そして「このエンジンの特徴は何か？」を一行で。
2. **接続** — Irodoriの接続フィールドと*生のURL/DSN形式*、最小限の動作例。
3. **クエリモデル** — 入力する内容、返ってくる内容、行制限の挙動。
4. **基本的なステートメント** — 80％のケースに対応できる、コンパクトで実行可能なクエリセット。
5. **オブジェクトの一覧表示** — Irodoriのオブジェクトブラウザのようにオブジェクトをリストアップする方法。
6. **Irodori固有の挙動** — このアプリ特有のマッピングや癖（デコード、オブジェクトブラウザのマッピング、未実装部分）。
7. **注意点** — 実際に人を困らせる小さなポイント。
8. **ソース** — このページが生成された`knowledge/sources.json`のID。

**Sources**フッターは重要で、各ページを公式ドキュメントに紐付け、ページの鮮度を確認できる仕組みになっています。