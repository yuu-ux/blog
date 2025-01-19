FROM debian:12.6-slim

RUN apt update \
  && apt install -y curl

# Rye のインストール
ENV RYE_VERSION="0.37.0"
ENV RYE_INSTALL_OPTION "--yes"
RUN curl -sSf https://rye.astral.sh/get | bash \
  && /root/.rye/shims/rye config --set-bool behavior.use-uv=true

# Python ライブラリのためのインストール
RUN apt update \
 && apt install -y python3-dev default-libmysqlclient-dev build-essential pkg-config clang

COPY ./docker/app/.bashrc /root
WORKDIR /root/app
EXPOSE 8001

# toolchainとapp用のバージョンを同一に固定する
ENV PATH="/root/.rye/shims:$PATH"
ENV PYTHON_VERSION="3.12.2"
RUN /root/.rye/shims/rye config --set behavior.toolchain="cpython@$PYTHON_VERSION" \
  && /root/.rye/shims/rye pin $PYTHON_VERSION

# ライブラリのインストール
COPY ./app/README.md ./app/pyproject.toml ./app/requirements*.lock /root/app
RUN mkdir -p /root/app/config
COPY ./app/config/gunicorn.conf.py /root/app/config
RUN /root/.rye/shims/rye sync --verbose --no-lock

CMD [ "/bin/bash", "-c", ". .venv/bin/activate && gunicorn -c /root/app/config/gunicorn.conf.py app:app" ]

