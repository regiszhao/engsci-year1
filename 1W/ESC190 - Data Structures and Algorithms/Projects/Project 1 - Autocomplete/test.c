#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define NEWLINE printf("\n")
#define STR_LEN 200
#define TESTING 0
#define RUNNING 0

int main(void)
{
    if(RUNNING){
    char line[STR_LEN+1];
    FILE *fp = fopen("cities.txt", "r");
    // fgets(line, sizeof(line), fp);
    // int nterms = atoi(line);
    int nterms = atoi(fgets(line, sizeof(line), fp));
    printf("%d", nterms);
    NEWLINE;

    fgets(line, sizeof(line), fp);
    printf("%s", line);
    NEWLINE;

    char *city_name;
    double weight = strtod(line, &city_name);
    printf("%f", weight);
    NEWLINE;

// TESTINGGGGGGGGGGGGGGGGGGGG
    if (TESTING){
    // print length of uncut city name string
    int len_str = strlen(city_name);
    printf("%d", len_str);
    NEWLINE;

    city_name[len_str-1] = '\0';
    len_str = strlen(city_name);
    printf("%d", len_str);

    printf("%c", city_name[len_str-1]);
    NEWLINE;}
/////////////////////////////

    char *cut_city_name = city_name+1;
    int len_str = strlen(cut_city_name);
    cut_city_name[len_str-1] = '\0';
    len_str = strlen(cut_city_name);
    printf("%d", len_str);
    printf("%s", cut_city_name);
    }

    char *str1 = "abc";
    char *str2 = "abc";
    if (str1 == str2){printf("urmomgay");}

    return 0;
}

