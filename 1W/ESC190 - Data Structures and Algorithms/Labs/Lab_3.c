#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <math.h>

//Q1
char* my_strcat(char* dest, char* src){
    char* start = dest;
    while(*dest != '\0'){
        dest++;
    }
    while(*src != '\0'){
        *dest = *src;
        dest++;
        src++;
    }
    return start;
}

//Q2
int my_strcmp_rec(char* s1, char* s2){
    if (*s1 == '\0' && *s2 == '\0'){
        return 0;
    }
    else if (*s1 != *s2){
        return *s1 - *s2;
    }
    else{
        return my_strcmp_rec(++s1, ++s2);
    }
}

//Q3
int my_atoi(char* str){
    int len = strlen(str);
    int res = 0;
    for (int i=0; i<len; i++){
        int n = str[len-1-i]-'0';
        res = res + (n * pow(10, i));
    }
    return res;
}


//Q4
struct node{
    struct node * next;
};

int floyd(struct node * head){
    struct node * t = head;
    struct node * h = head;
    while ((h->next != NULL) && (h->next->next != NULL)){
        t = t->next;
        h = h->next->next;
        if (t == h){
            return 1;
        }
    }
    return 0;
}


int main(void)
{
    //Q1
    char s1[4] = "abc";
    char s2[4] = "def";
    my_strcat(s1, s2);
    printf("%s\n", s1);

    //Q2
    char s3[4] = "abc";
    char s4[4] = "abd";
    int a = my_strcmp_rec(s3, s4);
    printf("%d\n", a);

    //Q3
    char digits[4] = "123";
    int num = my_atoi(digits);
    printf("%d\n", num);

    //Q4
    struct node * node0 = (struct node *)malloc(sizeof(struct node));
    struct node * node1 = (struct node *)malloc(sizeof(struct node));
    node0->next = node1;
    struct node * node2 = (struct node *)malloc(sizeof(struct node));
    node1->next = node2;
    struct node * node3 = (struct node *)malloc(sizeof(struct node));
    node2->next = node3;
    struct node * node4 = (struct node *)malloc(sizeof(struct node));
    node3->next = node4;
    node4->next = node0;
    printf("%d\n", floyd(node0));


    struct node * node5 = (struct node *)malloc(sizeof(struct node));
    struct node * node6 = (struct node *)malloc(sizeof(struct node));
    node5->next = node6;
    struct node * node7 = (struct node *)malloc(sizeof(struct node));
    node6->next = node7;
    struct node * node8 = (struct node *)malloc(sizeof(struct node));
    node7->next = node8;
    struct node * node9 = (struct node *)malloc(sizeof(struct node));
    node8->next = node9;
    node9->next = NULL;
    printf("%d", floyd(node5));

}