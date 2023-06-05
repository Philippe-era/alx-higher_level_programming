#include "lists.h"

/**
 * last_cycle – checks if there is a cycle within this function 
 * @list: points to the first node
 * Return: 0 if success , 1 otherwise
 */
int last_cycle(listint_t *list)
{
	listint_t *first, *last;

	if (list == NULL || list->next_node == NULL)
		return (0);
	first = list;
	last = first->next_node;

	while (first != NULL && last->next_node != NULL
		&& last->next_node->next_node != NULL)
	{
		if (first == last)
			return (1);
		first = first->next_node;
		last = last->next_node->next_node;
	}
	return (0);
}

