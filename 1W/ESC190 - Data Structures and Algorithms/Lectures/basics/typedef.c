#include <stdio.h>
#include <stdlib.h>

// typedef to rename types

typedef float my_float;

// size_t is defined in stdlib
// an integer that stores a size of a block of memory

struct node{
    int data;
    struct node * next;
};

typedef struct node node;

// OR:
// typedef struct node{
//     int data;
//     struct node * next;
// } node;

int main(void)
{
    node n1;
    n1.data = 5;
    my_float pi = 3.14;
    const int a = 5; // a is of type const int - can't be changed
    // a = a + 2; // error
    //to get around it:
    // int * b = (int *)&a;
    // *b = 4;
    // printf("%d\n", a);

    int d = 5;
    const int * ptr_d = &d; //cannot change *ptr_d, but CAN change ptr_d
    int * const ptr_d1 = &d; // cannot change ptr_d1, CAN change *ptr_d1
    const int * const ptr_d2; // cannot change both ptr_d2 and *ptr_d2
}

