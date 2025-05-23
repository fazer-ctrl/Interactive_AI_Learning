Machine Learning Examples with scikit-learn
This repository contains various machine learning examples using scikit-learn, focusing on Decision Trees and Support Vector Machines (SVM).
Examples Included

Basic Decision Tree Classification (decision_tree_basic.py)

Simple binary classification example
Demonstrates decision tree prediction and probability estimation
Uses scikit-learn's built-in dataset


Decision Tree Structure Analysis (decision_tree_structure.py)

Detailed analysis of decision tree internal structure
Visualization of decision paths
Uses iris dataset


Decision Tree Criterion Comparison (decision_tree_criteria.py)

Compares different splitting criteria (gini, entropy, log_loss)
Analyzes feature importance
Performance metrics visualization


SVM Multi-class Classification (svm_multiclass.py)

Demonstrates one-vs-one and one-vs-rest approaches
Shows different decision function shapes
Simple numerical example


SVM Kernel Comparison (svm_kernels.py)

Compares different SVM kernels (linear, RBF, polynomial)
Visualizes decision boundaries
Uses iris dataset



Installation

Create and activate a virtual environment (recommended):

bashCopypython -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

Install required packages:

bashCopypip install -r requirements.txt
Requirements
See requirements.txt for detailed package requirements. Main dependencies:
Copynumpy>=1.21.0
scipy>=1.7.0
scikit-learn>=1.0.0
matplotlib>=3.4.0
Usage
Each example can be run independently:
bashCopypython decision_tree_basic.py
python decision_tree_structure.py
python decision_tree_criteria.py
python svm_multiclass.py
python svm_kernels.py
Output

Decision Tree examples will generate:

Text output showing tree structure
Visualizations of the decision tree
Performance metrics where applicable


SVM examples will generate:

Decision boundary visualizations
Classification metrics
Model comparison plots



Notes

Some examples may take longer to run depending on dataset size and model complexity
Visualizations require a working display or proper backend configuration
Random state is set in some examples for reproducibility

License
This code is licensed under the BSD 3-Clause License. See LICENSE file for details.
Credits

Original code examples from scikit-learn documentation
Comments and explanations created through collaboration between Claude (Anthropic) and the user