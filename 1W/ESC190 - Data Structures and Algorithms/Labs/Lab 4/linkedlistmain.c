#include <stdio.h>
#include <stdlib.h>
#include "linkedlist.h"

int main(void)
{
    node * head = create_node(1, NULL);
    append_node(head, 2);
    append_node(head, 4);
    printf("Initializing list: ");
    print_list(head);
    printf("\n");

    printf("Inserting 3 at index 2: ");
    insert_node(head, 2, 3);
    print_list(head);
    printf("\n");

    printf("Deleting 2: ");
    delete_node(head, 2);
    print_list(head);
    printf("\n");

    //freeing the list
    free_list(head);

    return 0;
}