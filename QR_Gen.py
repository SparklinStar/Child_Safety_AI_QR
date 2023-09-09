from gradio_client import Client


  
def generate_qr_code(fileURL,positive_prompt,Seed):
    client = Client("https://huggingface-projects-qr-code-ai-art-generator--85d7mzwl6.hf.space/")
    result = client.predict(
        				fileURL,	# str  in 'QR Code Content' Textbox component
        				positive_prompt,	# str  in 'Prompt' Textbox component
        				'ugly, disfigured, low quality, blurry, nsfw',	# str  in 'Negative Prompt' Textbox component
        			    7.5,	# int | float (numeric value between 0.0 and 50.0) in 'Guidance Scale' Slider component
        				1.2,	# int | float (numeric value between 0.0 and 5.0) in 'Controlnet Conditioning Scale' Slider component
        				0.9,	# int | float (numeric value between 0.0 and 1.0) in 'Strength' Slider component
        				Seed,	# int | float (numeric value between -1 and 9999999999) in 'Seed' Slider component
        				"",	# str (filepath or URL to image) in 'Init Image (Optional). Leave blank to generate image with SD 2.1' Image component
        				"",	# str (filepath or URL to image) in 'QR Code Image (Optional). Leave blank to automatically generate QR code' Image component
        				True,	# bool  in 'Use QR code as init image' Checkbox component
        				'DPM++ Karras SDE',	# str (Option from: ['DPM++ Karras SDE', 'DPM++ Karras', 'Heun', 'Euler', 'DDIM', 'DEIS']) in 'Sampler' Dropdown component
        				fn_index=0
        )
    tmp = result
    return tmp
  # Get the image content from the result
  #image = Image.open(result)
