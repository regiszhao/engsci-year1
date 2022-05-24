#include <stdio.h>
#include "2021_02_02.h"

#define COURSE 180
#define ABS(x) x < 0 ? -x : x
#define MAX(x, y) (((x) > (y)) ? (x) : (y))

struct node{
    int data;
    struct node* next;
};

int main(void)
{
    f();
    printf("%d\n", COURSE);

    ABS(-4.5);
    MAX(3,6);

    return 0;

}



int max_fn(int a, int b){
    return (a > b) ? a : b;
}



// COND ? OUT1 : OUT2 
// same as
// if(COND){
//     OUT1
// }else{
//     OUT2
// }