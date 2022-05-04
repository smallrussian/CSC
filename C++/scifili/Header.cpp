#include <string>
#include <vector>
#include <istream>
#include <sstream>
#include <iterator>
#include <iostream>
#include <tuple>
#include "Header.h"
#include <fstream>
#include <algorithm>

using namespace std;
Book::Book()
{
	checkstatus = false;
	importance = 0;
}
Book::Book(string newtitle, string newauthor, int newcheckstatus, int newimportance)
{
	title = newtitle;
	author = newauthor;
	checkstatus = newcheckstatus;
	importance = newimportance;
}
string Book::getTitle()
{
	return title;
}
int Book::getTitleSize()
{
	return title.size();
}

string Book::getAuthor()
{
	return author;
}
int Book::getAuthorSize()
{
	return author.size();
}
 char* Book::getAuthor(bool charinidcator)
{
	char* char_arr;
	string str_obj(author);
	char_arr = &str_obj[0];
	return char_arr;
}
 char* Book::getTitle(bool charindicator)
 {
	 char* char_arr;
	 string str_obj(title);
	 char_arr = &str_obj[0];
	 return char_arr;
 }
bool Book::getCheckStatus()
{
	return checkstatus;
}
int Book::getImportance()
{
	return importance;
}
void Book::updateStatus(int newstatus)
{
	checkstatus = newstatus;
}


TNode::TNode()
{
	left = NULL;
	right = NULL;
	parent = NULL;
}
TNode::TNode(Book newdata)
{
	this->data = newdata;
	this->left = this->right = NULL;
}

int LinkedList::count()
{
	int count = 0;
	LinkNode* temp = head;
	while (temp)
	{
		temp = temp->next;
		count++;
	}
	return count;
}


void LinkedList::deleteNode(int importance)
{
	LinkNode* current = head;
	LinkNode* prev = NULL;
	if (current != NULL && current->data.getImportance() == importance)
	{
		 head= current->next;
		 delete current;
		 return;
	}
	else
	{
		while (current == NULL && current->data.getImportance() != importance)
		{
			prev = current;
			current = current->next;
		}
		
	}
}


LinkedList::LinkedList()
{
	head = NULL;
}
//i would have had a void function but i wanted it to return NULL 
TNode* SearchTree::sortedListToBSTRecursive(LinkNode** rhead, int count)
{
	if (count <= 0)
		return NULL;
	//constructs the left subtree, recusively
	TNode* left = sortedListToBSTRecursive(rhead, count / 2);

	TNode* root = new TNode((* rhead)->getData());
	root->left = left;
	*rhead = (*rhead)->getNext();

	root->right = sortedListToBSTRecursive(rhead, count - count / 2 - 1);
	
	return root;

	
	
}

SearchTree::SearchTree()
{
	root = NULL;
}

void SearchTree::displayTree(TNode* node)
{
	if (node == NULL)
		return;
	cout << node->data.getTitle() << ", " << node->data.getAuthor() << ", checked in: " << boolalpha << node->data.getCheckStatus() << endl;
	displayTree(node->left);
	displayTree(node->right);
}




TNode* SearchTree::sortedListToBST(LinkNode* rhead, LinkedList list)
{
	int count = list.count();
	return sortedListToBSTRecursive(&rhead, count);

}

TNode* SearchTree::getRoot()
{
	return this->root;
}
Book SearchTree::search(TNode* node,string author)
{
	if (root == NULL || root->data.getAuthor() == author)
		return root->data;
	if (compareABC(root->data.getAuthor(), author) == 2)
		return (search(root->right, author));
	return search(root->left, author);
}

Book SearchTree::search(TNode* node, string title)
{
	if (root == NULL || root->data.getTitle() == title)
		return root->data;
	if (compareABC(root->data.getTitle(), title) == 2)
		return (search(root->right, title));
	return search(root->left, title);
}
void LinkedList::add(Book book) {
	LinkNode* newNode = new LinkNode(book);
	newNode->data = book;
	newNode->next = NULL;

	if (head == NULL)
	{
		head = newNode;
		return;
	}
	LinkNode* temp = head;
	while (temp->next != NULL)
	{
		temp = temp->next;
	}
	temp->next = newNode;
	return;
}
Book LinkedList::searchTitle(string title)
{
	LinkNode* current = head;
	while (current != NULL)
	{
		if (current->data.getTitle() == title)
		{
			return current->data;
		}
		current = current->next;
	}
}

