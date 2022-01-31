#include <stdio.h>
#define SIZE 9

int board[SIZE][SIZE] = {
    {7,8,0,4,0,0,1,2,0},
    {6,0,0,0,7,5,0,0,9},
    {0,0,0,6,0,1,0,7,8},
    {0,0,7,0,4,0,2,6,0},
    {0,0,1,0,5,0,9,3,0},
    {9,0,4,0,6,0,0,0,5},
    {0,7,0,3,0,0,0,1,2},
    {1,2,0,0,0,7,4,0,0},
    {0,4,9,2,0,6,0,0,7}};

void print_board(int board[SIZE][SIZE]) {
    for (int row = 0; row < SIZE; row++) {
            if (row % 3 == 0) {printf("-------------------------------------\n");}

        for (int col = 0; col < SIZE; col++) {
            if (col % 3 == 0) {printf(" | ");}
            printf(" %d ", board[row][col]);
            if (col == SIZE - 1) {printf("| \n");}
        }
    }
    printf("-------------------------------------\n");
}

void write_to_txt(int board[SIZE][SIZE]) {
    FILE *pF = fopen("solutions1.txt", "a");
    for (int row = 0; row < SIZE; row++) {
        if (row % 3 == 0) {fprintf(pF, "-------------------------------------\n");}

    for (int col = 0; col < SIZE; col++) {
        if (col % 3 == 0) {fprintf(pF, " | ");}
        fprintf(pF, " %d ", board[row][col] );
        if (col == SIZE - 1) {fprintf(pF, "| \n");}
    }
}
    fprintf(pF, "-------------------------------------\n");
    fprintf(pF, "\n");
    fclose(pF);

}

int is_in_row(int board[SIZE][SIZE], int row, int number) {
    for (int col = 0; col < SIZE; col++) {
        if (board[row][col] == number) {return 0;}
    }
    return 1;
}

int is_in_column(int board[SIZE][SIZE], int col, int number) {
    for (int row = 0; row < SIZE; row++) {
        if (board[row][col] == number) {return 0;}
    }
    return 1;
}

int is_in_box(int board[SIZE][SIZE], int row, int col, int number) {
    int b_row = row - row % 3;
    int b_col = col - col % 3;

    for (int i = b_row; i < b_row + 3; i++) {
        for (int j = b_col;j < b_col+ 3; j++) {
            if (board[i][j] == number) {return 0;}
        }
    }
    return 1;
}

int is_valid_position(int board[SIZE][SIZE], int row, int col, int number) {
    if (is_in_box(board, row, col, number) == 1 && is_in_column(board, col, number) == 1 && is_in_row(board, row, number) == 1) {return 0;}
    return 1;
}

int solve(int board[SIZE][SIZE]) {
    int empties = 0;
    for (int i = 0; i < SIZE; i++) {
        for (int j = 0; j < SIZE; j++) {
            if (board[i][j] == 0) {
                for (int num = 1; num <= SIZE; num++) { 
                    if (is_valid_position(board, i, j, num) == 0) {
                        board[i][j] = num;
                        write_to_txt(board);
                        if (solve(board) != 0) {board[i][j] = 0; empties++;}
                        else {return 0;}
                    }
                }
                return 1;
            }
        }
    }
    return empties != 0;
}

int main() {
    print_board(board);
    solve(board);
    puts("");
    if (solve(board) == 0) {
        printf("Solved:\n");
        print_board(board);
    }
    else {
        printf("Cannot solve the grid\n");
        print_board(board);
    }
}