import pandas as pd
import seaborn as sns
import sqlalchemy as sa

import warnings
warnings.filterwarnings("ignore")
sns.set()

account = pd.read_csv('./AccountHistory.csv')

account.info()

account.describe()

account.columns

sns.set_style("White")

sns.boxplot("balance", data=account)
