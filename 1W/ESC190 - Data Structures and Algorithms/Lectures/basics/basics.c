#include <stdio.h>

int main() {
	int a = 8;	// other types: double, char, bool (same as int)
							/*multiline comment
							blahblahblah
							hahahahahaha
							*/
	printf("2*a = %d", 2*a);		// %d: decimal (int)
					                // %s: string
									//%ld: long (long int)
	int grade = 97;
	if (grade >= 50) {
		printf("pass\n");
	} else if (grade <= 50) {
		//
	} else {
		//
	}

	//Type: pointer
	int *p_a = &a;
	printf("%ld\n", p_a);

	// *p_a: the value at the address p_a
	printf("%d\n", *p_a);




	return 0;
}

void f(int a) {
	printf("%d\n", 2*a);
}