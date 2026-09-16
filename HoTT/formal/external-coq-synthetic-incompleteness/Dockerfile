FROM coqorg/coq:8.15

RUN opam repo add opam-archive https://github.com/ocaml/opam-repository-archive.git --all-switches \
    && opam repo add coq-released https://coq.inria.fr/opam/released --all-switches \
    && opam update

RUN opam pin add -n -y -k git coq-metacoq-template.dev+8.15 \
      https://github.com/MetaCoq/metacoq.git#9493bb6 \
    && opam install -y \
      coq-equations.1.3+8.15 \
      coq-smpl \
      coq-metacoq-template.dev+8.15
