#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct listint_s - linked list ( single)
 * @num: integer
 * @next_node: points to the next node
 * Description: prototypes needed for the task of the day
 */
typedef struct listint_s
{
	int num;
	struct listint_s *next_node;
} listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint_end(listint_t **head, const int n);
void free_listint(listint_t *head);
listint_t *insert_node(listint_t **head, int number);

#endif 

