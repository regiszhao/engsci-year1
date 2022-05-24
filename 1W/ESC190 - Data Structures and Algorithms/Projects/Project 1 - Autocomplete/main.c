// to run: gcc -Wall autocomplete.h main.c

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "autocomplete.h"

int main(void)
{
    struct term *terms;
    int nterms;
    read_in_terms(&terms, &nterms, "cities.txt");
    // read_in_terms(&terms, &nterms, "wiktionary.txt");
    if (DEBUG_READING1){print_all_terms(terms, nterms);}

    // lowest_match(terms, nterms, "Tor");
    // highest_match(terms, nterms, "Tor");

    // struct term *answer;
    // int n_answer;
    // autocomplete(&answer, &n_answer, terms, nterms, "Tor");

    if (DEBUG_AUTOCOMPLETE){
        char *substr = "Montré";
        int low_index = lowest_match(terms, nterms, substr);
        int high_index = highest_match(terms, nterms, substr);
        printf("Lowest match: %d    Highest match: %d", low_index, high_index);
        NEWLINE;
        struct term *answer;
        int n_answer;
        autocomplete(&answer, &n_answer, terms, nterms, substr);
    }


    //free allocated blocks here -- not required for the project, but good practice
    
    return 0;
}