# Fake News Classifier Using Bidirectional LSTM

This project aims to classify news articles as fake or real using a Bidirectional Long Short-Term Memory (BiLSTM) neural network. The dataset used for this project is from the [Kaggle Fake News competition](https://www.kaggle.com/c/fake-news/data).

## Dataset

The dataset consists of two CSV files:
- `train.csv`: Contains the training data with news articles and their corresponding labels (fake or real).
- `test.csv`: Contains the test data with news articles that need to be classified.

## Project Structure

```
Project
├── src
│   └── Bidirectional LSTM.ipynb
└── Data
│   ├── train.csv
│   ├── test.csv
│   └── submission.csv
└── README.md
```

The project is structured as follows:
1. **Data Loading**: Load the training and test datasets using pandas.
2. **Data Preprocessing**: 
    - Handle missing values.
    - Text preprocessing including tokenization, lemmatization, and removal of stopwords.
    - One-hot encoding of the text data.
    - Padding sequences to ensure uniform input length.
3. **Model Building**:
    - Define the BiLSTM model using TensorFlow and Keras.
    - Compile the model with appropriate loss function and optimizer.
4. **Model Training**: Train the model on the training data.
5. **Model Evaluation**: Evaluate the model on the test data using accuracy and confusion matrix.
6. **Prediction on Test Data**: Preprocess the test data and make predictions using the trained model.
7. **Submission**: Create a submission file in the required format for the Kaggle competition.

## Requirements

The following libraries are required to run the project:
- pandas
- numpy
- tensorflow
- nltk
- scikit-learn

## Installation

1. Clone the repository:
    ```
    git clone https://github.com/Khaled-Saleh-KL1/NLP/fake-news-classifier.git
    cd fake-news-classifier/src
    ```

## Results

The model achieves an accuracy of approximately `90%` on the test data.

## Author

Khaled Saleh
