FROM coqorg/coq:8.13.2@sha256:1f69b9224f068d408e6be7a3f536f67395d00c3497b97bdb99ee2d2c4c91954c

SHELL ["/bin/bash", "--login", "-c"]

RUN opam repository add opam-archive git+https://github.com/ocaml/opam-repository-archive.git \
    && opam update --repositories \
    && opam install -y \
       coq-equations.1.2.3+8.13 \
       coq-stdpp.1.5.0 \
    && opam clean -a -c -s --logs
