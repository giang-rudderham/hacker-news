import pandas as pd

def load_data():
    data = pd.read_csv("/home/dq/scripts/hn_stories.csv")
    # Assign column names
    data.columns = ["submission_time", "upvotes", "url", "headline"]
    return data
#Test load_data() function:
#data = load_data()
#print(data.head())    