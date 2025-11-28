
# CNN Tank Classification using VGG19

This project classifies images of **two tank types** (tank 1 and tank 2) using a CNN built on **VGG19 transfer learning**.

---

## 📁 Dataset Structure

Organize your data as:

data/
└── Train/
  ├── tank 1/
  └── tank 2/

---

## 🧠 Model Summary

* Base: **VGG19** (ImageNet, include_top=False)
* Input: **224×224×3**
* Added layers: GAP → Dense → BatchNorm → Dropout → Softmax (2 classes)
* Optimizer: **Adam (lr=0.001)**
* Loss: **Categorical Crossentropy**

---

## 🔄 Data Augmentation

* Rotation 15°, shift 10%, shear 20%, zoom 20%
* Horizontal flip, brightness (0.8–1.2)
* Class balancing: tank 1 ×5, tank 2 ×2

---

## 🏋️ Training

* Epochs: **56**
* Batch size: **64**
* Callbacks: EarlyStopping, ModelCheckpoint
* Plots: Accuracy & loss curves

---

## 📈 Evaluation

* Classification report
* Confusion matrix
* ROC-AUC
* Training/validation curves

---

## 🛠 Installation

Run:

pip install -r requirements.txt

---

## ▶️ Usage

1. Place dataset in the required folder structure.
2. Open and run: **Tank_CNN_VGG19.ipynb**
3. Train → Evaluate → Visualize

---

## 📦 Dependencies

See `requirements.txt` (TensorFlow, NumPy, Matplotlib, scikit-learn, Pillow, OpenCV).

---

## 🏁 Summary

A complete pipeline for classifying **tank 1 vs tank 2** using transfer learning, strong augmentation, and full performance evaluation.

---
