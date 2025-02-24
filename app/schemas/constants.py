from enum import Enum
from typing import List, Union

VariableValue = Union[int, float, str, bool, List[Union[int, float, str, bool]]]


class VariableType(str, Enum):
    """The types are based on what is used in CTSM xml files,
    except for date, which is char in yyyy-mm-dd format in CTSM."""

    char = "char"
    integer = "integer"
    float = "float"
    logical = "logical"
    date = "date"


class VariableCategory(str, Enum):
    ctsm_xml = "ctsm_xml"
    user_nl_clm = "user_nl_clm"
    user_nl_clm_extra = "user_nl_clm_extra"
    user_nl_clm_history_file = "user_nl_clm_history_file"
    fates = "fates"
    fates_param = "fates_param"


class CTSMDriver(str, Enum):
    """The driver to use with CTSM create_newcase script."""

    nuopc = "nuopc"
    mct = "mct"


class CaseStatus(str, Enum):
    INITIALISED = "INITIALISED"
    CREATED = "CREATED"
    SETUP = "SETUP"
    UPDATED = "UPDATED"
    FATES_PARAMS_UPDATED = "FATES_PARAMS_UPDATED"
    FATES_INDICES_SET = "FATES INDICES SET"
    CONFIGURED = "CONFIGURED"
    BUILDING = "BUILDING"
    BUILT = "BUILT"
    INPUT_DATA_READY = "INPUT_DATA_READY"
    SUBMITTED = "SUBMITTED"


class TaskStatus(str, Enum):
    PENDING = "PENDING"
    STARTED = "STARTED"
    SUCCESS = "SUCCESS"
    FAILURE = "FAILURE"
    REVOKED = "REVOKED"
    RECEIVED = "RECEIVED"
    REJECTED = "REJECTED"
    RETRY = "RETRY"
    IGNORED = "IGNORED"
