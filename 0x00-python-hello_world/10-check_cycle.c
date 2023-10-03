#include "lists.h"

/**
 * check_cycle - checks for a cycle
 * @list: checked list
 *
 * Return: 1 if cycle, 0 if it doesn't
 */
int check_cycle(listint_t *list)
{
	listint_t *back = list;
	listint_t *fawd = list;

	if (!list)
		return (0);

	while (back && fawd && fawd->next)
	{
		back = back->next;
		fawd = fawd->next->next;
		if (back == fawd)
			return (1);
	}

	return (0);
}
