FROM debian:12.5

RUN apt update \
    && apt install -y curl


ENV RYE_VERSION="0.37.0"
ENV RYE_INSTALL_OPTION "--yes"
RUN curl -sSf https://rye.astral.sh/get | bash \
    && /root/.rye/shims/rye config --set-bool behavior.use-uv=true

RUN apt update \
    && apt install -y build-essential libssl-dev libffi-dev python3-dev default-libmysqlclient-dev pkg-config

ENV PATH="/root/.rye/shims:$PATH"
ENV PYTHON_VERSION="3.12.2"
RUN /root/.rye/shims/rye config --set behavior.toolchain="cpython@$PYTHON_VERSION" \
  && /root/.rye/shims/rye pin $PYTHON_VERSION

WORKDIR /root/admin
COPY ./admin/README.md ./admin/pyproject.toml ./admin/requirements*.lock /root/admin
RUN mkdir -p /root/admin/config
COPY ./admin/config/gunicorn.conf.py /root/admin/config

CMD /root/.rye/shims/rye sync --verbose --no-lock \
    && /root/.rye/shims/rye run gunicorn --bind 0.0.0.0:9001 admin:app --reload --log-level debug --pid /run/gunicorn.pid
