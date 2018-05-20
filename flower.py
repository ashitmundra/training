#!/usr/bin/python3
import time
from sklearn.datasets import load_iris
from sklearn import tree

iris=load_iris()

fl_data=iris.data.tolist()
fl_target=iris.target.tolist()



vergi=fl_target[100:150]
train_vergi=vergi[0:49]




versi=fl_target[50:100]
train_versi=versi[0:49]




satosa=fl_target[0:50]
train_satosa=satosa[0:49]


s=fl_data[0:50]
train_s=s[0:49]
test_s=s[-1]

vs=fl_data[50:100]
train_vs=vs[0:49]
test_vs=vs[2]

vg=fl_data[100:150]
train_vg=vg[0:49]
test_vg=vg[-1]

features=train_s + train_vs + train_vg
output=train_satosa + train_versi + train_vergi





algo=tree.DecisionTreeClassifier()
trained=algo.fit(features, output)
res=trained.predict([test_s, test_vs, test_vg])
print (res)
