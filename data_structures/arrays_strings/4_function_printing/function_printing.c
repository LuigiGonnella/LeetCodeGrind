#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#define N 20
#define M 70
#define X_MIN -1.0
#define X_MAX 4.0
#define Y_MIN -1.0
#define Y_MAX 10.0

char TABLE[N][M];




float function(float a, float b, float c, float x) {
    return a*pow(x, 2) + b*x + c;
}

void solve(float a, float b, float c, char table[N][M], float x_min, float x_max, float y_min, float y_max) {
    int i, j;
    float step_x = (x_max - x_min) / (M-1);
    float step_y = (y_max - y_min) / (N-1);

    for (i=0; i<N; i++) {
        for(j=0;j<M;j++) {
            table[i][j] = ' ';
        }
    }

    
    for (j=0; j<M; j++) {
        float x = j*step_x + x_min;
        float y = function(a, b, c, x);

        if (y >= y_min && y <= y_max) {
            i = (y - y_min) /step_y;
            table[i][j] = '*';
        }

    }

    for (i = N-1; i>=0; i--) {
        for (j=0; j<M; j++) {
            printf("%c", table[i][j]);
        }
        printf("\n");
    }
    
}



void main(void) {
    float a = 1.0, b = 2.0, c = 1.0;
    solve(a, b, c, TABLE, X_MIN, X_MAX, Y_MIN, Y_MAX);
}