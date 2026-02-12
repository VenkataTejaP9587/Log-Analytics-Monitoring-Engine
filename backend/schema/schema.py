# schema files define the structure of data and type of data, role book of data
# uses: 
# 1.it ensures all rows to follow same data structure
# 2. it helps to validate and data cleaning
# 3. faster processing, easier analytics (filtering, mapping, grouping, anamoly detection becomes simple and fast)
log_schema = {
    "timestamp": "datetime", 
    "level" : "string" ,
    "service" : "string" ,
    "message" : "string" ,
}
# dataframe = df.astype(log_schema)