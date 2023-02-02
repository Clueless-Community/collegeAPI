## Description

<!-- Include a summary of the change made and also list the dependencies that are required if any -->

> ### Dependencies
>
> aiofiles==22.1.0
>
> autopep8==2.0.1

### Refactored

#### `main.py`

-   Removed conditions from `filter_colleges()`, do all in one using `get_colleges()`.
-   Stored metadata of **CollegeAPI** in `API_METADATA`.
-   removed unnecessary dependencies.

#### `filters.py`

-   Different field colleges / universities in 1 function named `get_colleges()`.
-   Replaced `processing()` with `fetch_details()` which generates the data, works more efficiently.
-   Stored path of data folder in `DATA_PATH`.
-   Stored fields mapped to their respective json files in `FIELD_FILES`.
-   Added $2$ custom _Exceptions_ inherited from `ValueError`

```py
class InvalidFieldPassedError(ValueError):
    """
    Exception class to raise if invalid field passed.
    """

class InvalidRegionPassedError(ValueError):
    """
    Exception class to raise if invalid field passed.
    """
```

-   Added `check_values()` function, which checks and raises above exceptions if data provided doesn't matched.

### `data` directory

-   Fixed cases of object parameters (city, state) of some files.

---

## Issue Ticket Number

Fixes \*\*Refactor the codebase #171

---

## Type of change

<!-- Please select all options that are applicable. -->

-   [x] Refactored code
-   [x] Bug fix (non-breaking change which fixes an issue)
-   [ ] New feature (non-breaking change which adds functionality)
-   [ ] Breaking change (fix or feature that would cause existing functionality to not work as expected)
-   [ ] This change requires a documentation update

---

# Checklist:

-   [x] Remove unnecessary dependencies.
-   [x] Use/create functions to use reduce the repetition of code.
-   [x] I have followed the contributing guidelines of this project as mentioned in [CONTRIBUTING.md](/CONTRIBUTING.md)
-   [x] I have checked to ensure there aren't other open [Pull Requests](https://github.com/Clueless-Community/collegeAPI/pulls) for the same update/change?
-   [x] I have performed a self-review of my own code
-   [x] I have commented my code, particularly in hard-to-understand areas
-   [x] I have made corresponding changes needed to the documentation
