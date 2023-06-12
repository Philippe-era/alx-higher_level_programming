#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * print_listint - prints all elements linked list
 * @h: header point
 * Return: nodes present will be displayed
 */
size_t print_listint(const listint_t *h)
{
	const listint_t *current_node;
	unsigned int num;

	current_node = h;
	num = 0;

	while (current_node != NULL)
	{
		printf("%i\n", current_node->num);
		current_node = current_node->next_node;
		num++;
	}
	return (num);
}

/**
 * add_nodeint_end – new node will be added to linked list
 * @head: header pointer
 * @num: number of nodes
 * Return: new elements returned
 */
listint_t *add_nodeint_end(listint_t **head, const int num)
{
	listint_t *new_node;
	listint_t *current_node;

	current_node = *head;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	new_node->num = num;
	new_node->next_node = NULL;

	if (*head == NULL)
		*head = new_node;
	else
	{
		while (current_node->next_node != NULL)
			current_node = current_node->next_node;
		current_node->next_node = new_node;
	}
	return (new_node);
}

/**
 * free_listint – list to be freed
 * @head: freeing the pointers
 * Return: void function
 */
void free_listint(listint_t *head)
{
	listint_t *current_node;

	while (head != NULL)
	{
		current_node = head;
		head = head->next_node;
		free(current_node);
	}
}

