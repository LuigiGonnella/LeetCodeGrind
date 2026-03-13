#define MAX 20
#define N 5
#include <string.h>
#include <stdio.h>
#include <stdlib.h>

typedef enum {
    search, modify, paste, end, err
} commands;


commands read_command() {
    commands command;
    char cmd[MAX];
    char TABLE[N][MAX] = {"search", "modify", "paste", "end", "err"};

    printf("Insert command: \n");
    scanf("%s", cmd);
    command = search;

    while(command < err && strcmp(cmd, TABLE[command])!=0) { //enum like integer
        command++;
    }

    return command;
    
}

void main() {
    commands command;
    char complete_row[MAX];
    while(1) {
        command = read_command();
        fgets(complete_row, MAX, stdin); //the rest of the line
        switch(command) {
            case search: printf("search\n"); break;
            case modify: printf("modify\n"); break;
            case paste: printf("paste\n"); break;
            case end: printf("end\n"); goto endloop;
            case err: printf("err\n"); break;
        }
    }

    endloop:

}