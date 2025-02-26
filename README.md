# AI project for combinational depth prediction

## Overview
This project aims to predict the **combinational logic depth** of RTL circuits using machine learning models. Instead of running a full synthesis, which is time-consuming, I useed extracted RTL features and ML models to estimate logic depth, enabling faster design iterations.

## Methodology

### 1. Feature Extraction using Yosys and ABC
I used **Yosys**, an open-source synthesis tool, to extract various structural parameters from RTL designs and **ABC**, a logic synthesis and optimization tool, to compute the logic depth.

#### Features Extracted:
- **Number of wires**: Total count of wires in the circuit.
- **Number of wire bits**: Total bit-width of all wires.
- **Number of public wires**: Count of publicly accessible wires.
- **Number of public wire bits**: Bit-width of public wires.
- **Number of memories**: Count of memory elements used.
- **Number of memory bits**: Total bit-width of memory elements.
- **Number of processes**: Number of process blocks in RTL.
- **Number of instantiated logic cells**: Instances of logic blocks like shift operations and multiplexers.
- **Logic Depth**: Extracted from ABC synthesis reports.

### 2. Automating Feature Extraction using Python
A Python script automates the process by:
1. Running **Yosys** to extract synthesis parameters.
2. Running **ABC** to determine the **logic depth**.
3. Parsing the output and storing the extracted features in a CSV file.

### 3. Data Augmentation using GANs
Since the dataset is small, I used **Generative Adversarial Networks (GANs)** to create synthetic data points, improving model accuracy. The GAN generates realistic feature sets to expand the dataset.

### 4. Machine Learning Model Training
I tested multiple models:
- **Neural Networks**: Required high computation.
- **Random Forest**: Performed Ill but had limitations.
- **XGBoost**: Provided the best accuracy and was chosen as the final model.

### 5. Prediction and Evaluation
The trained model predicts **logic depth** for new RTL designs in **real-time**, significantly reducing the need for full synthesis.

## Installation and Setup

### Prerequisites
Ensure you have the following installed:
- Python 3.x
- Yosys
- ABC
- Required Python libraries: `pandas`, `numpy`, `scikit-learn`, `xgboost`, `tensorflow`

### Steps to Install
1. Clone this repository:
   ```sh
   git clone https://github.com/PVSSukeerthi/GGH_round2.git
   cd GGH_round2
   ```
2. Install required Python libraries:
   ```sh
   pip install -r requirements.txt
   ```
3. Install **Yosys** and **ABC**:
   ```sh
   sudo apt-get install yosys
   ```
   ABC comes with Yosys, so no additional installation is needed.

4. Run the feature extraction script:
   ```sh
   python extract_features.py
   ```

5. Train the ML model:
   ```sh
   python train_model.py
   ```

6. Make predictions on new RTL files:
   ```sh
   python predict.py path/to/rtl_file.v
   ```

## Usage

### 1.Feature Extraction

To extract features from the Verilog designs:

1. Place your `.v` files in the `rtl_codes/` directory.

2. Run the `feature_generation.py` script:

   ```
   python feature_generation.py
   ```

   This script will process each Verilog file, invoke Yosys and ABC to extract relevant features, and save them to `yosys_features.csv`.

### 2.Data Augmentation

Since the dataset is relatively small, Generative Adversarial Networks (GANs) are used to create synthetic data:

- Open and run the `main.ipynb` notebook.
- The notebook includes sections that:
  - Load the extracted features.
  - Train a GAN to generate synthetic feature sets.
  - Save the augmented dataset to `synthetic_data.csv`.

### 3.Model Training and Evaluation

With the augmented dataset:

- Continue in the 

  ```
  main.ipynb
  ```

   notebook to:

  - Load the combined real and synthetic data.
  - Train machine learning models (e.g., XGBoost) to predict combinational logic depth.
  - Evaluate model performance using appropriate metri



## Results and Conclusion

- The **XGBoost model** provided the best accuracy.
- **GAN-generated data** improved model performance.
- The approach significantly reduces synthesis time, making it useful for early-stage timing analysis.

## References
- [Yosys Documentation](https://yosyshq.net/yosys/)
- [ABC Logic Synthesis Tool](https://people.eecs.berkeley.edu/~alanmi/abc/)
- [XGBoost Documentation](https://xgboost.readthedocs.io/)
