#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* concat_all(char **strs, int strs_sz)
{
    int size = 0;
    for (int i=0; i<strs_sz; i++){
        size += strlen(strs[i]);
    }
    char *all = (char *)malloc(size * sizeof(char));
    for (int j=0; j<strs_sz; j++){
        strcat(all, strs[j]);
    }
    all += 3;
    return all;
}