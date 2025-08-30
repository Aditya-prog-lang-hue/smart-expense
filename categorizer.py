import pandas as pd

def categorize_expenses(file_path):
    try:
        df = pd.read_csv(file_path)

        if "Description" not in df.columns or "Amount" not in df.columns:
            return None, "CSV must have 'Description' and 'Amount' columns!"

        categories = {
            "Food": ["restaurant", "dominos", "pizza", "cafe", "food", "swiggy", "zomato"],
            "Shopping": ["amazon", "flipkart", "myntra", "shopping", "clothes"],
            "Rent": ["rent", "apartment", "house"],
            "Bills": ["electricity", "wifi", "internet", "mobile", "gas"],
            "Travel": ["uber", "ola", "bus", "train", "flight", "airline"]
        }

        def classify(desc):
            desc = str(desc).lower()
            for cat, keywords in categories.items():
                if any(word in desc for word in keywords):
                    return cat
            return "Other"

        df["Category"] = df["Description"].apply(classify)
        summary = df.groupby("Category")["Amount"].sum().to_dict()

        return df, summary

    except Exception as e:
        return None, str(e)
