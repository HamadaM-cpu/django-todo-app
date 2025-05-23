# ToDoリストアプリ

このアプリケーションは、Djangoを使用して作成したシンプルな「今日のやることリスト」アプリです。ユーザーはタスクを追加、更新、削除、完了状態の切り替えができ、検索機能を使ってタスクを絞り込むこともできます。

## 機能

- タスクの追加、編集、削除
- タスクの完了状態の管理（完了・未完了の切り替え）
- タスクの検索
- タスクに締切日を設定
- タスクを完了した場合に視覚的に区別

## 技術スタック

- Python 3.x
- Django
- HTML/CSS (Bootstrap)

## インストール方法

1. **Pythonのインストール**  
   このプロジェクトを実行するために、Python 3.xが必要です。以下のリンクからインストールできます。  
   - [Python 公式サイト](https://www.python.org/downloads/)

2. **必要なパッケージのインストール**  
   プロジェクトディレクトリに移動し、`requirements.txt`を使って依存関係をインストールします。

   ```bash
   pip install -r requirements.txt
   ```

3. **データベースのマイグレーション**  
   データベースを設定し、マイグレーションを適用します。

   ```bash
   python manage.py migrate
   ```

4. **開発サーバーの起動**  
   アプリケーションを実行するには、以下のコマンドで開発サーバーを起動します。

   ```bash
   python manage.py runserver
   ```

   サーバーが立ち上がったら、ブラウザで `http://127.0.0.1:8000/` にアクセスしてアプリを利用できます。

## 使い方

- **新規タスク作成**  
  アプリのトップページから「＋ 新規作成」ボタンを押すと、タスクのタイトルと締切日を入力するフォームが表示されます。タスクを追加するとリストに表示されます。

- **タスクの完了状態を切り替え**  
  タスクの横にある「完了」ボタンを押すと、そのタスクの状態が「完了」に変わり、色が変わります。完了したタスクは「未完了」に戻すこともできます。

- **タスクの編集・削除**  
  各タスクには「詳細」、「編集」、「削除」のボタンがあり、タスクの詳細を確認したり、編集したり、削除することができます。

- **タスクの検索**  
  ページの上部にある検索ボックスを使って、特定のタスクをキーワードで絞り込むことができます。

## ディレクトリ構造

```
todo/
│
├── todo/
│   ├── migrations/
│   ├── models.py        # タスクのデータモデル
│   ├── views.py         # タスクの表示と操作を管理するビュー
│   ├── urls.py          # URLルーティング設定
│   ├── templates/
│   │   ├── todo/
│   │   │   ├── base.html  # 共通レイアウト（ヘッダーやフッターなど）
│   │   │   ├── list.html  # タスクのリスト表示ページ
│   │   │   ├── create.html  # 新規タスク作成ページ
│   │   │   ├── update.html  # タスク編集ページ
│   │   │   └── detail.html  # タスク詳細ページ
│   ├── forms.py         # タスク作成・更新フォーム
│   └── admin.py         # Django管理画面の設定
├── manage.py           # Djangoプロジェクト管理用のコマンド
└── requirements.txt     # 必要なパッケージの一覧
```




