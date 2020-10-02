#include<iostream>

using namespace std;

int main(int argc, char const *argv[])
{
    int a,b,c,d,n,x,tt,m;


    cin >> tt;
    while (tt--)
    {
        cin >> n >> m;
        bool ansLL = false;

        for(int i=0;i<n;i++){
            cin >> a >> b >> c >> d;
            if (b==c){
                ansLL = true;
            }
        }
        if(m%2 != 0){
            cout << "NO" << "\n";
        }else if(ansLL == true){
            cout << "YES" << "\n";
        }else
        {
            cout << "NO" << '\n';
        }
    }
    return 0;
}
