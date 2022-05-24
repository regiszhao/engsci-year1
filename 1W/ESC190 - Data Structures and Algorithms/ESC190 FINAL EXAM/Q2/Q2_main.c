#include <string.h>
#include <stdio.h>
#include "Q2.h"

int main(void){
	char *strs1[] = {"ESC", "MAT", "MSE", "CIV"};
	printf("%d\n", repeats(strs1, 4)); // 0

	char *strs2[] = {"ESC", "MAT", "MSE", "CIV", "ESC"};
	printf("%d\n", repeats(strs2, 5)); // 1
	return 0;
}

