# neural-network-ground-0

Welcome to **neural-network-ground-0**! This repository tracks my journey of building and understanding deep learning models completely from the ground up (from "ground zero"). 

The implementation avoids high-level abstractions like TensorFlow, Keras, or PyTorch, focusing instead on raw mathematics, logic, and fundamental matrix operations using **Python** and **NumPy**.

## 📺 Tutorial Reference
This project is built step-by-step following the excellent [Neural Networks From Scratch YouTube Playlist](https://youtube.com/playlist?list=PLQVvvaa0QuDcjD5BAw2DxE6OF2tius3V3&si=4yiidQdEKAYAvi9D) by **Harrison Kinsley (sentdex)** and the accompanying *NNFS* textbook.

---

## 🚀 Concepts Covered & Implemented

- **The Basic Neuron:** Input handling, weights, biases, and the dot product.
- **Layer Architecture:** Implementing dense (fully-connected) layers capable of handling batches of data.
- **Activation Functions:** - `ReLU` (Rectified Linear Unit) for hidden layers.
  - `Softmax` for generating probability distributions in the output layer.
- **Loss Calculation:** Implementing `Categorical Cross-Entropy` loss to measure network performance.
- **Backpropagation:** Computing gradients via the chain rule to understand exactly how a network learns.
- **Optimization:** Gradient Descent, Stochastic Gradient Descent (SGD), Adam, and learning rate decay.

---

## 🛠️ Tech Stack & Requirements

- **Python 3.x**
- **NumPy** (for optimized matrix calculations)
- **Matplotlib** (for data visualization and testing with datasets like the Spiral Dataset)

To get started, clone the repository and install the minimal dependencies:

```bash
git clone [https://github.com/vatssavvya/neural-network-ground-0.git](https://github.com/vatssavvya/neural-network-ground-0.git)
cd neural-network-ground-0
pip install numpy matplotlib
```
