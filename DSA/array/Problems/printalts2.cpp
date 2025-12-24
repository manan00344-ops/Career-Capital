/*
Input: arr[] = [10, 20, 30, 40, 50]
Output: 10 30 50
Explanation: Print the first element (10), skip the second element (20), print the third element (30), skip the fourth element(40) and print the fifth element(50).

Input: arr[] = [-5, 1, 4, 2, 12]
Output: -5 4 12
*/
// Iterate C++ Program to print alternate elements
// of the array

// Recursive C++ Program to print alternate elements
// of the array

#include <iostream>
#include <vector>
using namespace std;

// Recursive function to store all alternate elements
void getAlternatesRec(vector<int> &arr, int idx, vector<int>& res) {
	if(idx < arr.size()) {
    	res.push_back(arr[idx]);
        getAlternatesRec(arr, idx + 2, res);
    }
}

vector<int> getAlternates(vector<int> &arr) {
    vector<int> res;
    getAlternatesRec(arr, 0, res);
    return res;
}

int main() {
    vector<int> arr = {10, 20, 30, 40, 50};
    vector<int> res = getAlternates(arr); 
    for(int x: res)
        cout << x << " ";
}