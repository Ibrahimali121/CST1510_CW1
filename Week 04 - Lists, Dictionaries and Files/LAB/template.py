"""
RECORD CHECK  -  my version
===========================

Name  : ibrahim ali
Lane  :  AI / Cyber / IT      (delete two)
Date  :

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1. Bring back check_record(value, limit) and print_report(...) from Week 3
#    (copy them, or rewrite them - either is fine). check_record returns
#    difference, percent and status. print_report does all of the printing,
#    nothing outside it should contain a print() of its own. Give each a
#    one-line docstring.

# your function(s) go here
def check_record(value, limit):
    """check the recorded value"""
    difference = value - limit
    percent = (value / limit) * 100

    if value > limit:
        status = "OVER LIMIT"
    else:
        status = "OK"

    return difference, percent, status


def print_report(label, difference, percent, status):
    """print the results."""
    print("record:", label)
    print("Difference:", round(difference, 2))
    print("percent", round(percent,2))
    print("status:", status)
    


# ====================================================================== STORE
# 2. Get your records into a list of dicts, each shaped like:
#        {"label": ..., "value": ..., "limit": ...}
#
#    Threshold : write the list directly in the code - at least 3 records.
#    Typical   : instead, write a function load_records(path) that reads
#                label,value,limit lines from a file and returns the list.
#                Make your own data file, one record per line.
#    Excellent : also write the results out to a new file (one line per
#                record: label, status), as well as printing them.

records = []
def load_records(path):
    """Read records from"""
    records = []

    try:
        with open (path) as f:
            for line in f:
                label,value,limit = line.strip().split(",")


                record = {
                    "label": label,
                    "value": float(value),
                    "limit": float(limit)

                }
                records.append(record)

    except FileNotFoundError:
        print_report("file not", 0,0, "error")

    return records 


records = load_records("cyber_records.txt")






# =============================================================== PROCESS + OUTPUT
# 3. Loop over records. For each one, call check_record and print_report.
#
#    Excellent : also keep a running count of how many were OVER LIMIT, and
#                print that once, after the loop ends.
for record in records:
    difference, percent, status = check_record(
     record["value"], record["limit"]
    
    )

    print_report(record["label"], difference, percent, status)



# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers are correct by hand
#    [ ] If you are loading from a file, check what happens when the file
#        does not exist - write the error down
# if file doesnt exist than the following error will than be shown

#record: file not
#Difference: 0
#percent 0
#status: error

#    [ ] Check every function still does one job yes
