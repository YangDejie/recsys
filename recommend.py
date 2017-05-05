from recsys.algorithm.factorize import SVD
from recsys.datamodel.data import Data

filename="./data/ratings.dat"
data=Data()
format = {'col':0,'row':1,'value':2,'ids':int}
# About format parameter:
#   'row': 1 -> Rows in matrix come from second column in ratings.dat file
#   'col': 0 -> Cols in matrix come from first column in ratings.dat file
#   'value': 2 -> Values (Mij) in matrix come from third column in ratings.dat file
#   'ids': int -> Ids (row and col ids) are integers (not strings)
data.load(filename,sep="::",format=format)
train,test = data.split_train_test(percent=80) # 80% train ,20%test

svd= SVD()
svd.set_data(train)

print(svd.predict(22,22,MIN_VALUE=0.0,MAX_VALUE=5.0))
# the prediction for user loving item
print (svd.recommend(1,n=10,only_unknowns=True,is_row=False))
#item recomended for user ,only from known
print (svd.recommend(1,n=10,only_unknowns=False,is_row=False))
#item recomended for user