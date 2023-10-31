#include "lists.h"
/**
 * check_cycle - this checks a list for a cycle
 * @list: the list tobe checked
 * Return: returns 1.
 */
int check_cycle(listint_t *list)
{
	listint_t *fast, *slow;

	if (list == NULL || list->next == NULL)
    {
        return (0);
    }
	fast = list;
	slow = list;
	while (slow != NULL && fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
		    return (1);
	}
	return (0);
}