void SearchTree::add(LinkedList list)
{
	this->root = sortedListToBST(list.getHead(), list);
	return;
}

vector<Book> LinkedList::searchAuthor(string author)
{
	LinkNode* current = head;
	vector<Book> books;
	while (current != NULL)
	{

		if (current->data.getAuthor() == author)
		{
			
			Book book = current->data;

			books.push_back(book);
		}
		current = current->next;
	}
	return books;
}
void LinkedList::checkCleaner()
{
	LinkNode* current = head;
	while (current != NULL)
	{
		if (current->data.getCheckStatus() == false)
		{
			LinkNode* prev = current;
			current = current->next;
			deleteNode(prev->data.getImportance());
		}
	}

}


void LinkedList::swapData(LinkNode* a, LinkNode* b)
{
	Book temp = a->data;
	a->data = b->data;
	b->data = temp;
}
void LinkedList::printList()
{
	LinkNode* current = head;
	while (current)
	{
		cout << current->data.getAuthor()<<endl;
		cout << current->data.getTitle()<<endl;
		cout << current->data.getImportance()<<endl;
		cout<<boolalpha<< current->data.getCheckStatus() << endl;
		current = current->next;
	}
}
LinkNode* LinkedList::getHead()
{
	return head;
}
void LinkedList::quickSort()
{
	quickSortRecur(head,getTail(head));
}
void LinkedList::insertionSort()
{
	LinkNode* sorted = NULL;
	LinkNode* current = head;
	while (current != NULL)
	{
		LinkNode* next = current->next;
		sortedInsert(current, sorted);
		current = next;

	}

}
void LinkedList::sortedInsert(LinkNode* newnode, LinkNode* sorted)
{
	/* Special case for the head end */
	int strcomp = strcmp(sorted->data.getAuthor(true), newnode->data.getAuthor(true));
	if (sorted == NULL || strcomp >= 0) {
		newnode->next = sorted;
		sorted = newnode;
	}
	else
	{
		LinkNode* current = sorted;
		/* Locate the node before the point of insertion
		 */
		while (current->next != NULL
			&& strcmp(current->next->data.getAuthor(true), newnode->data.getAuthor(true)) < 0) 
		{//			&& current->next->val < newnode->valstrcmp() {

			current = current->next;
		}
		newnode->next = current->next;
		current->next = newnode;
	}

}

LinkNode* LinkedList::getTail(LinkNode* cur)
{
	while (cur != NULL && cur->next == NULL)
		cur = cur->next;
	return cur;
}

LinkNode* LinkedList::partition(LinkNode* end, LinkNode** newHead, LinkNode** newEnd)
{
	LinkNode* pivot = end;
	LinkNode* prev = NULL, * cur = head, * tail = pivot;


	while (cur != pivot)
	{
		int result = strcmp(cur->data.getAuthor(true), pivot->data.getAuthor(true));
		if (compareABC(cur->data.getAuthor(),pivot->data.getAuthor())==2)
		{
			if ((*newHead) == NULL)
				(*newHead) = cur;

			prev = cur;
			cur = cur->next;
		}
		else
		{
			if (prev)
				prev->next = cur->next;
			LinkNode* tmp = cur->next;
			cur->next = NULL;
			tail->next = cur;
			tail = cur;
			cur = tmp;
		}
	}
	if ((*newHead) == NULL)
		(*newHead) = pivot;

	(*newEnd) = tail;
	return pivot;
}

