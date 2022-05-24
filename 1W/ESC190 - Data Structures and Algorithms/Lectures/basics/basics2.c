#include <stdio.h>

void swap(int *p_a, int *p_b) {
    int temp = *p_a;
    *p_a = *p_b;
    *p_b = temp;

}


int main(void) {
    int a = 5;
    int* p_a = &a;
    printf("address of a: %ld|n", p_a);
    *p_a = 4; //a becomes 4
    int b = 6;

    int** pp_a = &p_a;

    swap(&a, &b);
    swap(&b, &a);

    return 0;
}