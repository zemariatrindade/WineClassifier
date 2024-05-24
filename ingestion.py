import sqlite3
import pandas as pd
import sys
import pickle
from sklearn.metrics import accuracy_score

def create_wines_table():
    # connecting to the Wines_user.db. If not existent, creates an empty db
    conn = sqlite3.connect('Wines_user.db')
    c = conn.cursor()

    # IF NOT EXISTS = only creates a table, if the wines table doesn't exist
    c.execute(
        "CREATE TABLE IF NOT EXISTS wines_table(id INTEGER, class TEXT)")

    # Closing the connection
    c.close()
    conn.close()


def load_implement_model(path_to_file):
    with open('best_model.pkl', 'rb') as file:
        loaded_model = pickle.load(file)

    df = pd.read_csv(path_to_file)

    # Splitting the data into features and target variable
    X = df.drop(['pH', 'quality', 'quality_merged'], axis=1)
    y = df['quality_merged']

    # Predict on the test set using the loaded model
    y_pred_loaded_model = loaded_model.predict(X)
    print(accuracy_score(y_pred_loaded_model, y))

    df["class"] = y_pred_loaded_model

    df = df["class"].reset_index().rename(columns={"index": "id"})

    return df


# Function to append records to the wines table in the Wines_user.db
def data_entry(df):
    # connecting to the db
    conn = sqlite3.connect('Wines_user.db')
    c = conn.cursor()

    # Appends messages to the wines table
    df.to_sql("wines_table", conn, if_exists="append", index=False)

    # closing connection
    c.close()
    conn.close()




if __name__ == '__main__':
    path_to_file = sys.argv[1]
    df = load_implement_model(path_to_file)

    create_wines_table()

    data_entry(df)