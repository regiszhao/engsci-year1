#include <stdio.h>
#include <stdlib.h>

typedef struct stack{
    int *data; //list of data
    int size; //size of allocated data block
    int num_elem; //number of elements in stack
} stack;

void create_stack(stack *stack){
    stack->num_elem = 0;
    stack->size = 1;
    stack->data = (int *)malloc((stack->size) * sizeof(int));
}

void push(stack *stack, int data){
    if (stack->num_elem == stack->size){
        stack->data = realloc(stack->data, (stack->size)*2*sizeof(int));
        stack->size *= 2;
    }
    stack->data[stack->num_elem] = data;
    stack->num_elem++;
    return;
}

int pop(stack *stack){
    stack->num_elem--;
    return stack->data[stack->num_elem];
}
