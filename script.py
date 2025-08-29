import git_api
import process
import pandas as pd

from process import fix_locations


def main():
    # returns the Github jobs added daily
    file_name = git_api.git_api()
    file = open(file_name, 'r', newline='')
    df = pd.read_csv(file)
    process.fix_locations(df)
    process.fix_arrow(df)
    df.dropna(axis=0, how='any', subset=['company', 'role', 'location', 'link', 'age']).to_csv(file_name, index=False)



if __name__ == '__main__':
    main()
