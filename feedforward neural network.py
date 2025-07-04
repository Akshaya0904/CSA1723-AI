from keras.models import Sequential
from keras.layers import Dense
import numpy as np
X=np.array([[0,0],[0,1],[1,0],[1,1]])
y=np.array([0,1,1,0])
m=Sequential()
m.add(Dense(2,input_dim=2,activation='relu'))
m.add(Dense(1,activation='sigmoid'))
m.compile(loss='binary_crossentropy',optimizer='adam')
m.fit(X,y,epochs=100,verbose=0)
print("Predictions:", m.predict(X).round().flatten())
