import json
from urllib import request

#This is the ComfyUI api prompt format.

#If you want it for a specific workflow you can "enable dev mode options"
#in the settings of the UI (gear beside the "Queue Size: ") this will enable
#a button on the UI to save workflows in api format.

#keep in mind ComfyUI is pre alpha software so this format will change a bit.

#this is the one for the default workflow
prompt_text = """
{
  "4": {
    "inputs": {
      "ckpt_name": "sd_xl_base_1.0.safetensors"
    },
    "class_type": "CheckpointLoaderSimple",
    "_meta": {
      "title": "Load Checkpoint - BASE"
    }
  },
  "5": {
    "inputs": {
      "width": 1024,
      "height": 1024,
      "batch_size": 1
    },
    "class_type": "EmptyLatentImage",
    "_meta": {
      "title": "Empty Latent Image"
    }
  },
  "6": {
    "inputs": {
      "text": "evening sunset scenery blue sky nature, glass bottle with a galaxy in it",
      "clip": [
        "4",
        1
      ]
    },
    "class_type": "CLIPTextEncode",
    "_meta": {
      "title": "CLIP Text Encode (Prompt)"
    }
  },
  "7": {
    "inputs": {
      "text": "text, watermark",
      "clip": [
        "4",
        1
      ]
    },
    "class_type": "CLIPTextEncode",
    "_meta": {
      "title": "CLIP Text Encode (Prompt)"
    }
  },
  "10": {
    "inputs": {
      "add_noise": "enable",
      "noise_seed": 11747843166881,
      "steps": 25,
      "cfg": 8,
      "sampler_name": "euler",
      "scheduler": "normal",
      "start_at_step": 0,
      "end_at_step": 20,
      "return_with_leftover_noise": "enable",
      "model": [
        "4",
        0
      ],
      "positive": [
        "6",
        0
      ],
      "negative": [
        "7",
        0
      ],
      "latent_image": [
        "5",
        0
      ]
    },
    "class_type": "KSamplerAdvanced",
    "_meta": {
      "title": "KSampler (Advanced) - BASE"
    }
  },
  "11": {
    "inputs": {
      "add_noise": "disable",
      "noise_seed": 0,
      "steps": 25,
      "cfg": 8,
      "sampler_name": "euler",
      "scheduler": "normal",
      "start_at_step": 20,
      "end_at_step": 10000,
      "return_with_leftover_noise": "disable",
      "model": [
        "12",
        0
      ],
      "positive": [
        "15",
        0
      ],
      "negative": [
        "16",
        0
      ],
      "latent_image": [
        "10",
        0
      ]
    },
    "class_type": "KSamplerAdvanced",
    "_meta": {
      "title": "KSampler (Advanced) - REFINER"
    }
  },
  "12": {
    "inputs": {
      "ckpt_name": "sd_xl_refiner_1.0.safetensors"
    },
    "class_type": "CheckpointLoaderSimple",
    "_meta": {
      "title": "Load Checkpoint - REFINER"
    }
  },
  "15": {
    "inputs": {
      "text": "evening sunset scenery blue sky nature, glass bottle with a galaxy in it",
      "clip": [
        "12",
        1
      ]
    },
    "class_type": "CLIPTextEncode",
    "_meta": {
      "title": "CLIP Text Encode (Prompt)"
    }
  },
  "16": {
    "inputs": {
      "text": "text, watermark",
      "clip": [
        "12",
        1
      ]
    },
    "class_type": "CLIPTextEncode",
    "_meta": {
      "title": "CLIP Text Encode (Prompt)"
    }
  },
  "17": {
    "inputs": {
      "samples": [
        "11",
        0
      ],
      "vae": [
        "12",
        2
      ]
    },
    "class_type": "VAEDecode",
    "_meta": {
      "title": "VAE Decode"
    }
  },
  "19": {
    "inputs": {
      "filename_prefix": "ComfyUI",
      "images": [
        "17",
        0
      ]
    },
    "class_type": "SaveImage",
    "_meta": {
      "title": "Save Image"
    }
  }
}
"""

def queue_prompt(prompt):
    p = {"prompt": prompt}
    data = json.dumps(p).encode('utf-8')
    req =  request.Request("http://127.0.0.1:8000/prompt", data=data)
    request.urlopen(req)


prompt = json.loads(prompt_text)

prompt["6"]["inputs"]["text"] = "evening sunset scenery blue sky nature, glass bottle with a galaxy in it"
prompt["7"]["inputs"]["text"] = "text, watermark"

prompt["5"]["inputs"]["batch_siz"] = 1

prompt["19"]["inputs"]["filename_prefix"] = "ApiTest/Test33"




queue_prompt(prompt)


