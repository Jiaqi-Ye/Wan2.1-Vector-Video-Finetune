# Controllable Vector Video Generation via Wan 2.1 Fine-Tuning

**Jun. 2025 – Present**  
Research Assistant, Prof. XXXX  
University of Wisconsin–Madison

This repository presents a **parameter-efficient framework for controllable vector-style video generation** by fine-tuning **Wan 2.1 (1.3B)** video diffusion models using **LoRA**.  
Our goal is to enable **prompt-controllable, temporally consistent vector animations** under **limited GPU memory constraints**, making stylized video generation feasible on consumer-grade hardware.

---

## Overview

- **Base Model**: Wan 2.1 (1.3B) video diffusion model  
- **Framework**: DiffSynth-Studio  
- **Fine-Tuning**: Low-Rank Adaptation (LoRA)  
- **Tasks**: Text-to-Image (T2I), Text-to-Video (T2V), Video-to-Video (V2V)  
- **Focus**: Vector-style animation, shape consistency, controllable motion  

---

## Key Contributions

- Fine-tuned **Wan 2.1 video diffusion models** for high-quality **vector-stylized animation generation**.
- Enabled **text-prompt–controllable vector animations**, supporting flexible semantic and stylistic control.
- Introduced a **layer-wise vector animation strategy** to decouple shape, color, and motion.
- Improved **temporal consistency by ~25%** compared to baseline Wan 2.1 generation.
- Demonstrated effective **LoRA fine-tuning under 8–16 GB VRAM constraints**.

---

## Method Summary

We build upon **DiffSynth-Studio** and apply **LoRA-based fine-tuning** to Wan 2.1 by adapting only attention and feed-forward submodules:

- Target modules: `q, k, v, o, ffn.0, ffn.2`
- Mixed precision training with `bfloat16`
- Gradient checkpointing enabled

To stabilize stylized video generation, we introduce **layer-wise vector supervision**, which improves shape preservation and reduces temporal drift across frames.

---

## Training Setup

**Dataset**
- 16 high-quality vector-style tiger images  
- Transparent background with dense semantic tagging  
- Resolution: 512 × 512  

**LoRA Configuration**
- Rank: 16  
- Alpha: 16  
- Learning rate: 5e-5  
- Steps per epoch: 500  
- Epochs: 5  

---

## Experimental Insights

- **Wan 2.1 (1.3B)** provides the best trade-off between quality and memory efficiency.
- **LoRA rank = 4** leads to insufficient style learning.
- **LoRA rank = 16** significantly improves character identity and vector-style consistency.
- Wan 2.2 (5B) exceeds the feasible memory limit on 8 GB GPUs and results in OOM during inference.

---

## Tiger Vector LoRA Model

The **Tiger Vector LoRA Model** is a LoRA adapter fine-tuned on **Wan 2.1**, designed for generating **stylized tiger characters with clean vector outlines and stable motion**.

- **Model Type**: LoRA Adapter  
- **Base Model**: Wan 2.1 – 1.3B  
- **Optimized For**: vector-style animation  
- **Release Date**: 2026-01-18  

**Hugging Face**:  
[Kokomi Lora Model on Hugging Face](https://huggingface.co/jye224/Kokomi)

---

## Example Prompt

