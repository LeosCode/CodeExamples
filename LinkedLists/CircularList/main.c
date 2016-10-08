#include <stdio.h>
#include <stdlib.h>

#define CIRCLE_C

#include <LinkedList.h>

//#define DEBUG

//
// Determine if a linked list has a circular reference
// where a node points back to a previous node in the list.
//
// Method is to have a fast and slow advancing pointer.
// If the fast pointer ever matches the slow pointer
// then the list is circular.
//
// method takes min = n * 1.5 max = n * 3 for O(n * 3)
//
// Return 1 if circular or 0 if not
#undef __FN__
#define __FN__ "determineCircular"
int determineCircular( tIntElement *head)
{
	//
	// There are fast and a slow advance pointers
	//
	tIntElement *fast, *slow;
	int slowCount, fastCount;
	//
    printf("\nDetermine if list is circular.");
    //
    // Check if the list is empty or only has one node
    //
	if( NULL == head || NULL == head->next )
	{
		printf("\nList is empty.");
			return 0;      // Not a circular list
	}
	//
	// Point slow pointer to the head of the list
	// Point the fast pointer ahead of the slow pointer
	slow = head;
	slowCount = 0;
	fast = head->next;
	fastCount = 1;
	//
	// Loop over the list
	//
	while(1)
	{
		#ifdef DEBUG
		printf("\nslow%d %0X != fast%d %0X", slowCount, slow, fastCount, fast );
		#endif
		//
		// If the fast pointer or it's next node are the end of the list
		// then the list is not circular
		//
		if( NULL == fast || NULL == fast->next )
		{
			printf("\n%d list comparisions.", fastCount + slowCount);
			return 0;   // End of list. Not a circular list.
		}
		//
		// If the fast pointer or it's next node have reached the
		// slow pointer then the list has wrapped around.
		//
		if( fast == slow || fast->next == slow )
		{
			#ifdef DEBUG
			if( fast == slow )
				printf("\nslow%d %0X = %0X fast%d = %0X", slowCount, slow, fastCount, fast);
			else
				printf("\nslow%d = %0X fast%d = %0X", slowCount, slow, fastCount, fast->next);
			#endif
			printf("\n%d list comparisions.", fastCount + slowCount);
		 	return 1;   // Repeat pointer before end of list. Circular list.
		}
		//
		// Advance the fast pointer by two nodes
		//
		fast = fast->next;
		fast = fast->next;
		fastCount +=2;
		//
		// Advance the slow pointer by one node
		//
		slow = slow->next;
		slowCount += 1;
	}
}
//
//
//
#undef __FN__
#define __FN__ "main//"
int main(int argc, char *argv[])
{
	tIntElement *linkedList;					// head of list pointer
    int i = 0;
    //
    // First make a regular list
    // but save node locations to make it circular later
    //
    tIntElement	*middle, *tail;
    linkedList = NULL;	// no entries in the list yet
	//
    insertFront( &linkedList, 1 );
    tail = linkedList;
	//
#ifdef NEVER
    for( i = 2; i < 6; ++i )
    {
        insertFront( &linkedList, i );
    }
    middle = linkedList;     // Save location half way through the list
#endif
    for( ; i <= 10; ++i )
    {
    	insertFront( &linkedList, i );
    }
    middle = linkedList;     // Save location in the list
    printList( &linkedList);
	//
	//
	//
    if( determineCircular( linkedList ) )
    	printf("\nList is circular.");
    else
    	printf("\nList is not circular.");
	//
	//
	//
    tail->next = middle;      // Make the last element point to the first element
    printf("\nMake tail of list point to head.");
    printf("\n%0X -> %0X", tail, middle);
	//
	//
	//
    if( determineCircular( linkedList ) )
      printf("\nList is circular.");
    else
      printf("\nList is not circular.");

    printf("\n");
    system("pause");
    return 0;
}
