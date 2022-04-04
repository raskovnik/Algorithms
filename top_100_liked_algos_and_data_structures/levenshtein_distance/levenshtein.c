#include <stdio.h>
#include <stdlib.h>

int levenshtein(char x[], int m, char y[], int n) {
    int cost = 0;
    for (int i = 0; i < n; i ++) {
        if (i == n - 1) {
            cost += abs(m - n);
            return cost;
        }
        if ((x[i] != y[i])) {
            cost += 1;
        }
    }
    return cost;
}

void main() {
    char x[1024] = "faljkdkjdafhhiusahdjfkadhfkjhadjhfiuahsduifjakljhakdhfkjhajwioendkajsdnjlfiwheadfhakjdfhakjhhajdhfjkahdkfhakdfhakjhdfhakjdfahdf";
    char y[1024] = "kafkjahdfkjhakjdshfksdfkjhasdkjfskahfkjsadkfjhaskdhfhajkfvakhdghasdfauhuiawrhbduabudfajfdnaiuwedhbfnwadiuhbfnkaergfuhbjnadsfhvbhjwadkfjvj";
    int m = sizeof(x) / sizeof(x[0]);
    int n = sizeof(y) / sizeof(y[0]);
    printf("%d\n", levenshtein(y, n, x, m));
}