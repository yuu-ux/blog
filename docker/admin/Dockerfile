FROM debian:12.5

RUN apt update \
    && apt install -y curl

ENV RYE_VERSION="0.37.0"
ENV RYE_INSTALL_OPTION "--yes"
RUN curl -sSf https://rye.astral.sh/get | bash \
    && /root/.rye/shims/rye config --set-bool behavior.use-uv=true

