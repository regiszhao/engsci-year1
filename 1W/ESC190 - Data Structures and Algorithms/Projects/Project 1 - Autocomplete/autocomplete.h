#if !defined(AUTOCOMPLETE_H)
#define AUTOCOMPLETE_H

#define NEWLINE printf("\n")
#define DEBUG_READING 0
#define DEBUG_READING1 0
#define DEBUG_SORTING 0
#define DEBUG_AUTOCOMPLETE 1

struct term{
    char term[200]; // assume terms are not longer than 200
    double weight;
};

void read_in_terms(struct term **terms, int *pnterms, char *filename);
int lowest_match(struct term *terms, int nterms, char *substr);
int highest_match(struct term *terms, int nterms, char *substr);
void autocomplete(struct term **answer, int *n_answer, struct term *terms, int nterms, char *substr);

#endif
