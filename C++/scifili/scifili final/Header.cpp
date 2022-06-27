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
#include <queue>


//theres a lot of linkes for this
// but plenty of this came from geeks for geeks, iu did have to adapt it all to work with my classes 
using namespace std;
//default constructor for book class 
Book::Book()
{
	checkstatus = false;
	importance = 0;
}
//paramterized contstructor for book class 
Book::Book(string newtitle, string newauthor, int newcheckstatus, int newimportance)
{
	title = newtitle;
	author = newauthor;
	checkstatus = newcheckstatus;
	importance = newimportance;
}
//title accessor
string Book::getTitle()
{
	return title;
}
// length accessor
int Book::getTitleSize()
{
	return title.size();
}
//author accessor
string Book::getAuthor()
{
	return author;
}
//authoir length acccessor
int Book::getAuthorSize()
{
	return author.size();
}
//returns a char array for author (i dont think its used)
 char* Book::getAuthor(bool charinidcator)
{
	char* char_arr;
	string str_obj(author);
	char_arr = &str_obj[0];
	return char_arr;
}
 //returns a char array for title (i dont htink its used)
 char* Book::getTitle(bool charindicator)
 {
	 char* char_arr;
	 string str_obj(title);
	 char_arr = &str_obj[0];
	 return char_arr;
 }
 //returns if the book is checked in or not 
bool Book::getCheckStatus()
{
	return checkstatus;
}
//returns the importance
int Book::getImportance()
{
	return importance;
}
//changes the check status
void Book::updateStatus()
{
	if (checkstatus == false)
		checkstatus = true;
	else
		checkstatus = false;
}

//TreeNode default cosntructor 
TNode::TNode()
{
	left = NULL;
	right = NULL;
	parent = NULL;
}
//TreeNode paramterized cosntructor 
TNode::TNode(Book newdata)
{
	data = newdata;
	this->left = this->right = NULL;
}
//returns node data 
Book TNode::getData()
{
	return data;
}
//returns right node 
TNode* TNode::getRight()
{
	return right;
}
//returns left node 
TNode* TNode::getLeft()
{
	return left;
}
//returns linked list length 
int LinkedList::count()
{
	int count = 0;
	LinkNode* temp = head;
	while (temp!=NULL)
	{
		temp = temp->next;
		count++;
	}
	return count;
}

