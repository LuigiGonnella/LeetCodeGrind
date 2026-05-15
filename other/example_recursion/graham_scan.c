#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int x, y;
} Point;

// Funzione per calcolare l'orientamento tra tre punti
// >0 = sinistro, <0 = destro, 0 = collineare
int cross(Point p1, Point p2, Point p3) {
    return (p2.x - p1.x)*(p3.y - p1.y) - (p2.y - p1.y)*(p3.x - p1.x);
}

// Stack per i punti dell'hull
typedef struct {
    Point *points;
    int top;
    int capacity;
} Stack;

Stack* createStack(int n) {
    Stack* s = (Stack*)malloc(sizeof(Stack));
    s->points = (Point*)malloc(n * sizeof(Point));
    s->top = -1;
    s->capacity = n;
    return s;
}

void push(Stack* s, Point p) {
    s->top++;
    s->points[s->top] = p;
}

void pop(Stack* s) {
    if (s->top >= 0) s->top--;
}

Point peek(Stack* s) {
    return s->points[s->top];
}

Point nextToTop(Stack* s) {
    return s->points[s->top - 1];
}

// Graham Scan assumendo i punti già ordinati per angolo rispetto a p0
void grahamScan(Point points[], int n) {
    if (n < 3) {
        printf("Convex hull non possibile\n");
        return;
    }

    Stack* hull = createStack(n);

    // Push dei primi due punti ordinati
    push(hull, points[0]);
    push(hull, points[1]);

    for (int i = 2; i < n; i++) {
        // rimuove punti non convexi
        while (hull->top >= 1 && cross(nextToTop(hull), peek(hull), points[i]) <= 0) {
            pop(hull);
        }
        push(hull, points[i]);
    }

    // Stampa punti dell'hull
    printf("Convex Hull:\n");
    for (int i = 0; i <= hull->top; i++) {
        printf("(%d, %d)\n", hull->points[i].x, hull->points[i].y);
    }

    free(hull->points);
    free(hull);
}

// Esempio d'uso
int main() {
    // Assumiamo che i punti siano già ordinati per angolo rispetto a p0
    Point points[] = {{0, 0}, {1, 1}, {2, 2}, {2, 0}, {1, -1}, {0, -2}};
    int n = sizeof(points)/sizeof(points[0]);

    grahamScan(points, n);

    return 0;
}