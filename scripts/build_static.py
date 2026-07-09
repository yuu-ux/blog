from pathlib import Path
import shutil

from flask import Flask, render_template


APP_DIR = Path(__file__).resolve().parent.parent
PUBLIC_DIR = APP_DIR / "public"


def create_static_build_app():
    app = Flask(
        __name__,
        template_folder=str(APP_DIR / "templates"),
        static_folder=str(APP_DIR / "static"),
        static_url_path="/static",
    )

    app.add_url_rule("/", endpoint="root_bp.index", view_func=lambda: "")

    return app


def build_index_html():
    app = create_static_build_app()

    PUBLIC_DIR.mkdir(exist_ok=True)

    with app.test_request_context("/"):
        html = render_template("index.html")

    (PUBLIC_DIR / "index.html").write_text(html, encoding="utf-8")


def copy_static_files():
    src = APP_DIR / "static"
    dest = PUBLIC_DIR / "static"

    if dest.exists():
        shutil.rmtree(dest)

    if src.exists():
        shutil.copytree(src, dest)


def main():
    build_index_html()
    copy_static_files()
    print("Generated public/index.html")


if __name__ == "__main__":
    main()
