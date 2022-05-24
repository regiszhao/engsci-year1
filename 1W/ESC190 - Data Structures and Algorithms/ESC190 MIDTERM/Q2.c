#include <stdio.h>
#include <stdlib.h>

int charcmp(char *str1, char *str2, int index){
    return str1[index] - str2[index];
}

int my_strncmp(char *str1, char *str2, int num){
    if (num == 0){
        return 0;
    }
    if (str1[0] == '\0' || str2[0] == '\0'){
        return 0;
    }
    if (charcmp(str1, str2, 0) != 0){
        return charcmp(str1, str2, 0);
    }
    return my_strncmp(str1+1, str2+1, num-1);
}

// int main(void){
//     char a[4] = "abc";
//     char b[4] = "abc";
//     printf("%d", my_strncmp(a, b, 3));
// }