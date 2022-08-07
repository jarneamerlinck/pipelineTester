# Load packages
## Data wrangling
import pandas as pd
import numpy as np

## Model training
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.model_selection import train_test_split

## For saving models
import pickle

## Parser arguments
import argparse


# Set our parser arguments. I like to add this mlflow_run argument so we can still test things out outside of an mlflow run environment by running 'python train.py'
parser = argparse.ArgumentParser(
    description='Titanic training script')

parser.add_argument('--mlflow_run', default=0, type=int,
                    help="Running as an experiment or not. Don't change this, this gets automatically changed by the MLFlow default parameters")

args = parser.parse_args()

if args.mlflow_run:
    from mlflow import log_metric, log_param, log_artifacts

# Main function for training model on split train data and evaluating on validation data
def main():
    # Read preprocessed training data
    train = pd.read_csv('data/preprocessed/train_preprocessed.csv')
    
    # Seperate our features from our outcome variable
    X_full = train.drop('Survived', axis=1)
    y_full = train.Survived
    
    # Split our non-test set into a training and validation set
    X_train, X_valid, y_train, y_valid = train_test_split(X_full, y_full, test_size=0.3, random_state=0)
    
    # Train a RandomForestClassifier
    n_estimators = 12
    model = RandomForestClassifier(n_estimators=n_estimators, random_state=0)
    
    print(f'Training {model}')
    model.fit(X_train, y_train)
    
    # Make prediction on our validation dataset
    predict = model.predict(X_valid)
    
    # Show our model accuracy on the validation data
    accuracy = metrics.accuracy_score(y_valid, predict)
    print('Valid Accuracy: ',np.round(accuracy, 4))
    
    # Log hyperparameters of the model and output metrics
    if args.mlflow_run:
        print('Tracking MLFlow params & metrics')
        log_param('n_estimators',n_estimators)
        log_metric('Validation accuracy', accuracy)
        log_metric('Training accuracy', metrics.accuracy_score(y_train, model.predict(X_train))) # This can be interesting to see how much we're overfitting on our data
    
    # Train model on the full dataset
    model.fit(X_full, y_full)
    
    # Save our model weights and parameters to a pickle file
    model_name = 'models/trained_model.pkl'
    with open(model_name, 'wb') as file:
        pickle.dump(model, file)
    
if __name__=='__main__':
    main()
