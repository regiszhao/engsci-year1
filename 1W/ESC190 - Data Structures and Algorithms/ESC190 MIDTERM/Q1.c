#include <stdio.h>
#include <stdlib.h>

int string_len(char *str){
    int len = 0;
    while(str[len] != '\0'){
        len++;
    }
    return len;
}

int my_atoi(char *str){
    if (str[0] == '0'){return 0;}
    else if (str[0] == '1'){return 1;}
    else if (str[0] == '2'){return 2;}
    else if (str[0] == '3'){return 3;}
    else if (str[0] == '4'){return 4;}
    else if (str[0] == '5'){return 5;}
    else if (str[0] == '6'){return 6;}
    else if (str[0] == '7'){return 7;}
    else if (str[0] == '8'){return 8;}
    else if (str[0] == '9'){return 9;}
}

double poww(int exp){
    double res = 10;
    for (int i=1; i<exp; i++){
        res *= 10;
    }
    return res;
}

double my_atof(char *str){
    int i = 0;
    int power = 0, dec_len = 0;
    double res = 0;

    while (str[i] != '.'){
        power++;
        i++;
    }
    for (int j=0; j<power; j++){
        int base = my_atoi(str+j);
        res += base * poww(power-j);
    }

    char *dec_str = str + i + 1;
    int k = 0;
    while(dec_str[k] != '\0'){
        k++;
        power = -k;
        int base = my_atoi(dec_str+k);
        res += base * poww(power);
    }
    
    return res;
}


// int main(void){
//     char a[8] = "123.123";
//     // printf("%d", string_len(a));
//     // int b = my_atoi("4");
//     // printf("%d", b);

//     printf("%f", my_atof(a));
// }