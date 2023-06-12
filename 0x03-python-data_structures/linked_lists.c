#include "lists.h"


  return (number);
}

/**
 * add_nodeint_end – node added to list 
 * @head: header pointer
 * @n: number of nodes
 * Return: if added to list pass , otherwise fail
 */
listint_t *add_nodeint_end(listint_t **head, const int n)
{
  listint_t *new_node;
  listint_t *current_node;

  current_node = *head;

  new_node = malloc(sizeof(listint_t));
  if (new_node == NULL)
    return (NULL);

  new_node->n = n;
  new_node->next = NULL;

  if (*head == NULL)
    *head = new_node;
  else
    {
      while (current_node->next != NULL)
	current_node = current_node->next;
      current_node->next = new_node;
    }

  return (new_node);
}

/**
 * print_listint – all elements to be printed
 * @h: header pointer
 * Return: counts numbers of nodes
 */
size_t print_listint(const listint_t *h)
{
  const listint_t *current_node;
  unsigned int number;

  current_node = h;
  number = 0;
  while (current_node != NULL)
    {
      printf("%i\n", current_node->number);
      current_node = current_node->next;
      number++;
    }

/**
 * free_listint – sets free the linked list
 * @head: pointer to be set free
 * Return: void
 */
void free_listint(listint_t *head)
{
  listint_t *current_node;

  while (head != NULL)
    {
      Current_node = head;
      head = head->next;
      free(current_node);
    }
}


