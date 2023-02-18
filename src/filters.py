import os
import json
from typing import Generator, Iterable


class InvalidFieldPassedError(ValueError):
    """
    Exception class to raise if invalid field passed.
    """


class InvalidRegionPassedError(ValueError):
    """
    Exception class to raise if invalid field passed.
    """


DATA_PATH = os.path.join(os.getcwd(), "data")

FIELD_FILES = {
    "law": "law_participated.json",
    "nirf": "college_participated.json",
    "research": "research_ranking.json",
    "dental": "dental_participated.json",
    "medical": "medical_participated.json",
    "pharmacy": "pharmacy_participated.json",
    "universities": "university_ranking.json",
    "management": "management_participated.json",
    "engineering": "engineering_participated.json",
    "architecture": "architecture_participated.json",
}


def check_values(*,
                 data: Iterable,
                 value: str,
                 value_type: str | None = None,
                 error_msg: str | None = None
                 ) -> None:
    """
    Check if the provided value present in the data.
    If not present,
    it raises the `value_type` matched ERROR with msg.
    `value_type` current matches with:
    - "region" : InvalidRegionPassedError
    - "field" : InvalidFieldPassedError
    """
    if value in data:
        return

    match value_type:
        case "region":
            ERROR = InvalidRegionPassedError
        case "field":
            ERROR = InvalidFieldPassedError
    raise ERROR(error_msg)


def get_data(field: str) -> list:
    """
    Takes the field,
    If field is correct, return the data mapped to it.
    Else, raises InvalidFieldPassedError from `check_values()`
    """
    print("get_data", field)
    check_values(
        data=FIELD_FILES,
        value=field,
        value_type="field",
        error_msg=("Invalid Field passed.\n"
                   "Run `field_files.keys()` to get a set of all available fields."
                   )
    )
    print("done")
    file = FIELD_FILES.get(field)
    file_path = os.path.join(DATA_PATH, file)
    return json.load(open(file_path))


def fetch_details(data: list,
                  region: str = "state",
                  region_required: str = "state"
                  ) -> Generator[dict | int, None, None]:
    """
    Generates the details of specified `region`.
    If no details found, gives `-1`
    """
    data_is_available = False
    for detail in range(len(data)):
        region_name = data[detail][region].replace(" ", '').lower()
        if region_name == region_required:
            data_is_available = True
            yield data[detail]

    if not data_is_available:
        yield -1


def get_colleges(field: str,
                 region: str = "state",
                 region_required: str = "state"
                 ) -> Generator[dict | int, None, None]:
    """
    Generates details of college/universities
    of specified field and region.
    If field is not correct, InvalidFieldPassedError
    If region is not correct, raises InvalidRegionPassedError
    from `check_values()`.
    """
    print("get_collegs")
    check_values(
        data=("state", "city"),
        value=region,
        value_type="region",
        error_msg=('Invalid Region passed.\n'
                   'Region either be "state" or "city".'
                   )
    )
    print("done")
    data = get_data(field)
    print("data", data)
    return fetch_details(data, region, region_required)


# Filter Function
def filter_colleges(field: str,
                    region_list: list[str],
                    region: str = "state") -> list[int | str]:
    
    response = []
    for i in region_list:
        region_req = i.replace(" ", "").lower()
        print(region_req)
        response.extend(get_colleges(field, region, region_req))
    return response


def get_response(field: str,
                 **regions: str) -> list[int | str]:

    region = set(regions.keys()).pop()

    region_list = [i.strip() for i in regions[region].split('&')]
    print(regions, region, region_list)
    try:
        output = filter_colleges(field, region_list, region)
        print(output)
        if output[0] == -1:
            output = -1
    except:
        output = -1

    return output


def get_field_data(file: str) -> str | int:
    file_path = os.path.join(DATA_PATH, file)
    try:
        with open(file_path) as file:
            output = file.read()
    except:
        output = -1
    return output
