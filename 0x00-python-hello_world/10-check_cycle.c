#include "lists.h"
/**
 * check_cycle - checks if there is a cycle or not
 * @list: list linked to be analyzed
 * Return: 1 if success , 0 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	if (!list)
		return (0);

	while (slow && fast && fast->next_node)
	{
		slow = slow->next_node;
		fast = fast->next_node->next_node;
		if (slow == fast)
			return (1);
	}

	return (0);
}

