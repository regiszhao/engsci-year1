#include <stdio.h>
#include <stdlib.h>

typedef struct node{
    int data;
    struct node *next;
    struct node *prev;
} node;


void print_list(node *head){
    while (head->next != NULL){
        printf("%d, ", head->data);
        head = head->next;
    }
    printf("%d, ", head->data);
    return;
}

