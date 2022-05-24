#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int my_strlen(char *s1){
    int len = 0;
    while(s1 != NULL){
        len++; // same as len = len + 1
        s1++;
    }
    return len;
}

void my_strcpy(char *dest, char *src){
    while(*src != NULL){
        *dest = *src; // copying characters one by one
        src++;
        dest++;
    }
}
// same as:
void my_strcpy2(char *dest, char *src){
    while(*src != NULL){
        *dest++ = *src++;
    }
}

int main(void)
{
    char c1 = 'a'; // character literal (single quotes)
    char c2 =  'A';
    char *s1 = "asdfjasdfj"; // string literal (double quotes)
    // s1[2];
    // s1[2] = 'z';  <-- not guaranteed to work (but most likely)
    char *s2 = (char *)malloc(sizeof(char) * 20);
    s2[0] = "A";
    char s3[20];

    // "abc" C stores: ['a', 'b', 'c', NULL]
    // strings are arrays of characters w/ NULL at the end
    char s4[4] = "abc";

    printf("%s\n", s4);
    printf("%c\n", *s4);
    printf("%ld\n", s1);

    // copy strings
    char s5[20] = "abc";
    char s6[20];
    strcpy(s6, s5); // s6 is destination, s5 is source
    // s6 = s5 is an error
    strlen(s5); // length of str (num of characters not counting NULL)
    strcmp(s5, s6); // returns <0 if s5 comes before s6 in
    // lexicographic ordering, returns 0 if they are same, returns
    // >0 otherwise (not the same as s5 == s6, for pointers, checks
    // whether s5 and s6 are aliases)

    printf("%ld\n", sizeof(s1));
    printf("%ld\n", sizeof(char));
    printf("%d", sizeof(s1)/sizeof(char));

    return 0;
}
