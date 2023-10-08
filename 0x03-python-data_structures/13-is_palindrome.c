#include "lists.h"

/**
 * is_palindrome - function to call if_palin to see if list is palindrome
 * @head: head of the list
 * Return: 0 if it's not a palindrome
 * 1 if it is a palindrome
**/

int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return (1);
	return (if_palin(head, *head));
}

/**
 * if_palin - function to check if the list is palindrome
 * @head: ptr to the beginning of the list
 * @last: ptr to the end of the list
 * Return: 0 if not palindrom else 1
 */
int if_palin(listint_t **head, listint_t *end)
{
	if (end == NULL)
		return (1);
	if (if_palin(head, end->next) && (*head)->n == end->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}
