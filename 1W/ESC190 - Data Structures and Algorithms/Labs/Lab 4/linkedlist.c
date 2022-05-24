#include <stdio.h>
#include <stdlib.h>
#include "linkedlist.h"

void print_list(node * head){
    while (head->next != NULL){
        printf("%d, ", head->data);
        head = head->next;
    }
    printf("%d", head->data);
    return;
}

node * create_node(int data, node * next){
    node * new_node = (node *)malloc(sizeof(node));
    new_node->data = data;
    new_node->next = next;
    return new_node;
}

void append_node(node * head, int data) {
    while (head->next != NULL){
        head = head->next;
    } //cur->next is now equal to NULL
    head->next = create_node(data, NULL);
}

void insert_node(node * head, int index, int data){
    for (int i = 0; i < (index-1); i++){
        head = head->next;
    }
    node * prev_node = head;
    node * next_node = head->next;
    prev_node->next = create_node(data, next_node);
}

void delete_node(node * head, int data){
    node * prev_node;
    while (head->data != data){
        prev_node = head;
        head = head->next;
    }
    node * next_node = head->next;
    prev_node->next = next_node;
    free(head);
}

void free_list(node * head){
    node * next = head->next;
    while (head != NULL){
        next = head->next;
        free(head);
        head = next;
    }
}
