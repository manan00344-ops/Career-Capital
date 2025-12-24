/*
Input: arr[] = [10, 20, 30, 40, 50]
Output: 10 30 50
Explanation: Print the first element (10),
skip the second element (20), print the third element (30),
skip the fourth element(40) and print the fifth element(50).

Input: arr[] = [-5, 1, 4, 2, 12]
Output: -5 4 12
*/
#include <iostream>
#include <string>
#include <vector>
using namespace std;
vector<int> getalternatives(vector<int> &arr)
{
    vector<int> res;
    // Iterate over all alternate elements
    for (int i = 0; i < arr.size(); i += 2)
    {
        res.push_back(arr[i]);
    }
    return res;
}
int main()
{
    vector<int> arr = {10, 20, 30, 40, 50};
    vector<int> res = getalternatives(arr);
    for (int x : res)
        cout << x << " ";
}
