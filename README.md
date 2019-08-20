# Today  

https://jlptstudy.net/N5/

```cpp
#include <iostream>
#include <thread>

int x = 1;

void thread_function()
{
	x = x - 1;
	x = x + 1;
}

int main()
{

	std::thread t2(thread_function);
	std::thread t1(thread_function);

	t1.join();
	t2.join();

	std::cout << x << std::endl;

	return 0;
}
```

```cpp
#include <iostream>
#include <string>
using namespace std;

string foo() {
    string* s = new string("World");
    return *s;
}

void main()
{
    cout << "Hello, " << foo();
}
```
