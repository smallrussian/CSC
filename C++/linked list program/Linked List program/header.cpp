#include <iostream>
#include <string>
#include <fstream>

#include <vector>
using namespace std;




 string read_file(string filename)
{
	fstream myfile(filename);
	string mystring ="";
	char qmark = '?';
	char period = '.';
	char comma = ',';
	if (myfile.is_open())
	{
		
		while (myfile)
		{
			string tempstring;
			tempstring = myfile.get();
			mystring = mystring + tempstring;
		}

	}
	
	for (int i = 0; i < mystring.size(); i++)
	{
		if ((mystring[i] == period) || (mystring[i] == comma) || (mystring[i] == qmark)) {
			mystring.erase(i, 1);
		}
	}
	return mystring;
}



	




linkedList::linkedList() 
{
	head = NULL;
	tail = NULL;

void linkedList::add(Word new_data, int key) {
	Node* temp = new Node;
	temp->data = new_data;
	temp->key = key;
	temp->next = NULL;
	if (head == NULL)
	{
		head = temp;
		tail = temp;
	}
	else
	{
		tail->next = temp;
		tail = tail->next;
	}
}

Word linkedList::search(int index) {
	Node* current = head;
	while (current != NULL) {
		if (current->key==index) 
		{
			return current->data;
		}
		current = current->next;

	}



}

int linkedList::count()
{
	int counter=0;
	Node* p = head;
	while (p != NULL)
	{
		counter++;
		p++;
	}
	return counter;
}
