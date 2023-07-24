import pandas as pd
from ydata_profiling import ProfileReport

pd_df = pd.read_csv("file:///Users/santiagorespane/Documents/repos/zenpli-challenge/data/backend-dev-data-dataset.txt", parse_dates=['date_2'])

print(pd_df.info())

profile = ProfileReport(pd_df, title="Data Profiling Report")


# Export data profiling to a local HTML file
profile.to_file("your_report.html")



