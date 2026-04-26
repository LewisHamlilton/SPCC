#include <stdio.h>
#include "Palindrome.h"

int n, temp, rem, rev, isPal;

int main()
{
    printf("Enter a number: ");
    scanf("%d", &n);
    
    checkPalindrome(n);

    if (isPal == 1) {
        printf("\n%d is a Palindrome number.\n", n);
    } else {
        printf("\n%d is not a Palindrome number.\n", n);
    }

    return 0;
}
