#include "lists.h"

/**
 * insert_node- Inserting node in the right order
 * @head: the head node
 * @number: the value of the node
 * Return: the new node
*/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp = *head;
	listint_t *prev;
	listint_t *new = malloc(sizeof(listint_t));

	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (*head == NULL)
		*head = new;
	else if (temp->n <= number)
	{
		while (temp->n <= number)
		{
			prev = temp;
			temp = temp->next;
		}

		prev->next = new;
		new->next = temp;
	}
	else if (temp->n > number)
	{
		new->next = *head;
		*head = new;
	}

	return (new);
}
