#include <stdio.h>

int main(void) {
    int a[3] = {2,3,4};
    f2(a);

    /* when you pass an array to a list, you are passing
    the ADDRESS of the first element */

    /* address of array is same as value of array */
    // a = a + 1; raises error since a cannot be modified

    int an_int = 0;
    printf("An int takes up %ld bytes\n", sizeof(an_int));
    float a_float = 0;
    printf("A float takes up %ld bytes\n", sizeof(a_float));
    double a_double = 0;
    printf("A double takes up %ld bytes\n", sizeof(a_double));
    long int a_long = 0;
    printf("A long int takes up %ld bytes\n", sizeof(a_long));
    char a_char = 'a';
    printf("A char takes up %ld bytes\n", sizeof(a_char));

    printf("sizeof(a) %ld\n", sizeof(a));
    printf("length of array: sizeof(a)/sizeof(a[0]) %ld\n", sizeof(a)/sizeof(a[0]));
    





    printf("%d\n", a[1]);

    f(a);
    f2(a);
    // a[0] is the same as *a

    int * p_a = &a[0];
    p_a + 1; //1028
    p_a + 2; //1032
    *(p_a + 1); //3
    p_a[1]; // *(p_a + 1)
    a[1]; // *(a + 1)

}


void f(int a[]) {
    a[0] = 5; //equivalently: *a = 5;
}



void f2(int *a) {
    a[0] = 5; //equivalently: *a = 5;
    a[1] = 6;
}

// works same way