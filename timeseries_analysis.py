# Training and Predicting for different parameters
dtm = DecisionTreeRegressor(max_depth=4,
                           min_samples_split=5,
                           max_leaf_nodes=10)

dtm.fit(x_train_lm1, y_train_lm1)
print("R-Squared on train dataset={}".format(dtm.score(x_test_lm1,y_test_lm1)))

dtm.fit(x_test_lm1,y_test_lm1)   
print("R-Squaredon test dataset={}".format(dtm.score(x_test_lm1,y_test_lm1)))

