#include <stdio.h>
#include <stdlib.h>

#define INIT_HEAP_CAPACITY 4

/* Macros to navigate a heap array's tree structure. */
#define PARENT(item)      ( ( ( (item) + 1) / 2) - 1)    /* the index of item's parent      */
#define LEFT_CHILD(item)  ( ( ( (item) + 1) * 2) - 1)     /* the index of item's left child  */
#define RIGHT_CHILD(item) ( ( (item) + 1) * 2) /* the index of item's right child */

typedef struct heap_item{
    int value;
    int priority;
} heap_item;

typedef struct Heap{
    heap_item *heap_array; //pointer to first item of array
    int size; //capacity of heap
    int num_items; //number of items in heap
} Heap;

void create_heap(Heap *heap){
    heap->num_items = 0;
    heap->size = INIT_HEAP_CAPACITY;
    heap->heap_array = (heap_item *)malloc((heap->size) * sizeof(heap_item));
}

void swap(heap_item *heap_array, int i1, int i2){
    heap_item tmp = heap_array[i1];
    heap_array[i1] = heap_array[i2];
    heap_array[i2] = tmp;
}

void swimup(Heap *heap){
    heap_item *heap_array = heap->heap_array;
    int last_item_priority = (heap_array + heap->num_items - 1)->priority;
    int parent_index = PARENT(heap->num_items - 1);
    int parent_index_priority = (heap_array + parent_index)->priority;
    while (last_item_priority < parent_index_priority){}
    return;
}