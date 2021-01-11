# Face Recognition Using OpenCV


This is a simple Face Recognition project. This will help to create your own dataset, train the model on your dataset, and test your model. 
<br/><br/>

To use the code download the zip file and unzip it.Then open command prompt and go to the folder location.

### Create an environment using following command.
```python
py -m venv env
```

### Now we can activate the environment. We created the environment with name ***env*** so , we do the following
```python
.\env\Scripts\activate
```

### Now we have to install all the required pakages. So run the following command.
```python
pip install -r requirements.txt
```

### Creating Dataset 
The first file **create_dataset.py** will help us to create a dataset for any number of user you want. ***Remember to create a folder named 'dataset' before running the above script***. Just give it a proper number when asked starting from 1. 
```python
python create_dataset.py
```

### Training Model
The second file is the **training_dataset.py**. This will help us to train the dataset we just created. ***Remember to create a folder named 'trainer' before running the above script as this is the folder where our model will be stored***.
```python
python training_dataset.py
```

### Testing
Now you can run the last file. This file will read the saved model and then predict the result. Just remember to put the names of the users you have created the dataset in the dictionary defined in this file. The model predicts the output very well. I am having a problem in printing the accuracy of prediction. It shows accuracy greater than 100%. Don't worry I will fix it later.
```python
python recogniser.py
```
<br/><br/>
