from surprise import Dataset, Reader,KNNBasic

data = Dataset.load_builtin('ml-100k')

raw = data.raw_ratings

cols = ['user_id', 'item_id', 'rating', 'timestamp']

for i in range(5):
    row = raw[i]
    print({cols[j]:row[j] for j in range(len(cols))})

model = KNNBasic()
trainset = data.build_full_trainset()
model.fit(trainset)

def predict(user_id,model,custom_rating):
    custom_d = [(user_id,item_id,rating)for item_id,rating in custom_rating.items()]
    testset = trainset.build_testset()+custom_d
    predictions = model.test(testset)
    return predictions

pred = predict(196,model,{0:4,1:2,2:5})

for i,pre in enumerate(pred):
    print(f"Prediction Item Id {pre.iid} : Estimated : {pre.est:.2f}")