LinkNode* LinkedList::quickSortRecur(LinkNode* headRef,LinkNode* end)
{
	//base condition
	if (!head || head == end)
		return head;
	LinkNode* newHead = NULL, *newEnd = NULL;

	LinkNode* pivot
		= partition(head, &newHead, &newEnd);

	if (newHead != pivot)
	{
		LinkNode* tmp = newHead;
		while (tmp->next != pivot)
			tmp = tmp->next;
		tmp->next = NULL;

		newHead = quickSortRecur(newHead, tmp);

		tmp = getTail(newHead);
		tmp->next = pivot;
		
		
	} 
	pivot->next = quickSortRecur(pivot->next, newEnd);
	return newHead;
}
	
//python.strip() equavilent at beginning, for author
//https://www.codegrepper.com/code-examples/cpp/c%2B%2B+strip+white+space+from+string

// trim from start (in place)
static inline void strip(string& s) {
	s.erase(s.begin(), find_if(s.begin(), s.end(), [](unsigned char ch) {
		return !isspace(ch);
		}));
}
vector<Book> read_file(string filename)
{
	string tempstring;

	string text;
	vector<Book> books{};
	ifstream myfile(filename);
	if (!myfile.is_open())
	{
		cerr << "Could not open the file" << filename << endl;
	}
	while (getline(myfile, tempstring))

	{
		//cout << tempstring<<endl;
		vector<string> tokens{};
		string token;
		stringstream ss(tempstring);
		while (getline(ss, token, ','))
		{
			tokens.push_back(token);
		}
		bool checkbool;
		if (stoi(tokens[2]) == 1)
			checkbool = true;
		else
		{
			checkbool = false;
		}
		strip(tokens[1]);
		Book book(tokens[0], tokens[1], checkbool, stoi(tokens[3]));
		books.push_back(book);
	}
	return books;
	
}




LinkNode::LinkNode()
{
	next = NULL;
}

LinkNode::LinkNode(Book data)
{
	this->data = data;
}

Book LinkNode::getData()
{
	return this->data;
}

LinkNode* LinkNode::getNext()
{
	return next;
}

LinkedList makeInventoryList(LinkedList list)
{
	LinkedList newlist;
	LinkNode* current = list.getHead();
	while (current)
	{
		Book book;
		book = current->getData();
		if (book.getCheckStatus() == true)
			newlist.add(book);
		current = current->getNext();
	}
	return newlist;
}
int compareABC(string str1, string str2)
{
	for (int i = 0; i < str1.length() && i < str2.length(); i++)
	{
		if (str1[i] == str2[i])
		{
			i++;
		}
		else if (str1[i] > str2[i])
			return 1;
		else
			return 2;
	}
	return 3;
}

void LinkedList::swapNodes(LinkNode** head_ref,
	LinkNode* currX,
	LinkNode* currY, LinkNode* prevY)
{
	// make 'currY' as new head
	*head_ref = currY;

	// adjust links
	prevY->next = currX;

	// Swap next pointers
	LinkNode* temp = currY->next;
	currY->next = currX->next;
	currX->next = temp;
}

// function to sort the linked list using
// recursive selection sort technique
LinkNode* LinkedList::recurSelectionSort(LinkNode* head)
{
	// if there is only a single node
	if (head->next == NULL)
		return head;

	// 'min' - pointer to store the node having
	// minimum data value
	LinkNode* min = head;

	// 'beforeMin' - pointer to store node previous
	// to 'min' node
	LinkNode* beforeMin = NULL;
	LinkNode* ptr;

	// traverse the list till the last node
	for (ptr = head; ptr->next != NULL; ptr = ptr->next) {

		// if true, then update 'min' and 'beforeMin'
		if (compareABC(ptr->next->data.getAuthor() , min->data.getAuthor())==1) {
			min = ptr->next;
			beforeMin = ptr;
		}
	}

	// if 'min' and 'head' are not same,
	// swap the head node with the 'min' node
	if (min != head)
		swapNodes(&head, head, min, beforeMin);

	// recursively sort the remaining list
	head->next = recurSelectionSort(head->next);

	return head;
}

// function to sort the given linked list
void LinkedList::sort()
{
	// if list is empty
	if ((head) == NULL)
		return;

	// sort the list using recursive selection
	// sort technique
	head = recurSelectionSort(head);
}