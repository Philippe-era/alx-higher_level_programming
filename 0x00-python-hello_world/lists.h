#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct listint_s – single linked list node
 * @number: the number data type interger to be evualated
 * @next_node: goes to the next node
 * Description: Python task number 1.
 */
typedef struct listint_s
{
	int number;
	struct listint_s *next_node;
} listint_t;

size_t print_listint(const listint_t *h);
int check_cycle(listint_t *list);
void free_listint(listint_t *head);
listint_t *add_nodeint(listint_t **head, const int number);


#endif /* LISTS_H */

