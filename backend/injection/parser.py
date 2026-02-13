import re
LOG_PATTERN = re.compile(
    r"(?P<timestamp>[\d\-:\s]+)\s"
    r"(?P<level>\w+)\s"
    r"(?P<service>\w+)\s"
    r"(?P<message>.*?)(?:\suser_id=(?P<user_id>\d+))?$"
)
#Groupdict()
#Strip()
#re.compile()
#python regex are used for searching, matching and extract the data pattern from given text.
#re.compile is a method used to create regex patterns
#r-> raw data
# ?->starting of pattern
#(?P<timestamp>[\d\-:\s]+), (?P<level>\w+), (?P<service>\w+), (?P<message>.*?) is used to capture the names of particualr data
# \s is used to remove the white or extra space from the data