/*Q93: Check if two strings are anagrams of each other.
Sample Test Cases:
Input 1:
listen
silent
Output 1:
Anagrams

Input 2:
hello
world
Output 2:
Not anagrams
*/
#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main()
{
    string s, h;
    cin >> s >> h;
    if (s.length() != h.length())
    {
        cout << "Not anagrams" << endl;
        return 0;
    }
    sort(s.begin(), h.end());
    sort(s.begin(), h.end());
    if (s == h)
        cout << "Analgrams " << endl;
    else
        cout << "Not analgrams" << endl;
    return 0;
}
