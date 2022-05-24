// to run: gcc -Wall autocomplete.h main.c

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "autocomplete.h"
#define NEWLINE printf("\n")
#define DEBUG_READING 0
#define DEBUG_READING1 0
#define DEBUG_SORTING 0
#define DEBUG_AUTOCOMPLETE 0

static void print_all_terms(struct term *head_term, int nterms);
static void make_term(char *line, struct term *dest_term);
static int termcmp(const void *term1, const void *term2);
static int weightcmp(const void *term1, const void *term2);


void print_all_terms(struct term *head_term, int nterms){
    //prints all terms in block
    for (int i=0; i<nterms; i++){ //for loop to assign terms
        printf("Weight: %f, Term: %s", (head_term+i)->weight, (head_term+i)->term);
        NEWLINE;
    }
}

void make_term(char *line, struct term *dest_term){
    // reads in a line and converts it to a term
    char *raw_term;
    char *cut_term;
    dest_term->weight = strtod(line, &raw_term); // assigns weight

    cut_term = raw_term + 1; //gets rid of tab in front
    cut_term[strlen(cut_term)-1] = '\0'; // gets rid of newline character at the end
    strcpy(dest_term->term, cut_term); // assigns string
    return;
}

// int termcmp(struct term *term1, struct term *term2){
//     // comparison function for terms (used in qsort)
//     return strcmp(term1->term, term2->term);
// }

int termcmp(const void *term1, const void *term2){
    // comparison function for terms (used in qsort)
    struct term *new_term1 = (struct term *)term1;
    struct term *new_term2 = (struct term *)term2;
    return strcmp(new_term1->term, new_term2->term);
}

void read_in_terms(struct term **terms, int *pnterms, char *filename){
    char line[200];
    FILE *fp = fopen(filename, "r");
    int nterms = atoi(fgets(line, sizeof(line), fp)); //number of terms
    *pnterms = nterms; //store value of nterms at pnterms

    struct term *head_term = (struct term *)malloc(sizeof(struct term) * nterms); //allocating memory for block of terms
    for (int i=0; i<nterms; i++){ //for loop to assign terms
        fgets(line, sizeof(line), fp);
        if (DEBUG_READING){
        printf("%s", line);}
        make_term(line, head_term + i);
        if (DEBUG_READING){
        printf("Weight: %f, Term: %s", (head_term+i)->weight, (head_term+i)->term);
        NEWLINE;NEWLINE;}
    }
    qsort(head_term, nterms, sizeof(struct term), termcmp);
    if(DEBUG_SORTING){print_all_terms(head_term, nterms);}
    *terms = head_term;
    fclose(fp);
    return;
}


int lowest_match(struct term *terms, int nterms, char *substr){
    int low = 0, high = nterms - 1, mid;
    int len_substr = strlen(substr);
    int comparison, cmp_prev_term;
    while (low <= high){
        mid = (high + low) / 2;
        comparison = strncmp(substr, (terms+mid)->term, len_substr);
        if (comparison == 0){
            cmp_prev_term = strncmp(substr, (terms+mid-1)->term, len_substr);
            if (cmp_prev_term != 0 || mid == low){
                return mid;
            }
            high = mid - 1;
        } 
        else if (comparison < 0){
            high = mid - 1;
        }
        else{
            low = mid + 1;
        }
    }
    return -1;
}

int highest_match(struct term *terms, int nterms, char *substr){
    int low = 0, high = nterms - 1, mid;
    int len_substr = strlen(substr);
    int comparison, cmp_next_term;
    while (low <= high){
        mid = (high + low) / 2;
        comparison = strncmp(substr, (terms+mid)->term, len_substr);
        if (comparison == 0){
            cmp_next_term = strncmp(substr, (terms+mid+1)->term, len_substr);
            if (cmp_next_term != 0 || mid == high){
                return mid;
            }
            low = mid + 1;
        } 
        else if (comparison < 0){
            high = mid - 1;
        }
        else{
            low = mid + 1;
        }
    }
    return -1;
}


// int weightcmp(struct term *term1, struct term *term2){
//     // comparison function for terms (used in qsort)
//     return ( (int)(term1->weight) - (int)(term2->weight) );
// }

int weightcmp(const void *term1, const void *term2){
    // comparison function for terms (used in qsort)
    struct term *new_term1 = (struct term *)term1;
    struct term *new_term2 = (struct term *)term2;
    return -( (int)(new_term1->weight) - (int)(new_term2->weight) );
}

void autocomplete(struct term **answer, int *n_answer, struct term *terms, int nterms, char *substr){
    int low_index = lowest_match(terms, nterms, substr);
    int high_index = highest_match(terms, nterms, substr);

    if ( (low_index == -1) || (high_index == -1) ){
        *n_answer = 0;
        return;
    }

    *n_answer = high_index - low_index + 1;
    struct term *head_answer = (struct term *)malloc(sizeof(struct term) * (*n_answer));
    for (int i=0; i<(*n_answer); i++){
        (head_answer + i)->weight = (terms + low_index + i)->weight;
        strcpy((head_answer + i)->term, (terms + low_index + i)->term);
    }
    if (DEBUG_AUTOCOMPLETE){print_all_terms(head_answer, *n_answer);NEWLINE;NEWLINE;NEWLINE;NEWLINE;}
    qsort(head_answer, *n_answer, sizeof(struct term), weightcmp);
    if (DEBUG_AUTOCOMPLETE){print_all_terms(head_answer, *n_answer);}
    *answer = head_answer;
    return;
}