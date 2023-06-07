#include "lists.h"

/**
 * insert_node - number to be inputted in sorted linked list
 * @head: header pointer
 * @number: The number to be inputted
 * Return: Null will be returned if function fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *node_check;

	node_check = malloc(sizeof(listint_t));
	if (node_check == NULL)
		return (NULL);
	node_check->num = number;

	if (node == NULL || node->num >= number)
	{
		node_check->next_node = node;
		*head = node_check;
		return (node_check);
	}

	while (node && node->next_node && node->next_node->num < number)
		node = node->next_node;

	node_check->next_node = node->next_node;
	node->next_node = node_check;

	return (node_check);
}

