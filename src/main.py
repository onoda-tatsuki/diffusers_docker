import uuid
import os
import time
from diffusers import StableDiffusionPipeline
import torch

start_time = time.time()

# モデルの指定
pipe = StableDiffusionPipeline.from_pretrained(
    "admruul/anything-v3.0",
    torch_dtyoe=torch.float16,
    use_auth_token=""
    # モデルのversion指定のオプション存在しないとエラーになる
    # variant="fp16",
    # use_safetensors=True
)

# # # デバイスの指定。mpsはM1/M2 Macを指す。
pipe = pipe.to("cpu")

pipe.enable_attention_slicing()
prompt = "best quality masterpiece 1girl maid"

# # # modelのウォームアップ。Macの場合は必要 1.3.3のみ
image = pipe(prompt, num_inference_steps=1)

# # 処理の実行
image = pipe(prompt).images[0]

end_time = time.time()
elapsed_time = end_time - start_time
print(f"Execution time: {elapsed_time} seconds")

image.show()

output_dir = "./outputs"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

image.save(f"{output_dir}/{uuid.uuid4()}.png")

print("pipeline connection")