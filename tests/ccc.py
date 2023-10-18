from cancel_all_orders import cancel_all_orders
from orders_of_user import get_orders_of_user
# cancel_all_orders()
# get_orders_of_user()

import seaborn
import matplotlib.pyplot as plt
from orderbooks import get_orderbooks
import pandas as pd


def write_dataframe(path_to_file, df: pd.DataFrame):
    df.to_csv(path_to_file)
    return 0


    # try:
    #     with open(path_to_file, 'w') as file:
    #         write(path_to_file)
    # except Exception as error:
    #     print(error)


data = get_orderbooks()
data_asks = data['result']['asks']
data_bids = data['result']['bids']

df_asks = pd.DataFrame.from_dict(data_asks, orient='columns')
path_to_file = f'json_responces/orderbooks_frame_asks.json'
df_asks.to_csv(path_to_file)
print(df_asks)

plt.show()
seaborn.barplot(data=df_asks)





