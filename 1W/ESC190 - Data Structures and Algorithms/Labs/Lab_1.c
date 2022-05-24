#include <stdio.h>


void change_num(int *ptr) {
    *ptr = 10;
}


void print_list(int arr[]) {
    int i = 0;
    for (i=0; i<5; i++) {
        printf("%d", arr[i]);
    }
    printf("\n");
}

void insertion_sort(int arr[], int size_arr) {
    int i = 0;
    int j = 0;
    int x = 0;
    for (i=1; i<size_arr; i++) {
        x = arr[i];
        j = i - 1;
        while (j >= 0 && x < arr[j]) {
            arr[j+1] = arr[j];
            j = j - 1;
        }
        arr[j + 1] = x;
    }
}


int main() {
    int a = 5;
    printf("%d\n", a);
    int *ptr_a = &a;
    change_num(ptr_a);
    printf("%d\n", a);


    int arr[5] = {3,2,6,4,1};
    print_list(arr);
    int size_arr = sizeof(arr)/sizeof(arr[1]);

    insertion_sort(arr, size_arr);
    print_list(arr);

    return 0;
}

