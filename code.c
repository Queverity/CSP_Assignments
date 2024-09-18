#include <stdio.h>
#include <string.h>

int main() {
    char name[100];

    // Prompt the user for their name
    printf("Enter your name: ");
    fgets(name, sizeof(name), stdin);

    // Remove the newline character if it's present
    size_t len = strlen(name);
    if (len > 0 && name[len - 1] == '\n') {
        name[len - 1] = '\0';
    }

    // Print the name surrounded by symbols
    printf("<<< %s >>>\n", name);

    return 0;
}