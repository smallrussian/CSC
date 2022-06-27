#include <string>
#include <vector>
#include <fstream>
#include <sstream>
#include <iterator>
#include <iostream>
#include <tuple>
#include <istream>
#include <queue>
using namespace std;
//stores all the books values 
class Book
{
private:
	string title;
	string author;
	bool checkstatus; //true or false
	int importance; //unique to each book
	int getAuthorSize();
	int getTitleSize();
public:
	Book();
	Book(string newtitle, string newauthor, int newcheckstatus, int newimportance);
	

	string getTitle();
	string getAuthor();
	char* getAuthor(bool charindicator);
	char* getTitle(bool charindicator);
	bool getCheckStatus();
	int getImportance();
	void updateStatus();

	
	

};
//decided to throw some class inheritance in there to clean up my classes
class Node
{
protected:
	Book data;
	
};

class LinkNode : protected Node
{
protected:
	LinkNode* next;
public:
	LinkNode();
	LinkNode(Book data);
	friend class LinkedList;
	Book getData();
	LinkNode* getNext();
};

class TNode : protected Node
{
protected:
	TNode* left;
	TNode* right;
	TNode* parent;
public:
	friend class SearchTree;
	TNode();
	TNode(Book data);
	TNode* getRight();
	TNode* getLeft();
	Book getData();

};


class LinkedList
{
	LinkNode* head;
	//https://www.geeksforgeeks.org/linked-list-set-3-deleting-node/?ref=lbp
	
	void swapData(LinkNode* a, LinkNode* b);
	void sortedInsert(LinkNode* newnode, LinkNode* sorted);
	LinkNode* getTail(LinkNode* cur);
	LinkNode* partition(LinkNode* end, LinkNode** newHead, LinkNode** newEnd);
	LinkNode* partition(LinkNode* end, LinkNode** newHead, LinkNode** newEnd, bool title);
	LinkNode* quickSortRecur(LinkNode*headref,LinkNode* end);
	LinkNode* quickSortRecur(LinkNode* headref, LinkNode* end, bool title);
	void swapNodes(LinkNode** head_ref, LinkNode* currX, LinkNode* currY, LinkNode* prevY);
	


public:
	LinkedList();
	void add(Book new_data);
	Book searchTitle(string title);
	Book searchImportance(int importance);
	Book searchAuthor(string author);
	void checkCleaner();
	void insertionSort();
	void printList();
	int count();
	LinkNode* getHead();
	void quickSort();
	void quickSort(bool title);
	friend class TNode;
	friend class SearchTree;
	void deleteNode(LinkNode** headref, int importance); //deletes by importance cause its unique to each book and is easier than pointers

};

class SearchTree
{
protected:
	TNode* root;
	TNode* sortedListToBST(LinkNode* rhead, LinkedList list);
	TNode* sortedListToBSTRecursive(LinkNode** rhead, int count);
	TNode* minValueNode(TNode* node);

public:
	friend class LinkedList;
	SearchTree();
	TNode* insert(TNode* rootref, Book book);
	void deleteNode(TNode* rootref,  Book Book);
	void displayTree(TNode* node);
	void listAdd(LinkedList list);
	TNode* getRoot();
	Book searchAuthor(TNode* node, string author);
	Book searchTitle(TNode* node, string title, string author);
	Book search(TNode* rootref, Book book);
	void searchDelete(TNode*& node, Book book, TNode*& parent);


	

};
static inline void strip(std::string& s);
vector<Book> read_file(string filename);
LinkedList makeInventoryList(LinkedList list);
int compareABC(string str1, string str2);

// im using a c++ queue bc i am tired
class Librarian
{

	LinkedList masterList;
	LinkedList checkList;
	SearchTree library;
public:
	queue<Book> returnpile;
	void checkIn();
	void checkOut(Book book);
	void listAuthor();

	void listTitle();
	void searchByAuthor(string author);
	void searchByTitle(string title);
	void resuce(); //iterate through importance values with a search through the bst 
	void open(SearchTree &Library);
	void EndofDay();
};