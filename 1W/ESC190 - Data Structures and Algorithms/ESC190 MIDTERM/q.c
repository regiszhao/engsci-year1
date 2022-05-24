#include <stdio.h>
#include <stdlib.h>

typedef struct node{
    int data;
    struct node *next;
} node;

typedef struct queue{
    node *head;
    node *tail;
} queue;

void create_q(queue *q){
    q->head = NULL;
    q->tail = NULL;
}

void enqueue(queue *q, int data){
    //create new node
    node *new_node = (node *)malloc(sizeof(node));
    new_node->data = data;
    new_node->next = NULL;

    //if queue is empty, change head to new node
    if (q->head == NULL){
        q->head = new_node;
    }

    //as long as queue's tail isn't NULL, make the tail node point to new node
    if (q->tail != NULL){
        q->tail->next = new_node;
    }
    q->tail = new_node; //change tail to new node
    return;
}

int dequeue(queue *q){
    //if queue is empty, return NULL
    if (q->head == NULL){
        return NULL;
    }

    int first_elem = q->head->data;

    //move head back to the next node
    q->head = q->head->next;
    //if there's no next node, set head and tail to NULL
    if (q->head == NULL){
        q->tail = NULL;
    }

    return first_elem;
}