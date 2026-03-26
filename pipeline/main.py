import sys, os 
import pandas as pd

def main():

    os.makedirs('output', exist_ok=True)

    print("Hello from pipeline!", sys.argv[1])
    df = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
    print(df.head())

    df.to_parquet(f"output/output_day_{sys.argv[1]}.parquet")






if __name__ == "__main__":
    main()
