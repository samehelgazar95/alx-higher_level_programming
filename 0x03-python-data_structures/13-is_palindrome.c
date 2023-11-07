#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome- Cheching if numbers are palindrome
 * @head: the head of the node
 * Return: Success (1), Failure (0)
*/
int is_palindrome(listint_t **head)
{
    listint_t *ptr1;
    listint_t *ptr2;

    ptr1 = *head;
    ptr2 = *head;

    while (ptr2->next != NULL)
        ptr2 = ptr2->next;

    

}