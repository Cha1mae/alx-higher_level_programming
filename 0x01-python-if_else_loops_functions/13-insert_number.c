#include "lists.h"
#include <stddef.h>
#include <stdlib.h>

/**
 * insert_sorted_node - Inserts a num into a sorted singly-linked list.
 * @head: A pointer to the head of the linked list.
 * @number: The number to insert into the list
 *
 * Return: If the function fails - NULL.
 * Otherwise - a pointer to the newly inserted node.
 */
listint_t *insert_sorted_node(listint_t **head, int number)
{
    listint_t *current = *head, *new_node;

    new_node = malloc(sizeof(listint_t));
    if (new_node == NULL)
        return (NULL);
    new_node->n = number;

    if (current == NULL || current->n >= number)
    {
        new_node->next = current;
        *head = new_node;
        return (new_node);
    }

    while (current && current->next && current->next->n < number)
        current = current->next;

    new_node->next = current->next;
    current->next = new_node;

    return (new_node);
}
