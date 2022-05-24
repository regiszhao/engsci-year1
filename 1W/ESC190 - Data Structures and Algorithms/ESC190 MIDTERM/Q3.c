/*
PART A
2 DFS traversals:
1) A->B->C->D->F->G
2) A->B->D->F->G->C

2 BFS traversals:
1) G->F->D->B->A->C
2) G->F->D->B->C->A


PART B
There can be more than 1 depth-first traversal since at B, the graph branches off to 2 possible paths, which means that one traversal can go deep into one path first, while another traversal can go deep into the other path first.
 */