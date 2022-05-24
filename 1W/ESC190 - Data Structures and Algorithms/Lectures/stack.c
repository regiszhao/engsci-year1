#include <stdio.h>
#include <stdlib.h>

struct stack{
    int* data;
    int size;   //the size of the data block data
    int n;  // current number of elements on the stack
};

void create_stack(struct stack* stack){
    stack->size = 1;
    stack->data = (int *)malloc(stack->size * sizeof(int));
    stack->n = 0;
}

void push(struct stack* stack, int elem){
    if (stack->size == stack->n){
        stack->data = realloc(stack->data, stack->size*2*sizeof(int));
        stack->size *= 2;
    }
    stack->data[stack->n] = elem;
    stack->n++;
}

int pop(struct stack* stack){
    stack->n--;
    return stack->data[stack->n];
    // equivalently: return stack->data[--stack->n];
}

int main(void){
    struct stack s1;
    create_stack(&s1);
    printf("Size: %d,   n: %d\n", s1.size, s1.n);
    push(&s1, 1);
    printf("Size: %d,   n: %d\n", s1.size, s1.n);
    push(&s1, 2);
    printf("Size: %d,   n: %d\n", s1.size, s1.n);
    push(&s1, 3);
    printf("Size: %d,   n: %d\n", s1.size, s1.n);
    printf("%d %d %d\n", s1.data[0], s1.data[1], s1.data[2]);
    printf("%d\n", pop(&s1));
    printf("Size: %d,   n: %d\n", s1.size, s1.n);
}