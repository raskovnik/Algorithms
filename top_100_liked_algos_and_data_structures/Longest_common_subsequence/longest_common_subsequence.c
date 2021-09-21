#include <stdio.h>
#include <string.h>

int max(int a, int b);

int lcs(char *x, char *y, int m, int n) {
    if (m == 0 || n == 0) { return 0;}

    if (x[m - 1] == y[n - 1]) { return lcs(x, y, m - 1, n - 1) + 1;}

    return max(lcs(x, y, m, n -1), lcs(x, y, m - 1, n));

}

int max(int a, int b) { return (a > b)? a : b;}


int main() {
    char x[] = "ABCBDAB", y[] = "BDCABA";
    printf("The length of the LCS of %s and %s is %d\n", &x, &y, lcs(x, y, strlen(x), strlen(y)));
}

