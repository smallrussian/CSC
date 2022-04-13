
#include <string>
#include <vector>
#include <fstream>
#include <sstream>
#include <iterator>
#include <iostream>
using namespace std;



class Book
{
private:
	string title;
	string author;
	int checkstatus; //1 or 0 
	int importance; //unique to each book
public:
	Book()
	{
		checkstatus = 1;
	}
	Book(string newtitle, string newauthor, int newcheckstatus, int newimportance) {
		title = newtitle;
		author = newauthor;
		checkstatus = newcheckstatus;
		importance = newimportance;
	}

	string getTitle()
	{
		return title;
	}
	string getAuthor()
	{
		return author;
	}
	int getCheckStatus()
	{
		return checkstatus;
	}
	int getImportance()
	{
		return importance;
	}
	void updateStatus(int newstatus)
	{
		checkstatus = newstatus;
	}
		
};

class Node
{
public:
	Book data;
	Node* next;
	Node* left;
	Node* right;
	
	
	Node()
	{
		next = NULL;
		left = NULL;
		right = NULL;
	}
	Node(Book data)
	{
		this->data = data;
		this->next = NULL;
		this->left = NULL;
		this->right = NULL;
	}
	friend class linkedList;
};

class linkedList
{
	Node* head;
public:
	linkedList()
	{
		head = NULL;

	}
	void add(Book new_data);
	Book searchTitle(string title);
	Book searchAuthor(string author);

};
 void linkedList::add(Book data) {
	Node* newNode = new Node(data);
	newNode->data = data;
	newNode->next = NULL;

	if (head == NULL)
	{
		head = newNode;
		return;
	}
	Node* temp = head;
	while (temp->next != NULL)
	{
		temp = temp->next;
	}
	temp->next = newNode;
	return;
}
Book linkedList::searchTitle(string title)
{
	Node* current = head;
	while (current != NULL) {
		if (current->data.getTitle()==title)
		{
			return current->data;
		}
		current = current->next;
	}
}
vector<Book> read_file(string filename)
{
	fstream myfile(filename);
	string text;
	if (myfile.is_open())
	{
		vector<Book> books{};
		while (myfile)
		{
			string tempstring;

			tempstring = myfile.get();
			vector<string> tokens{};
			string token;
			stringstream ss(tempstring);
			while (getline(ss, token, ','))
			{
				tokens.push_back(token);
			}
			for (auto& tempstring : tokens) {
				cout << tempstring;
			}
			Book book(tokens[0], tokens[1], stoi(tokens[2]), stoi(tokens[3]));
			books.push_back(book);
		}
		return books;
	}
}


void open()
{

}

int main()
{
	vector<Book> books{};
	books = read_file("SciFiLiBooks.txt");
	//cout << books[1].getAuthor();
}