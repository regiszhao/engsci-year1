/* FILE test_pq.c
 *    Minimal functionality test for min_pq.
 * Author: Francois Pitt, March 2012.
 */

#include <stdio.h>
#include <stdlib.h>

#include "min_pq.h"


/* FUNCTION main
 *    Test that min_pq implementation is reasonable.
 * Parameters and preconditions:  none
 * Return value:  exit status
 * Side-effects:  main program is executed
 */
int main(void)
{
    /* Only one "typical" test case -- this is NOT thorough! */
    long elems[] = {5L, 4L, 3L, 2L, 1L};
    min_pq_t *q = min_pq_create();

    min_pq_insert(q, elems+0, elems[0]);
    min_pq_insert(q, elems+1, elems[1]);
    min_pq_insert(q, elems+2, elems[2]);
    min_pq_insert(q, elems+3, elems[3]);
    min_pq_insert(q, elems+4, elems[4]);

    while (min_pq_size(q) > 0) {
        printf("%ld\n", *(long *) min_pq_remove_min(q));
    }

    min_pq_destroy(q);

    return EXIT_SUCCESS;
}
