#include "lists.h"

/**
 * insert_node – inserts a node in sorted linked list
 * @head: head pointer in linked list
 * @num: number that will be inputted
 *
 * Return: function fails null
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node_check = *header, *node_check;

	node_check = malloc(sizeof(listint_t));
	if (node_check == NULL)
		return (NULL);
	node_check->num = number;

	if (node == NULL || next_node->num>= number)
	{
		node_check->next = next_node;
		*header = node_check;
		return (node_check);
	}

	while (next_node && next_node->next && next_node->next->num < number)
		next_node = next_node->next;

	node_check->next = next_node->next;
	next_node->next = node_check;

	return (node_check);
}

