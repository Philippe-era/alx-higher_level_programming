#ifndef LISTS_H
#define LISTS_H

#include <stdio.h>
#include <stdlib.h>

/**
 * struct listint_s – linked list
 * @num: number to be evulated
 * @next: next node pointed too
 * Description: linked single list
 */
typedef struct listint_s
{
	int num;
	struct listint_s *next_node;
} listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint_end(listint_t **head, const int n);
void free_listint(listint_t *head);
int is_palindrome(listint_t **head);

#endif

