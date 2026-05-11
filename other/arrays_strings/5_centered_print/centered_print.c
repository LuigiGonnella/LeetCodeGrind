#include <string.h>
#include <stdio.h>
#include <stdlib.h>

#define NMAX 1000
#define ROW_MAX 10



void solve(char text[NMAX]) {
    int i = 0, curr_len = 0;
    char row[ROW_MAX];
    char* curr_word;
    strcpy(row, "");
    char *token = strtok(text, " \n");

    while(token!=NULL) {
        curr_word =  token;
        token = strtok(NULL,  " \n");
        if (curr_len + strlen(curr_word) + 1 > ROW_MAX) { //1 is the space
            if (row[curr_len -1] == ' ') { //remove space after last word
                row[curr_len-1] = '\0';
                curr_len--;
            }
            for (int i =0; i< (ROW_MAX - curr_len)/2; i++) {
                printf(" ");
            }
            for (int i =0; i<curr_len; i++) {
                printf("%c", row[i]);
            }
            printf("\n");

            
            strcpy(row, curr_word);
            strcat(row, " ");
            curr_len = strlen(row);
        } 
        else {
            
            strcat(row, curr_word);
            strcat(row, " "); //add space
            curr_len = strlen(row);
        }
       
    } //exit before printing last row

    if (curr_len > 0) { //if last row exists
        if (row[curr_len -1] == ' ') {
                row[curr_len-1] = '\0';
                curr_len--;
            }
        for (int i =0; i< (ROW_MAX - curr_len)/2; i++) {
                printf(" ");
            }
        for (int i =0; i<curr_len; i++) {
                printf("%c", row[i]);
            }
    }


}

int main() {
    char text[NMAX] = "This is      the first line of the text.\n"
    "Here is the second line.\n"
    "And this is the third one.\n"
    "Finally, this is the last line.\n";

    solve(text);
    return 0;


}
