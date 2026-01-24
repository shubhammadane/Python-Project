from sklearn.linear_model import LinearRegression

X = [[2],[4],[6],[8]]   # hours studied
y = [40, 50, 70, 86]    # marks

model = LinearRegression()
model.fit(X, y)

print(model.predict([[7]]))  # predict marks for 5 hours study
