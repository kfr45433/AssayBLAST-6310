# AssayBLAST-6310
Reproduction of the key features of AssayBLAST for BINF6310 at NEU
## What is this repo for?
This repo contains "starter" code that demonstrates how global and local alignment will work. Therefore, you can expect .py files (a couple) implementing this algorithm (no external packages needed), and another "master" file (or two) for orchestrating input .fasta file acceptance, traversal, and processing to return an alignment result. You can then use this code as you wish when implementing this on your own. We can also include key aspects like finding the melting point from GC content or tagging off-site alignment (like a primer that binds to multiple sites you identify).
## This repo will be organized with the following directories:
AssayBLAST-6310\
  / README.md\
  / .gitignore (in Python since it's the main language we'll be using)\
  src\
    / ---> main code goes here\
  / data\
    / ---> user input data/accompanying files go here for now (once I create a database this will change)\
  / output\
    / ---> output files from the algorithm implementation go here.\
## Things to do before you start coding
Please research + attempt global alignment (Needleman-Wunsch) before attempting local alignment (BLAST). The latter builds on the former and the algorithm itself is not intuitive. For this, you need to be familiar with: 
(A) grid traversal (or row/column operations),\
(B) File I/O,\
(C) mutating arrays (or arrays of arrays, or lists of lists in Python).\
Brush up on these first before trying to understand the algorithm itself.\
Tomorrow I will commit a rough (very rough) implementation of the global alignment algorithm in Python once I've finished implementing it in C++ tonight (so I can see how well it would work). We can also meet virtually to go over how the algorithm itself works, I wouldn't mind doing a demo. Afterwards I will also post a rough attempt at local alignment (close to what BLAST uses!) You can choose to scale it however you'd like.
## Other notes
The TA has notified us that we can try implementing this ourselves, and then present the results after. This repo will contain the global alignment + local alignment (maybe) algorithm you can modify yourself later during the semester for this assignment. This repo will also demonstrate/test how generating output and reading input files would work from different directories (we can even try web-crawling).
<b>IMPORTANT</b> Github WILL SUBMIT ANY AND ALL CODE YOU UPLOAD HERE FOR TRAINING COPILOT. Regardless of what you think I believe you should be aware and able to opt-in and out if necessary. By default, Github assumes your consent. If you'd like to keep your data (and this repo) private, go to settings > copilot > scroll to the bottom, and disable the appropriate features.
The interface (contract) of the algorithm itself and a rough manpage will be added here in the next week or so I take to implement it. If you have any questions let me know!!
