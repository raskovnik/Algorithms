int sort(int A[], int n) {
    int k = 0;

    for (int i = 0; i < n; i++) {
        if (A[i] == 0) {A[k++] = 0;}
    }

    for (int i = k; i < n; i++) { A[k++] = 1;}

    for (int i = 0; i < n; i ++) {printf("%d  ", A[i]);}
}

int main() {
    int A[] = { 0, 0, 1, 0, 1, 1, 0, 1, 0, 0 };
    int n = sizeof(A)/sizeof(A[0]);
    
    sort(A, n);
}