
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
|<img width="375" height="396" alt="Screenshot 2025-08-06 184151" src="https://github.com/user-attachments/assets/3ed132ba-85a4-4698-b1fa-51eef8de7046" /> | <img width="374" height="397" alt="Screenshot 2025-08-06 184219" src="https://github.com/user-attachments/assets/5b16c34f-ed6b-4e92-b0ef-ffda0822ecbe" /> | <img width="379" height="397" alt="Screenshot 2025-08-06 184237" src="https://github.com/user-attachments/assets/545c029e-5340-438d-b12c-1c7da3bbd938" />|

<img width="1456" height="495" alt="self_click_2" src="https://github.com/user-attachments/assets/34d07f4e-6c77-4855-bc49-046cbb162001" />

<img width="1460" height="499" alt="self_click_1" src="https://github.com/user-attachments/assets/54130e5c-b0f4-4d63-8a28-0d109a1224ac" />


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
