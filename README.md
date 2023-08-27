# CSE-2nd-yr-B-programs

[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](https://makeapullrequest.com)
![License](https://badgen.net/github/license/micromatch/micromatch)

IT and DSA programs assigned to section B of 2nd year CSE.

I will add particulars on how to contribute to this repository after sometime, Meanwhile feel free to contribute if you are already knowledgeable.
Ofcourse the prerequisite is to belong from CSE 2nd yr section B.

Points to note before opening a pr:

1.This repo will mainly focus on programs given as assignments(classwork or homework) and should be written in a way that will be accepted by the college,
so classmates can just copy blindly. So no fancy stuff here.

2.Fancy stuff will be included in an "Extras" folder.

3.Comment lines are encouraged wherever necessary.

## Getting started

To get a copy of these programs up and running on your local machine, simply clone this repository:

```bash
git clone https://github.com/itz-ankit/CSE-2nd-yr-B-programs
```

[if you are scared of CLI don't worry we got you covered](https://www.youtube.com/watch?v=PvUexC0-D2s)

## Prerequisites

You will need the following tools installed on your system to run these programs:

- Any Code Editor you like we prefer [VS Code](https://code.visualstudio.com/download)

- setup C compiler, we prefer [MinGW](https://sourceforge.net/projects/mingw/), 
  setup Python by following this [tutorial](https://youtu.be/cUAK4x_7thA?si=Qn4rZbF85UCEZxc8)

  [You can follow this tutorial to install gcc in vscode for windows](https://www.youtube.com/watch?v=Ubfgi4NoTPk)

- Lastly make sure you have prettier extension installed in vscode for formatting
  [here is how you can do it](https://www.youtube.com/watch?v=__eiQumLOEo)

  you are now ready to contribute ;)

## Contributing

- Navigate to the specified folder the format is section name and then day name

  (any extra programs should be written in the extra folder under the specified concept)

  Example:

  ```
   IT/D1 would contain Day 1 IT programs
  ```

- Write the question using comment lines and then code
  if possible display the result in comment lines.

  Example

```C
// Convert Farenheit to Celcius
#include <stdio.h>

int main()
{
    float fahrenheit, celcius;

    printf("Enter temp in farenheit\n");
    scanf("%f", &fahrenheit);

    celcius = (5.0 / 9) * (fahrenheit - 32);

    printf("The temperature in celcius is %f °", celcius);

    return 0;
}
/*
Enter temp in farenheit
32
The temperature in celcius is 0.000000
*/

```

- Use suitable comment lines.

- There's no restriction on your approach to solve.

- Maintain readability(use appropriate variable names and comments)

## Documentation and Concepts

check out

[Documentation.md](Documentation.md) and [Concepts.md](Concepts.md)
