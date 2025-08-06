
# 🛣️ Road Segmentation with U-Net and Edge-Aware Loss
**Accurate Road Boundary Detection using CamVid Dataset and Edge-Weighted Training**

## 📌 Overview

This project presents a robust **road segmentation model** using the **U-Net architecture**, tailored for **autonomous vehicles and intelligent transport systems**. A major challenge in road segmentation is capturing **sharp, precise edges**, which are critical for tasks like lane following and obstacle avoidance.

To solve this, I implemented a novel **edge-aware loss function**, improving **IoU from 87% to 92%**, and significantly enhancing edge clarity, making the model more **reliable in real-world scenarios**.

## 🎯 Objectives

- Perform **binary road segmentation** using the CamVid dataset.
- Address boundary inaccuracies by introducing a **custom edge-weighted Binary Cross-Entropy loss**.
- Achieve high accuracy while improving **edge delineation** and **real-world generalizability**.

## 🧠 Model Architecture

The model is based on the **U-Net architecture**, known for its:
- Encoder–decoder structure
- Skip connections for fine-grained spatial details
- Excellent performance even with small datasets

Implemented **from scratch** using TensorFlow and Keras, the model:
- Takes 256×256 RGB images
- Outputs binary segmentation masks (road vs. non-road)

## 📊 Key Results

| Metric             | Without Edge Loss | With Edge Loss |
|-------------------|-------------------|----------------|
| Training Accuracy | 0.97              | 0.98           |
| Validation Accuracy| 0.96             | 0.97           |
| Test Accuracy     | 0.96              | 0.97           |
| IoU (Mean)        | 0.87              | **0.92**       |

🟢 Significant improvement in **boundary sharpness and continuity**, especially visible in real-world samples.

## 🔍 Method Highlights

- **Edge-Aware Loss**: Used Canny edge detection on ground truth masks to generate weight maps.
- **Weight Map**: Edge pixels were given weight = 5, others = 1, to enforce boundary precision.
- **Evaluation**: Quantitative (Accuracy, IoU, Confusion Matrix) and qualitative (visual predictions).

## 📁 Dataset

### 1. **CamVid Dataset**
- Used for training and validation
- Preprocessing: resizing, normalization, and binary mask conversion (road vs. not-road)

### 2. **Self-Captured Images**
- Used for qualitative testing
- Helped identify edge prediction limitations

### ⚠️ Dataset Access:
Due to size limitations, the dataset is not included in this repository. 

👉 [Download CamVid Dataset](https://drive.google.com/file/d/1nfUiaZ_e_HReJEdrD6Ivl5_80k2eLInH/view?usp=sharing)
## 🧪 Installation & Usage

### ✅ Requirements
Install dependencies:

```bash
pip install -r requirements.txt
```

(You can also run this project easily on **Google Colab**.)


## 🖥️ Directory Structure

```
road-segmentation-project/
├── download_dataset.py                             # Dataset download
├── Road_segmentation_project.ipynb                 # Jupyter notebooks
├── research_paper_unet_road_segmentation.pdf       # Research paper
├── requirements.txt
├── LICENSE
└── README.md
```

## 📸 Sample Outputs

| Original Image | Ground Truth | Prediction (Edge-Aware) |
|----------------|--------------|--------------------------|
| ![img1](outputs/sample1.png) | ![gt1](outputs/gt1.png) | ![pred1](outputs/pred1.png) |

*(Add your own sample images above)*

## 💡 Future Work

- Extend to **multi-class segmentation** (sidewalks, lanes, vehicles)
- Integrate with **real-time embedded systems**
- Experiment with advanced models: **DeepLabv3+, SegFormer**

## 🤝 Acknowledgments

- 👨‍🏫 **Dr. Sandeep Singh Sandha** (Ph.D. in AI, UCLA) for mentorship under *Punjab AI Excellence*
- 📚 Open-source communities and forums for ongoing support
- 🏫 Faculty of Khalsa College, Amritsar

## 📜 License

This project is licensed under the [MIT License](LICENSE).
