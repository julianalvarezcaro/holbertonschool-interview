#include "lists.h"

/**
 * insert_node - inserts a node with a given number into a sorted linked list
 *
 * @head: pointer to the first node of the linked list
 * @number: Number that will be inserted in the linked list
 *
 * Return: Pointer to the new node. NULL if failed to add
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *curr, *next, *new;

	if (head == NULL || *head == NULL)
		return (NULL);

	if (number < (*head)->n)
	{
		new = malloc(sizeof(listint_t));
		if (new == NULL)
			return (NULL);
		new->n = number;
		new->next = *head;

		*head = new;

		return (new);
	}

	curr = *head;
	next = (*head)->next;

	while (next)
	{
		if (next->n > number)
			break;
		curr = next;
		next = curr->next;
	}

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	curr->next = new;
	new->next = next;
	return (new);
}
