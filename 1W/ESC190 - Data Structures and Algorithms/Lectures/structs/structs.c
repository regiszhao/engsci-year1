#include <stdio.h>

void print_arr(int * arr, int size) {
    int i = 0;
    for (i = 0; i < size; i++) {  // i++ is same as i+=1
        printf("%d", arr[i]);
    }
}

struct student_record {
    int esc180;
    int phy180;
};

int main(void) {
    int SIZE_ARR = 3;
    int a[3] = {4, 5, 6};
    //print_arr(a, SIZE_ARR);
    struct student_record student1;
    student1.esc180 = 85;
    student1.phy180 = 82;
    printf("%ld", sizeof(struct student_record));
}