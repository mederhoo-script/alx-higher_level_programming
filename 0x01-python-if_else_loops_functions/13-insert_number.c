#include "lists.h"

/**
 * insert_node - Inserts
 * @head: A pointer to head
 * @number: number innsert.
 * Return: NULL..
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *mid;

	mid = malloc(sizeof(listint_t));
	if (mid == NULL)
		return (NULL);
	mid->n = number;

	if (node == NULL || node->n >= number)
	{
		mid->next = node;
		*head = mid;
		return (mid);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;

	mid->next = node->next;
	node->next = mid;

	return (mid);
}