//deletes node from linked list 
void LinkedList::deleteNode(LinkNode** headref,int importance)
{
	LinkNode* current = *headref;
	LinkNode* prev = NULL;
	if (current != NULL && current->data.getImportance() == importance)
	{
		 *headref = current->next;
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

//linked list default constructor 
LinkedList::LinkedList()
{
	head = NULL;
}
//reescursive internal function to sort a linked list into a Binary Search Tree
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

//finds the minimunm node in the tree 
TNode* SearchTree::minValueNode(TNode* node)
{
	TNode* current = node;

	while (current && current->left != NULL)
		current = current->left;
	return current;
}
//default constructor for Binary Search Tree 
SearchTree::SearchTree()
{
	root = NULL;
}
//displays the tree in order 
void SearchTree::displayTree(TNode* node)
{
	if (node == NULL)
		return;
	cout << node->data.getTitle() << ", " << node->data.getAuthor() << ", checked in: " << boolalpha << node->data.getCheckStatus() << endl;
	displayTree(node->left);
	displayTree(node->right);
}



//turns a sorted linked list int oa binary search tree 
TNode* SearchTree::sortedListToBST(LinkNode* rhead, LinkedList list)
{
	int count = list.count();
	return sortedListToBSTRecursive(&rhead, count);

}
//returns the root of the bST
TNode* SearchTree::getRoot()
{
	return this->root;
}
//searches for a book by author 
Book SearchTree::searchAuthor(TNode* node,string author)
{
	if (root == NULL || root->data.getAuthor() == author)
		return root->data;
	if (compareABC(root->data.getAuthor(), author) == 2)
		return (searchAuthor(root->right, author));
	return searchAuthor(root->left, author);
}
//searches for a book by title 
Book SearchTree::searchTitle(TNode* node, string title, string author)
{
	if (root == NULL || root->data.getTitle() == title)
		return root->data;
	if (compareABC(root->data.getAuthor(), author) == 2)
		return (searchTitle(root->right, title, author));
	return searchTitle(root->left, title, author);
}
//plain search for a book, by importance cause its unique 
Book SearchTree::search(TNode* rootref, Book book)
{
	if (rootref == NULL || rootref->data.getImportance() == book.getImportance())
		return rootref->data;

	if (compareABC(rootref->data.getAuthor(), book.getAuthor()) == 2)
		return search(rootref->right, book);
	return search(root->left, book);
}

//the search used for deleting a node 
void SearchTree::searchDelete(TNode*& node, Book book, TNode*& parent)
{
	while (node != NULL && node->data.getImportance() != book.getImportance())
	{
		parent = node;

		if (compareABC(book.getAuthor(), node->data.getAuthor()) == 2)
			node = node->left;
		else
			node = node->right;
	}
}


//adds a node to a linked list 
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
//searchs the linked list by title 
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
//searchs the linkedlist by importance 
Book LinkedList::searchImportance(int importance)
{
	LinkNode* current = head;
	while (current != NULL)
	{
		if (current->data.getImportance() == importance)
			return current->data;
	}
	current = current->next;
}
//actual sorted list conversion 
void SearchTree::listAdd(LinkedList list)
{
	root = sortedListToBST(list.getHead(), list);
	return;
}
//returns a node so it can be recursive
//inserts a node into the tree 
TNode* SearchTree::insert(TNode* rootref, Book book)
{
	if (!rootref)
		return new TNode(book);
	
	if (compareABC(book.getAuthor(), rootref->data.getAuthor()) == 1)
		rootref->right;
	else
		rootref->left = insert(rootref->left, book);

	return rootref;
}
//https://www.techiedelight.com/deletion-from-bst
void SearchTree::deleteNode(TNode* rootref, Book book)
{
	TNode* parent = NULL;
	TNode* current = root;
	searchDelete(current,book,parent);
	if (current == NULL)
		return;
	//case 1 
	if (current->left == NULL && current->right == NULL)
	{
		if (current != rootref)
		{
			if (parent->left = current)
				parent->left = NULL;
			else
				parent->right = NULL;
		}
		else
			rootref = NULL;
		free(current);

	}
	//case 2
	else if (current->left && current->right)
	{
		TNode* successor = minValueNode(current->right);
		Book newbook = successor->data;
		deleteNode(rootref, successor->data);

		current->data = newbook;
	}
	//case 3
	else {
		TNode* child = (current->left) ? current->left : current->right;

		if (current != rootref)
		{
			if (current == parent->left)
				parent->left = child;
			else
				parent->right = child;
		}

		else
			rootref = child;

		free(current);
	}
	

	

}
//searches the linked list by author 
Book LinkedList::searchAuthor(string author)
{
	LinkNode* current = head;
	while (current != NULL)
	{

		if (current->data.getAuthor() == author)
		{
			
			return current->data;
		}
		current = current->next;
	}
}
//cleans the list of unchecked books, 
void LinkedList::checkCleaner()
{
	LinkNode* current = head;
	while (current != NULL)
	{
		if (current->data.getCheckStatus() == false)
		{
			LinkNode* prev = current;
			current = current->next;
			deleteNode(&head,prev->data.getImportance());
		}
	}

}

//swaps nodes (not sure if its used or not)
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
		Book book = current->data;
		cout << book.getTitle() << "written by: " << book.getAuthor() << "checked in: " << boolalpha << book.getCheckStatus();
		current = current->next;
	}
}
//returns list head 
LinkNode* LinkedList::getHead()
{
	return head;
}
//sorts a linked list by author 
void LinkedList::quickSort()
{
	quickSortRecur(head,getTail(head));
}
//sorts alinked list by title 
void LinkedList::quickSort(bool title)
{
	quickSortRecur(head, getTail(head), title);
}
//uselss insertion sort i forgot to delete 
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
//more useless insertion sort 
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
//returns the tail of the lsit 
LinkNode* LinkedList::getTail(LinkNode* cur)
{
	while (cur != NULL && cur->next == NULL)
		cur = cur->next;
	return cur;
}
//used to comparare valused when sorting 
LinkNode* LinkedList::partition(LinkNode* end, LinkNode** newHead, LinkNode** newEnd)
{
	LinkNode* pivot = end;
	LinkNode* prev = NULL, * cur = head, * tail = pivot;


	while (cur != pivot)
	{
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
//partition but for a title 
LinkNode* LinkedList::partition(LinkNode* end, LinkNode** newHead, LinkNode** newEnd, bool title)
{
	LinkNode* pivot = end;
	LinkNode* prev = NULL, * cur = head, * tail = pivot;


	while (cur != pivot)
	{
		if (compareABC(cur->data.getTitle(), pivot->data.getTitle()) == 2)
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
//internal recursive function for quick sort
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
//quickSortRecur for title 
LinkNode* LinkedList::quickSortRecur(LinkNode* headRef, LinkNode* end, bool title)
{
	//base condition
	if (!head || head == end)
		return head;
	LinkNode* newHead = NULL, * newEnd = NULL;

	LinkNode* pivot
		= partition(head, &newHead, &newEnd, title);

	if (newHead != pivot)
	{
		LinkNode* tmp = newHead;
		while (tmp->next != pivot)
			tmp = tmp->next;
		tmp->next = NULL;

		newHead = quickSortRecur(newHead, tmp, title);

		tmp = getTail(newHead);
		tmp->next = pivot;


	}
	pivot->next = quickSortRecur(pivot->next, newEnd, title);
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
//function to read afile into a vector of books 
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
	myfile.close();
	return books;
	
}



//linked list node default  constructor 
LinkNode::LinkNode()
{
	next = NULL;
}
//linked list node parameteized cosntructor
LinkNode::LinkNode(Book data)
{
	this->data = data;
}
//returns node data 
Book LinkNode::getData()
{
	return data;
}
//returns the "next" pointer
LinkNode* LinkNode::getNext()
{
	return next;
}
//makes the list of chcekded in books 
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
//compares strings alphebtically
int compareABC(string str1, string str2)
{
	if (str1 == str2)
		return 3;
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
}
//swap nodes again (not sreally sure if it used, cant remember what web page i got this from)
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


// function to sort the given linked list


//end of day function for librarian 
void Librarian::EndofDay()
{
	fstream file;
	file.open("opengenus_test.txt", ios::out | ios::app);
	LinkedList titleList = masterList;
	titleList.quickSort(true);
	LinkNode* current = titleList.getHead();
	while (current != NULL)
	{
		file << current->getData().getTitle() << ", checked in: " << boolalpha << current->getData().getTitle() << endl;
		current = current->getNext();
	}
	return;
}

//checks in books from the return pile, which is a queue 
void Librarian::checkIn()
{
	int size = returnpile.size();
	for (int i = 0; i < size; i++)
	{
		Book book = returnpile.front();
		masterList.searchImportance(book.getImportance()).updateStatus();
		book.updateStatus();
		checkList.add(book);
		library.insert(library.getRoot(), book);
	}
}
//checks out books 
void Librarian::checkOut(Book book)
{
	masterList.searchImportance(book.getImportance()).updateStatus();
	LinkNode* checkHead = checkList.getHead();
	checkList.deleteNode(&checkHead, book.getImportance());
	library.deleteNode(library.getRoot(), book);

}
//lists books by author 
void Librarian::listAuthor()
{
	masterList.quickSort();
	masterList.printList();
}
//lists books by title 
void Librarian::listTitle()
{
	LinkedList titleList = masterList;
	titleList.quickSort(true);
	titleList.printList();
}
//searches by author 
void Librarian::searchByAuthor(string author)
{
	vector<Book> books;
	for (int i=0;i<masterList.count();i++)
	{
		
		Book book = masterList.searchAuthor(author);
		//https://www.codegrepper.com/code-examples/cpp/check+i++an+element+is+not+in+a+vector+c%2B%2B
		for (auto& libre : books)
		{
			if (libre.getImportance() == book.getImportance())
				continue;
			else
				books.push_back(book);
		}
		
			
	}
	cout << "Books by: " << author << endl;
	for (auto& book : books)
	{
		cout << book.getTitle() << boolalpha << endl;
	}
		
}
//searchs by title 
void Librarian::searchByTitle(string title)
{
	Book book = masterList.searchTitle(title);
	cout << book.getTitle() << ", written by: " << book.getAuthor() << ", checked in: " << boolalpha << book.getCheckStatus() << endl;
	
		
}
//opens the library 
void Librarian::open(SearchTree& library)
{
	vector<Book>books;
	books = read_file("SciFiLiBooks.txt");
	for (auto& book : books)
	{
		masterList.add(book);
	}
	checkList = makeInventoryList(masterList);
	checkList.quickSort();
	library.listAdd(checkList);

}
//rescuses books in case of fire 
void Librarian::resuce()
{
	vector<Book> rescue;
	for (int i = 1; i <= checkList.count(); i++)
	{
		Book book = checkList.searchImportance(i);
		library.deleteNode(library.getRoot(), book);
		rescue.push_back(book);
	}
}