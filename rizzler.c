#include <stdio.h>

int main() {
    // Array of names
    const char *names[] = {"Alice", "Bob", "Charlie", "David", "Eve"};
    int num_names = sizeof(names) / sizeof(names[0]);

    // Loop through the names and print greetings
    for (int i = 0; i < num_names; i++) {
        printf("Hello, %s!\n", names[i]);
    }

    return 0;
}
