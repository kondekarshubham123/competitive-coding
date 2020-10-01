#include <iostream>

using namespace std;

int main(int argc, char const *argv[])
{
    int t,n,x,r;
    cin >> t;
    while (t--)
    {
        cin >> n >> x;
        if (n==1 || n==2)
        {
            cout << 1;
        }else
        {
            n-=2;
            if(n%x){
                r=2;
            }else{
                r=1;
            }
            cout << r+(n/x); 
        }
        cout << "\n";
        
    }
    
    
    return 0;
}
