#include <stdio.h>
#include <stdlib.h>
#include "intset.h"

//Create an intset, and place a pointer to it in *s.
void intset_create(struct intset **s){
    struct intset *int_set = (struct intset*)malloc(sizeof(struct intset));
    int_set->head = NULL;
    *s = &int_set;
}

//Add the elements from attay elems to intset s. There are
//num_elems elements in elems
void intset_add(struct intset *s, int *elems, int num_elems){
    struct node *head_node = (struct node *)malloc(sizeof(struct node) * num_elems);
    if (s->head == NULL){
        s->head = head_node;
    }
    else{
        struct node *cur_node = s->head;
        while (cur_node->next != NULL){
            cur_node = cur_node->next;
        }
        cur_node->next = head_node;
    }
    for (int i=0; i<num_elems; i++){
        (head_node+i)->data = elems[i];
        (head_node+i)->next = head_node + i + 1;
    }
}

//Return 1 if element elem is in intset s. Otherwise return 0.
int intset_iselem(struct intset *s, int elem){
    struct node *cur_node = s->head;
    while (cur_node->next != NULL){
        if (cur_node->data == elem){
            return 1;
        }
        cur_node = cur_node->next;
    }
    if (cur_node->data == elem){
        return 1;
    }
    return 0;
}

//Remove element elem from s, of eleme is in s. If the element 
//is not in s, do nothing.
//free memory that's not needed anymore
void intset_remove(struct intset *s, int elem){
    if (intset_iselem(s, elem) == 0){
        return;
    }
    struct node *cur_node = s->head;
    struct node *prev_node = cur_node;
    while (cur_node->next != NULL){
        if (cur_node->data == elem){
            prev_node->next = cur_node->next;
            free(cur_node);
        }
        prev_node = cur_node;
        cur_node = cur_node->next;
    }
    if (cur_node->data == elem){
            prev_node->next == NULL;
            free(cur_node);
        }
}

//Compute the union of sets s1 and s2, and place the
//result in a new intset *s3.
void intset_union(struct intset *s1, struct intset *s2, struct intset **s3){
    //loop through elements in s1 and s2 and if the element is not already in s3, use intset_add to add the element to s3
    intset_create(s3);

    struct node *cur_node = s1->head;
    while (cur_node->next != NULL){
        if (intset_iselem(*s3, cur_node->data) == 0){
            intset_add(*s3, &(cur_node->data), 1);
        }
        cur_node = cur_node->next;
    }
    // if (cur_node->data == elem){
    //         prev_node->next == NULL;
    //         free(cur_node);
    //     }
}