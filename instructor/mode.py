import enum
import warnings


class Mode(enum.Enum):
    """The mode to use for patching the client"""

    FUNCTIONS = "function_call"
    PARALLEL_TOOLS = "parallel_tool_call"
    TOOLS = "tool_call"
    MISTRAL_TOOLS = "mistral_tools"
    UNGUIDED_JSON = "unguided_json_mode"
    PARSED_UNGUIDED_JSON = "parsed_unguided_json_mode"
    JSON = "json_mode"
    MD_JSON = "markdown_json_mode"
    JSON_SCHEMA = "json_schema_mode"

    def __new__(cls, value: str) -> "Mode":
        member = object.__new__(cls)
        member._value_ = value

        # Deprecation warning for FUNCTIONS
        if value == "function_call":
            warnings.warn(
                "FUNCTIONS is deprecated and will be removed in future versions",
                DeprecationWarning,
                stacklevel=2,
            )

        return member
