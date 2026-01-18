# Tiger Vector-Style Animation LoRA Model

The **Tiger LoRA Model** is a **LoRA fine-tuned model for Wan 2.1**, specifically designed to generate **high-quality anime-style tiger characters** with a vector animation aesthetic.  

It is fully compatible with **ComfyUI** and is hosted on **Hugging Face**.

---

## Notebook Overview

This notebook includes scripts for **Wan 2.1 1.3B T2I, T2V, and V2V reference testing**, as well as **vector-style video LoRA tuning**.  

You can refer to the official **LoRA Tuning.md** to learn how the script works, and you can also **train your own Wan 2.1 LoRA model** using the provided Google Colab notebook (`.py`) file.

---

## Model Details

- **Model Name:** Tiger LoRA Model  
- **Model Type:** LoRA  
- **Base Model:** Wan 2.1 – 1.3B  
- **Training Data:** 16 high-quality images of Kokomi with detailed annotations  
- **Optimized Features:** Orange, chubby tiger character  
- **Release Date:** 2026.01.18  
- **Hugging Face Repository:** [Kokomi LoRA Model on Hugging Face](https://huggingface.co/jye224/Kokomi)

---

## Getting Started

### Load the Model

#### Download from Hugging Face

You can download the model directly from Hugging Face here:  
[Kokomi LoRA Model on Hugging Face](https://huggingface.co/jye224/Kokomi)

---

## Kokomi Character Example

<p align="center">
<img src="example_dataset/train/09.png" width="600" />
</p>

---

## Sample Prompt

**Prompt Example:**  
`tigersticker_unique001, adorable tiger cub, fluffy fur, playful and dynamic pose, smiling, soft lighting, smooth animation style, cute cartoon style, centered composition, simple white background, solo`

<p align="center">
  <video src="https://raw.githubusercontent.com/Jiaqi-Ye/Wan2.1-Vector-Video-Finetune/945d54fec0db49034e0cbe5742c88e1971b04a8a/Example_Video/video1.mp4" width="300" controls></video>
  <video src="https://raw.githubusercontent.com/Jiaqi-Ye/Wan2.1-Vector-Video-Finetune/945d54fec0db49034e0cbe5742c88e1971b04a8a/Example_Video/video2.mp4" width="300" controls></video>
  <video src="https://raw.githubusercontent.com/Jiaqi-Ye/Wan2.1-Vector-Video-Finetune/945d54fec0db49034e0cbe5742c88e1971b04a8a/Example_Video/video3.mp4" width="300" controls></video>
</p>

