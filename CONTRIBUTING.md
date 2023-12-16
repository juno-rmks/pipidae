# Pipidae への貢献方法

Pipidae への貢献をご検討いただき、ありがとうございます。

## ローカル開発環境のセットアップ

Pipidae の開発には、次の製品が必要です。

- IDE
  - Microsoft Visual Studio Code (VSCode) 最新安定版
- プログラミング言語
  - Python 3.10 以降

### VSCode のセットアップ

VSCode へ次のエクステンションを追加します。

- エディタ統制
  - EditorConfig for VS Code (ID: EditorConfig.EditorConfig)
- オーサリング
  - Markdown All in One (ID: yzhang.markdown-all-in-one)
  - Markdown Preview Mermaid Support (ID: bierner.markdown-mermaid)
- Python 開発
  - Python (ID: ms-python.python)
    - Pylance (ID: ms-python.vscode-pylance)
  - Pylint (ID: ms-python.pylint)
  - Black Formatter (ID: ms-python.black-formatter)
  - isort (ID: ms-python.isort)
- その他
  - Even Better TOML (ID: tamasfe.even-better-toml)

### Python 仮想環境のセットアップ

Pipidae の開発用に Python 仮想環境を作成します。

```sh
python -m venv .venv
```

作成した Python 仮想環境をアクティベートします。

```sh
. .venv/bin/activate
```

アクティベートした Python 仮想環境の pip を最新バージョンへアップグレードします。

```sh
pip install --upgrade pip
```

Pipidae とその開発に必要な依存関係を Python 仮想環境へ編集可能モードでインストールします。

```sh
pip install -e .
pip install -e .[test]
pip install -e .[dev]
pip install -e .[docs]
```

開発では、セットアップした Python 仮想環境を使用します。

## ドキュメントの開発

Pipidae のドキュメントは `docs` フォルダ配下へ `sphinx-quickstart` を使用して、次の設定で初期構成しています。

```sh
> Separate source and build directories (y/n) [n]: y
> Project name: Pipidae
> Author name(s): Nobuyuki Sekimori
> Project release []: 0.0.0
> Project language [en]: ja
```

`docs` フォルダ配下の構造は、次の通りです。

```txt
docs
+-- source
|   +-- _static
|   +-- _templates
|   +-- api
|   +-- users-guide
|   |-- conf.py
|   \-- index.md
|-- make.bat
\-- Makefile
```

- source  
  ドキュメントのソースコードを格納するフォルダです。
- source/api  
  API リファレンスのソースコードを格納するフォルダです。
- source/users-guide  
  ユーザーズガイドのソースコードを格納するフォルダです。
- source/conf.py  
  Sphinx の構成ファイルです。
- source/index.md  
  ホームページのソースコードファイルです。
- make.bat  
  Windows OS でドキュメントをビルドする場合に使用するビルドスクリプトファイルです。
- Makefile  
  Linux や macOS でドキュメントをビルドする場合に使用する Makefile です。

`src` フォルダ配下の構造や Python ソースコード内の docstring を変更した場合、API リファレンスも必ず再生成します。

> [!IMPORTANT]
> API リファレンスは `autodoc` で自動生成するため、`docs/source/api` フォルダ配下のファイルは絶対に手動で変更しないでください。

```sh
sphinx-apidoc -f -T -e -M -o docs/source/api src
```

ドキュメントを変更したら、ローカルで再ビルドし、ウェブブラウザで表示を確認します。

```sh
cd docs
make clean html
```

ドキュメントは Read the Docs サービスを使用して公開しています。
