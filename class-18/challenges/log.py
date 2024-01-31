# Open the log file and read its contents
with open("log.txt", "r") as log_file:
    # Read the entire contents of the file
    error_log = log_file.read()

# Split the log into lines
log_entries = error_log.strip().split('\n')

# Create separate files for warnings, errors, and threats
warnings_file = open("warnings.log", "w")
errors_file = open("errors.log", "w")
threats_file = open("threats.log", "w")

# Iterate through log entries and categorize them
for entry in log_entries:
    if "WARNING" in entry:
        warnings_file.write(entry + '\n')
    elif "ERROR" in entry:
        errors_file.write(entry + '\n')
    elif "THREAT" in entry:
        threats_file.write(entry + '\n')

# Close the files
warnings_file.close()
errors_file.close()
threats_file.close()

print("Categorization complete. Check 'warnings.txt', 'errors.txt', and 'threats.txt' for results.")
