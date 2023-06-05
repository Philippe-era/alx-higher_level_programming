#include "lists.h"

/**
 * check_cycle - checks if a linked list contains a cycle
 * @list: list to be analyzed
 *
 * Return: 1 is success otherwise fail
 */
int check_cycle(listint_t *list)
{
	listint_t *first_check = list;
	listint_t *last_check = list;
	int fail = 0, success = 1;

	if (!list)
		return (fail);

	while (first_check && last_check && last_check->next)
	{
		first_check = first_check->next;
		last_check = last_check->next->next;
		if (first_check == last_check)
			return (success);
	}

	return (fail);
}

