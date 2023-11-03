#include "lists.h"

listint_t *create_node(int n);
/**
 * insert_node - function puts node into a list of ints
 * @head: pointer to head.
 * @num:item tobe added
 * Return:returns  pointer to newly created node, NULL on failure
 */
listint_t *insert_node(listint_t **head, int num)
{
	listint_t *current = NULL;
	listint_t *nn = NULL;

	if (head == NULL)
	{
		return (NULL);
	}
	else if (!(*head))
	{
		nn = create_node(num);
		*head = nn;
		return (nn);
	}
	current = *head;
	while (current)
	{
		if (current->n >= num)
		{
			nn = create_node(num);
			nn->next = current;
			*head = nn;
			return (nn);
		}
		else if (current->n <= num)
		{
			if (!current->next || current->next->n >= num)
			{
				nn = create_node(num);
				nn->next = current->next;
				current->next = nn;
				return (current->next);
			}
		}
		current = current->next;
	}
	return (NULL); 
}
/**
 * create_node - func creates new node
 * @n: item tobe added
 *
 * Return: returns pter to newly allocated node
 */
listint_t *create_node(int n)
{
	listint_t *ter = NULL;

	ter = malloc(sizeof(listint_t));
	if (ter == NULL)
	{
		return (NULL);
	}
	ter->next = NULL;
	ter->n = n;
	return (ter);
}
