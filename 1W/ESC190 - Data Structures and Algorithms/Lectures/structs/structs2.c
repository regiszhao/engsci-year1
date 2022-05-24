#include <stdio.h>
#include <stdlib.h>

struct student_record {
    int esc180;
    int phy180;
};

void f(struct student_record s) {
    s.esc180 = 100; // has no effect outside the function
}

void f1(int * a) {
    *a = 100;
}

void f2(struct student_record * ps) {
    (*ps).esc180 = 100;  // has an effect
}
// (*a).b is equivalent to a->b
void f3(struct student_record * ps) {
    ps->esc180 = 100;  // more common syntax
}


int *make_arr(int size_arr) {
    return (int *)malloc(size_arr * sizeof(int));
}

int *make_arr_wrong() {
    int a[10];  // local variable
    return a;
}

int *make_arr_wrong() {
    int a;  // local variable
    return &a;
}

int main(void) {
    struct student_record s;
    struct student_record s1;
    s.esc180 = 94;
    s1.esc180 = 95;
    f(s);
    f1(&s.esc180); //has an effect

    // int a = 5;
    // float b = (float)a;

    printf("%ld %ld %ld", (&s), &s.esc180, &s.phy180);

    int * a = (int *)malloc(10 * sizeof(int));
    int size_arr = 10;
    int * a = (int *)malloc(size_arr * sizeof(int));
    a[5] = 15; // *(a+5) = 15;
    // malloc returns an address - a variable of type void*, 
    // we then cast it to int *

    int *c = make_arr(50);
    c[10] = 40;
    printf("c: %ld", c);
    free(c); // frees memory allocated to c
}