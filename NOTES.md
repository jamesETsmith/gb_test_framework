# Survey of the Options
|   Name    | Support C  | Header Only | CMake Interface | Catches Errors | Speed of Running Tests |
| :-------: | :--------: | :---------: | :-------------: | :------------: | :--------------------: |
| Criterion |    Yes     |     No      |       Yes       |      Yes       |          Slow          |
|    Tau    |    Yes     |     Yes     |       Yes       |       No       |          Fast          |
|  doctest  |     No     |     Yes     |       Yes       |      Yes       |          Fast          |
| cpputest  | not really |     No      |       Yes       |       ?        |           ?            |
|  cmocka   |    Yes     |     No      |       Yes       |      Yes       |           ?            |

- [Criterion](https://github.com/Snaipe/Criterion)
- [Doctest](https://github.com/doctest/doctest)
- [tau](https://github.com/jasmcaus/tau)
- [cpputest](https://github.com/cpputest/cpputest)
- [cmocka](https://cmocka.org/)

For now, due to simplicity, I'll just be using `tau`.

Problems with `tau` so far:
- Filtering tests works ok when you want to filter only one thing, but I haven't figured out how to use multiple filters yet (it might not be possible).
- The xml output isn't as useful as other test suites like doctest, it doesn't capture stdout, and doesn't report test status.
- 

## Notes
- Dynamically swap libraries during run time