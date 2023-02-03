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


# Files Not Used:
"""
- allAgriculture.json
- allParticipatingDentalColleges.json

- nirfAllColleges.json
- nirfAllParticipatingColleges22.json
- nirfArchitectureColleges.json
- nirfLawCollegesRanked.json
- nirfManagementColleges.json
- nirfMedicalColleges.json
- nirfPharmacyColleges.json
- nirfResearchColleges.json
- nirfUniversities.json
- nirfParticipatingUniversities.json
"""

DATA_PATH = os.path.join(os.getcwd(), "data")

FIELD_FILES = {
    "nirf": "allNirfColleges.json",
    "dental": "nirfDentalColleges.json",
    "medical": "allMedicalColleges.json",
    "research": "allResearchColleges.json",
    "law": "allParticipatedLawColleges.json",
    "management": "allManagementColleges.json",
    "engineering": "allEngineeringColleges.json",
    "architecture": "allArchitectureColleges.json",
    "pharmacy": "allParticipatingPharmacyColleges.json",
    "universities": "nirfParticipatedUniversities.json",
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
    check_values(
        data=FIELD_FILES,
        value=field,
        value_type="field",
        error_msg=("Invalid Field passed.\n"
                   "Run `field_files.keys()` to get a set of all available fields."
                   )
    )

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

    check_values(
        data=("state", "city"),
        value=region,
        value_type="region",
        error_msg=('Invalid Region passed.\n'
                   'Region either be "state" or "city".'
                   )
    )

    data = get_data(field.strip("_colleges"))
    return fetch_details(data, region, region_required)
