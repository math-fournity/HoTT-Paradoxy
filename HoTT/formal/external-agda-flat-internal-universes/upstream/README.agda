{- 
Proofs of Theorems 3.1, 5.2 and Proposition 6.2 from 

Dan R. Licata, Ian Orton, Andrew M. Pitts and Bas Spitters, 
"Internal Universes in Models of Homotopy Type Theory"

in Proceedings of the 3rd International Conference on Formal
Structures for Computation and Deduction (FSCD 2018), Leibniz
International Proceedings in Informatics (LIPIcs), Vol. 108,
pp. 23:1-28:, 2018.

The proofs are carried out in agda-flat, an extension of Agda by
Andrea Vezzosi which implements the local type theory described in the
paper.

Installation instructions for agda-flat are in ~/code/agda-flat/install.txt
-}

{-# OPTIONS --without-K #-}

module README where

-- Proof of Theorem 3.1
open import theorem-3-1

-- Proof of Theorem 5.2
open import theorem-5-2

-- A version  of Theorem 5.2 relativized to an arbitrary universe
open import theorem-5-2-relative

-- Proof of Proposition 6.2
open import proposition-6-2
