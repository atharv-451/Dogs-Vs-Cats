# Dogs vs Cats Classification Project

This project aims to classify images of dogs and cats using transfer learning with the MobileNetV2 model. The dataset used is the "Dogs vs. Cats" competition dataset from Kaggle.

## Getting Started

### Prerequisites

- Python 3
- Jupyter Notebook/ Google Colab Notebook
- TensorFlow
- TensorFlow Hub
- OpenCV
- NumPy
- PIL (Pillow)
- Matplotlib
- Scikit-Learn

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/dogs-vs-cats-classification.git
   cd dogs-vs-cats-classification
   
2. Install dependencies:

   ```bash
   pip install -r requirements.txt

3. Download the Kaggle dataset and extract it:

   ```bash
   kaggle competitions download -c dogs-vs-cats
   unzip dogs-vs-cats.zip
   unzip train.zip

## Project Structure

- 'Dog vs Cat Classification.ipynb' : Google Colab Notebook containing the code for the project.
- 'kaggle.json' : Kaggle API key for downloading the dataset
- 'image_resized/' : Directory containing resized images.

## Usage

- Open and run the 'Dog vs Cat Classification.ipynb' notebook in a Google Colab environment.
- Follow the instructions and code cells in the notebook to:

    - Download the dataset from Kaggle.
    - Extract and resize images.
    - Train a MobileNetV2-based model for classification.
- Evaluate the model's performance on the test set.
- Use the predictive system to classify new images.

## Results
The model achieved 99.3% accuracy on the test set after training for 5 epochs. Results may vary based on parameters and dataset size.

## Author
ATHARV KULKARNI

### Please feel free to contribute to the project by creating a pull request
