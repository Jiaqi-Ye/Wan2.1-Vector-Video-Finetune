import torch
from diffsynth import ModelManager, WanVideoPipeline, save_video

# 加载模型
model_manager = ModelManager(torch_dtype=torch.bfloat16, device="cuda")
model_manager.load_models([
    "models/Wan-AI/Wan2.1-T2V-1.3B/diffusion_pytorch_model.safetensors",
    "models/Wan-AI/Wan2.1-T2V-1.3B/models_t5_umt5-xxl-enc-bf16.pth",
    "models/Wan-AI/Wan2.1-T2V-1.3B/Wan2.1_VAE.pth",
])

# 加载 LoRA 微调权重（可选）
model_manager.load_lora("models/lightning_logs/version_1/checkpoints/epoch=0-step=500.ckpt", lora_alpha=1.5)

pipe = WanVideoPipeline.from_model_manager(model_manager, device="cuda")
pipe.enable_vram_management(num_persistent_param_in_dit=None)

# 生成视频
video = pipe(
    prompt=(
      "tigersticker_unique001, adorable tiger cub, surprised expression, small character, distant view, zoomed out, camera pulled back,full body in frame, whole character visible, mouth slightly open, raised eyebrows, fluffy fur, pure black eyes, no eye highlights, chibi cartoon style, centered composition, lots of negative space, clean white background, sticker style, emoji style, solo" 
            ),
    negative_prompt=(
        "cropped, out of frame, partial body, cut off, close-up, 色调艳丽，过曝，静态，细节模糊不清，字幕，风格，作品，画作，画面，静止，整体发灰，"
        "最差质量，低质量，JPEG压缩残留，丑陋的，残缺的，多余的手指，画得不好的手部，"
        "画得不好的脸部，畸形的，毁容的，形态畸形的肢体，手指融合，静止不动的画面，"
        "杂乱的背景，三条腿，背景人很多，倒着走"
    ),
    num_inference_steps=50,
    seed=0,
    height=640,
    width=512,
    tiled=False
)

save_video(video, "video.mp4", fps=30, quality=5)

