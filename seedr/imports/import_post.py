from datetime import datetime
from setup_db import setup_db, AuditableColumns
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.mysql import INTEGER

app, db = setup_db()


class Category(AuditableColumns, db.Model):
    __tablename__ = "category"

    id: Mapped[int] = mapped_column(
        INTEGER(unsigned=True), primary_key=True, autoincrement=True
    )
    name: Mapped[str] = mapped_column(db.String(30), nullable=False, unique=True)


class Post(AuditableColumns, db.Model):
    __tablename__ = "post"

    id: Mapped[int] = mapped_column(
        INTEGER(unsigned=True), primary_key=True, autoincrement=True
    )
    title: Mapped[str] = mapped_column(db.String(100), nullable=False, default="無題")
    body: Mapped[str] = mapped_column(db.Text, nullable=True)
    published_at: Mapped[datetime] = mapped_column(db.DateTime(), nullable=True)
    is_draft: Mapped[bool] = mapped_column(db.Boolean, nullable=False, default=False)
    is_deleted: Mapped[bool] = mapped_column(db.Boolean, nullable=False, default=False)
    category_id: Mapped[int] = mapped_column(
        db.ForeignKey("category.id"), nullable=False
    )
    category: Mapped["Category"] = relationship("Category", backref="posts")


with app.app_context():
    # db.drop_all()
    db.create_all()

    if not db.session.get(Post, 1):
        post = [
            Post(
                title="PATH を通すとは",
                body="""
コマンド検索パスを追加すること
同じコマンドがあった場合初めに指定されているPATHのコマンドを採用するため、追加するコマンドを優先させたい場合は＄PATHの前に書く。
```c
export PATH=<追加したいPATH>:$PATH
export PATH=$PATH:<追加したいPATH>
```
参考：https://qiita.com/soarflat/items/09be6ab9cd91d366bf71
参考：https://qiita.com/soarflat/items/d5015bec37f8a8254380
                """,
                published_at=datetime.now(),
                is_draft=False,
                is_deleted=False,
                category_id=2,
            ),
            Post(
                title="シバン（#!/bin/bash）",
                body="""
カーネルに対して明示的に使用するインタプリタを示すもの。
インタプリタ言語でスクリプトを書く際は基本的に記述する。
例

```
#!/bin/bash
```
### インタプリタとは
翻訳者のようなもの。インタプリタはソースコードを1行ずつ翻訳し、翻訳が終わるごとに即座に実行される。
## シバンを記述することで
シバンを記述することで、スクリプトを直接実行できるようになる。
たとえば、
シバンあり

```perl
./test.pl # これで実行できる
```

```perl
#!/usr/bin/perl
use strict;
use warnings;
print "Hello World";
```

シバンなし

```perl
./test.pl # これだと実行できない
perl test.pl # コマンドでなんのインタプリタを指定するか指定してあげれば実行できる
```

```perl
use strict;
use warnings;

print "Hello World";
```

                """,
                published_at=datetime.now(),
                is_draft=False,
                is_deleted=False,
                category_id=1,
            ),
            Post(
                title="複合リテラルとは",
                body="""
一時的な無名変数を作れる。配列とか構造体でもできる。
計算結果とか直接渡したい時に便利

```c
#include <libc.h>

int main(int argc, char **argv)
{
    if (argc == 2)
    {
        char *s = argv[1];

        while (*s)
        {
            if (*s >= 'a' && *s <= 'z')
                write(1, &(char){'a' + (*s - 'a' + 13) % 26}, 1);
            else if (*s >= 'A' && *s <= 'Z')
                write(1, &(char){'A' + (*s - 'A' + 13) % 26}, 1);
            else
                write(1, s, 1);
        s++;
        }
    }
    write(1, "\n", 1);
}

```
参考：https://marycore.jp/prog/c-lang/compound-literal/
                """,
                published_at=datetime.now(),
                is_draft=False,
                is_deleted=False,
                category_id=2,
            ),
            Post(
                title="Goの文字列について",
                body="""
Goの文字列は不変で、`str1 += str2` のように文字列を連結した場合、str1とは別の領域に連結したテキストを新しく作成しているらしい。ただ、自分で検証してみると文字の連結はされているにも関わらず、アドレスは変わっていない。
→変数のアドレスは変更されないため。

```go
package main

import "fmt"

func main() {
    str1 := "Hello, "
    str2 := "World"
    fmt.Printf("%s %p\n", str1, &str1)
    str1 += str2
    fmt.Printf("%s %p\n", str1, &str1)
}
```

```go
Hello,  0xc000014070
Hello, World 0xc000014070
```

## 文字が新しく作成されていることを調べるためには
byte型の配列に変換してその文字自体のアドレスを確認する。文字列はポインタで参照するけど、文字であれば実データがあるため、それを確認することで確認できる

```go
package main

import "fmt"

func main() {
    str1 := "Hello"
    fmt.Printf("str1 address: %p\n", &str1)
    fmt.Printf("str1 data address: %p\n", []byte(str1))

    str1 += " World"
    fmt.Printf("str1 address after concatenation: %p\n", &str1)
    fmt.Printf("str1 data address after concatenation: %p\n", []byte(str1))
}
```

```go
str1 address: 0xc000014070
str1 data address: 0xc000012028
str1 address after concatenation: 0xc000014070
str1 data address after concatenation: 0xc000012070
```

## Goの文字列変数の扱いについて
C言語のポインタのように文字のアドレスをを持っている。
以下のような構造体で構成される

- 文字列データへのポインタ
- 文字数

```go
type stringStruct struct {
    str unsafe.Pointer
    len int
}
```

## 大規模な文字列の連結を行う場合
**`strings.Builder`**や**`bytes.Buffer`** が推奨されている
内部的な挙動としては、バッファをもって一度だけメモリ領域を確保し、新しく文字列を作成する。加算の場合だと呼び出されるたびに文字列が生成されるため、パフォーマンスが悪化する。

## range構文について
### 配列やスライス
基本的には0,1,2のようにインデックスは増加していく。たとえば、intの配列であれば普通に0, 1, 2のようにインデックスが増加していく。

### 文字列
文字列の場合のインデックスはその文字が開始するバイトオフセットを指す。これはエンコーディングの問題らしい。goではデフォルトでUTF-8でエンコーディングする。UTF-8は可変長エンコーディングという方式をとっており、1バイトから4バイトの範囲で適切なバイト数が割り振られ文字として認識される。
たとえば、日本語は3バイトのUTF-8を使用しているため、3バイトずつ増加していく。英語であれば、ASCII文字を使用しているため、1バイトで出力される。各言語を正しく処理できるようにしてくれてるっぽい。この機能がないと絵文字や日本語などさまざまな言語に対応できなくなる。

```go
package main

import "fmt"

func main() {
    str := "こんにちは"
    for i, r := range str {
        fmt.Printf("インデックス: %d, 文字: %c\n", i, r)
    }
}
```

```go
インデックス: 0, 文字: こ
インデックス: 3, 文字: ん
インデックス: 6, 文字: に
インデックス: 9, 文字: ち
インデックス: 12, 文字: は
```

```go
package main

import "fmt"

func main() {
    str := "hello"
    for i, r := range str {
        fmt.Printf("インデックス: %d, 文字: %c\n", i, r)
    }
}
```

```go
インデックス: 0, 文字: h
インデックス: 1, 文字: e
インデックス: 2, 文字: l
インデックス: 3, 文字: l
インデックス: 4, 文字: o
```

## バイトオフセットとは
バイトオフセットは、ある基準点（通常はデータ構造の開始点やメモリブロックの先頭）から、特定のデータまでのバイト数の距離を表します。この基準点からの距離が、それぞれのデータを一意に位置づけるために使われます。
「あ」がUTF-8でエンコードされる場合、実際には3バイトを使用します。もし「あ」が文字列の最初に来る場合、そのバイトオフセットは次のようになります：
- 「あ」の最初のバイトのオフセットは `0`
- 次の文字（「あ」の次に続く文字）の開始オフセットは `3`
したがって、「あ」が始まるオフセットは `0` であり、その長さは `3` バイトです。これが意味するのは、メモリ上で「あ」を表すデータは、オフセット `0` から `2`（0, 1, 2 の3バイト）までの位置を占めるということです。次の文字が開始されるのはオフセット `3` からとなります。
                """,
                published_at=datetime.now(),
                is_draft=False,
                is_deleted=False,
                category_id=2,
            ),
        ]
        db.session.add_all(post)
        db.session.commit()
        print("ポスト追加成功")
    else:
        print("すでにデータがあります")
