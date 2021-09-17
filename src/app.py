# Standard library imports
import os

# Third party imports
from pandas import DataFrame

# Local application imports
from helper import load_df_to_postgres


# def lambda_handler(event, context):
def main():
    # print('Events :', event)
    # print('\n Context :',  context)
    appointy_data = get_fake_data_from_appointy()
    print(appointy_data)


def get_fake_data_from_appointy():
    fake_data = {
        'Customer User Name': 'email@example.com',
        'Customer First Name': 'Noemi',
        'Customer Last Name': 'Cognomitis',
        'Contact Number Cell': '600111222',
        'Appointment Start Time': '2021-06-13T07:45:00+00:00',
        'Appointment End Time': '2021-06-13T05:45:00+00:00',
    }
    return fake_data


if __name__ == "__main__":
    main()
