#include <fstream>
#include <string>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector<string> read_file(string filename)
{
	fstream myfile(filename);
	string text = "";
	char qmark = '?';
	char period = '.';
	char comma = ',';
	if (myfile.is_open())
	{

		while (myfile)
		{
			string tempstring;
			tempstring = myfile.get();
			text = text + tempstring;
		}

	}

	for (int i = 0; i < text.size(); i++)
	{
		if ((text[i] == period) || (text[i] == comma) || (text[i] == qmark)) {
			text.erase(i, 1);
		}
	}
	vector<string> words{};
	size_t pos = 0;
	string space_delim = " ";
	while ((pos = text.find(space_delim)) != string::npos)
	{
		words.push_back(text.substr(0, pos));
		text.erase(0, pos + space_delim.length());
	}
	return words;
}

string capitalizeString(string s)
{
	transform(s.begin(), s.end(), s.begin(),
		[](unsigned char c) { return toupper(c); });
	return s;
}

class Word
{
private:
	string word;
	int count;
public:

	Word()
	{
		count = 0;
	}
	Word(string word)
	{
		this->word = word;
		this->count = 1;
	}
	string getWord();
	int getCount();
	void count_add();;

};

string Word::getWord()
{
	return word;
}
int Word::getCount()
{
	return count;
}
void Word::count_add()
{
	count++;
}

class Node
{
public:
	Word data;
	Node* next;
	Node() 
	{
		next = NULL;
	}
	Node(Word data) 
	{
		this->data = data;
		this->next = NULL;
	}

};





class linkedList
{
private:
	Node* head;
public:
	linkedList()
	{
		head = NULL;
		
	}
	void add(Word new_data);
	Node* search(string word);
	int getLength();
	int total();
	void output();
};

void linkedList::add(Word data) {
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

}
Node* linkedList::search(string word) {
	Node* current = head;
	while (current != NULL) {
		string str = capitalizeString(current->data.getWord());
		string newword = capitalizeString(word);
		if (str==newword)
		{
			return current;
		}
		current = current->next;
	}
	return NULL;
}
int linkedList::getLength()
{
	Node* current = head;
	int count = 0;
	while (current != NULL)
	{
		count++;
		current = current->next;
	}
	return count;
}
int linkedList::total()
{
	int total = 0;
	Node* current = head;
	while (current != NULL)
	{
		total = total + current->data.getCount();
		current = current->next;
	}
	return total;
}

void linkedList::output() {
	Node* current = head;
	while (current != NULL)
	{
		cout << current->data.getWord() << ": " << current->data.getCount() << "\n";
		current = current->next;
	}
	cout << "Creativty ratio: " << getLength() << " unique words / " << total() << " total words\n";
}




int main()
{
	linkedList list;
	int wordcount = 0;
	vector <string> wordlist;
	wordlist = read_file("paragraph.txt");
	for (auto w: wordlist)
	{
		Node *searchptr = list.search(w);
		if (searchptr!=NULL)
		{
			//cout << searchptr->data.getWord()<<" found" << endl;
			searchptr->data.count_add();
			continue;
		}
		else
		{
			//cout << "add word " << w << endl;
			Word obj(w);
			//cout << obj.getWord() << " " << obj.getCount() << endl;
			list.add(obj);
		}
	}

	list.output();
	//cout << list.getLength();
	return 0;
}