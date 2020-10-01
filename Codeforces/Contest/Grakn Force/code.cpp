#include <iostream>


using namespace std;

const int N = 102;
int a[N],b[N],c[N];
int n;

int main(int argc, char const *argv[])
{
    int t;
    cin >> t;
    while (t--)
    {
        cin >> n;
        for(int i=0;i<n;i++)cin >> a[i];
        for(int i=0;i<n;i++)cin >> b[i];
        for(int i=0;i<n;i++)cin >> c[i];

        for(int i=1;i<n;i++){
            if (i!=n-1)
            {
                if (a[i-1]==a[i])
                {
                    a[i]=b[i];
                }
            }else
            {
                if (a[0]!=b[i] && b[i] != a[i-1])
                {
                    a[i]=b[i];
                }else if( a[0]!=c[i] && c[i] != a[i-1])
                {
                    a[i]=c[i];
                }
            }
        }
        for(int i=0;i<n;i++){
            cout << a[i] << " ";
        }
        cout << "\n";
    }
    





    /* code */
    return 0;
}
