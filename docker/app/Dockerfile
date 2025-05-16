FROM debian:12.6-slim AS build

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

COPY ./docker/app/.bashrc /root/
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
RUN /root/.rye/shims/rye sync --verbose --no-lock && mv .venv /root/

COPY --chmod=0755 <<-'EOF' /root/startup.sh
#!/bin/bash
if [ -d /root/.venv -a ! -f /root/app/.venv/rye-venv.json ]; then
    cp -pR /root/.venv /root/app/
fi
/root/.rye/shims/rye sync --no-lock
rm -f /run/gunicorn.pid
exec "$@"
EOF

FROM debian:12.6-slim
WORKDIR /root/app
COPY --from=build /root/.rye/ /root/.rye/
COPY --from=build /root/.venv/ /root/.venv/
COPY --from=build /root/.bashrc /root/.bashrc
COPY --from=build /root/startup.sh /root/
RUN --mount=type=cache,target=/var/lib/apt/lists \
  --mount=type=cache,target=/var/cache/apt/archives \
  apt update \
  && apt install -y \
  ca-certificates \
  inotify-tools \
  procps

CMD /root/startup.sh /root/.rye/shims/rye run gunicorn --bind 0.0.0.0:9000 app:app --reload --log-level debug --pid /run/gunicorn.pid
