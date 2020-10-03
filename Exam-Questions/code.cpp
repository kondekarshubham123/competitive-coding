#include <iostream>
#include <math.h>
#include <vector>
#include <bits/stdc++.h> 

using namespace std;

int find(char a){
    char p = 'A';
    int ele = -1;
    for(int i=1;i<=26;i++){
        if(p==a){
            return i;
        }
        p++;
    }
    return ele;
}

int len(string A){
    int count = 0;
    for(int i=0;A[i]!='\0';i++){
        count++;
    }
    return count;
}

int fun(string A){
    int n=len(A)-1;
    int i=0,sum=0;
    for(i=0;A[i]!='\0';i++){
        sum += pow(26,n) * find(A[i]);
        n--;
    }
    return sum;
}



int main(int argc, char const *argv[]){
    int no;
    cin >> no;
    vector<int> ans;

    string Array[no];
    for(int i=0;i<no;i++){
        cin >> Array[i];
    }
    for(int i=0;i<no;i++){
        ans.push_back(fun(Array[i]));
    }
    sort(ans.begin(),ans.end());
    for(int i=no-1;i>=0;i--){
        cout << ans[i];
    }
}