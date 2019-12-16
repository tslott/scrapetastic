import requests
import pandas as pd


def get_tryg_donations():

    page_not_empty = True
    page_num = 1
    responses = []

    while page_not_empty:

        # Print progress
        if page_num % 10 == 0:
            print(f'Looped through {page_num} pages')

        response = requests.get(
            f'https://www.trygfonden.dk/api/donation/?npt=donation&currentPage={page_num}&Sort=-year'
        )
        response_data = response.json()['Results']['data']

        # Break loop if repsonse has no data
        if not response_data:
            page_not_empty = False
            break

        # Add all data entries (donations) from page
        for donation in response_data:
            responses.append(donation)

        page_num += 1

    return pd.DataFrame(responses)


if __name__ == "__main__":

    df = get_tryg_donations()

    # Save to pickle
    df.to_pickle(f'./data/tryg_donations.pickle')
