#include <stdio.h>
#include <stdlib.h>

// Q1

struct node{
    int data;
    struct node *next;
};

void print_list(struct node *head){
    while (head->next != NULL){
        printf("%d, ", head->data);
        head = head->next;
    }
    printf("%d", head->data);
    return;
}

//Q2

void print_list_rec(struct node *head){
    if (head->next == NULL){
        printf("%d", head->data);
    }
    else{
        printf("%d, ", head->data);
        print_list_rec(head->next);
    }
    return;
}

//////////////////////////////////////////////////////////////////////////////////

//Q3

struct Node{
    void* ptr_data;
    int type; // 0 = int, 1 = float, 2 = double
    struct Node* next;
};

void print_list2(struct Node* head){
    while (head->next != NULL){
        if (head->type == 0){
            printf("%d, ", *(int *)(head->ptr_data));
        }
        else if (head->type == 1){
            printf("%f, ", *(float *)(head->ptr_data));
        }
        else{
            printf("%lf, ", *(double *)(head->ptr_data));
        }
        head = head->next;
    }
    if (head->type == 0){
        printf("%d", *(int *)(head->ptr_data));
    }
    else if (head->type == 1){
        printf("%f", *(float *)(head->ptr_data));
    }
    else{
        printf("%lf", *(double *)(head->ptr_data));
    }

}

void append(struct Node* head, void * ptr_data, int type){
    while (head->next != NULL){
        head = head->next;
    }

    //make node
    struct Node* node = (struct Node*)malloc(sizeof(struct Node));
    node->ptr_data = ptr_data;
    node->type = type;
    node->next = NULL;
    head->next = node;

    return;
}

void append_int(struct Node* head, int data){
    //initialize pointer address, data at pointer, and data type
    void * ptr_data = malloc(sizeof(int));
    *(int *)(ptr_data) = data;
    int type = 0;
    append(head, ptr_data, type);
    return;
}

void append_float(struct Node* head, float data){
    //initialize pointer address, data at pointer, and data type
    void * ptr_data = malloc(sizeof(float));
    *(float *)(ptr_data) = data;
    int type = 1;
    append(head, ptr_data, type);
    return;
}

void append_double(struct Node* head, double data){
    //initialize pointer address, data at pointer, and data type
    void * ptr_data = malloc(sizeof(double));
    *(double *)(ptr_data) = data;
    int type = 2;
    append(head, ptr_data, type);
    return;
}

/////////////////////////////////////////////////////////////////////////////////

int main(void)
{
    struct node *node0 = (struct node*)malloc(sizeof(struct node));
    node0->data = 1;
    struct node *node1 = (struct node*)malloc(sizeof(struct node));
    node0->next = node1;
    node1->data = 2;
    struct node *node2 = (struct node*)malloc(sizeof(struct node));
    node1->next = node2;
    node2->data = 3;
    node2->next = NULL;
    // printf("%c", node2->next);
    // printf("%ld", node0);
    print_list(node0); printf("\n");
    print_list_rec(node0); printf("\n");

    struct Node* Node0 = (struct Node*)malloc(sizeof(struct Node));
    Node0->ptr_data = malloc(sizeof(int));
    *(int *)(Node0->ptr_data) = 1;
    Node0->type = 0 ;
    Node0->next = NULL;

    struct Node* Node1 = (struct Node*)malloc(sizeof(struct Node));
    append_float(Node0, 3.1);
    struct Node* Node2 = (struct Node*)malloc(sizeof(struct Node));
    append_double(Node0, 3.14);
    struct Node* Node3 = (struct Node*)malloc(sizeof(struct Node));
    append_int(Node0, 21);

    print_list2(Node0);

    return 0;
}