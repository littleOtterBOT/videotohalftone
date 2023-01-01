import cv2
import os
import halftone as ht
import glob
import moviepy.editor as mp
import tqdm

image_path = "path/to/images/"

#Capture every frames from video to images
def vidcap():
  vidcap = cv2.VideoCapture("ORIGINAL VIDEO NAME")
  global fcount
  fcount = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
  success,image = vidcap.read()
  for i in tqdm.tqdm (range(fcount), desc="Frame extracting..........."):
    cv2.imwrite(os.path.join(image_path ,"frame" + str(i).zfill(4) + ".jpg"), image)
    success,image = vidcap.read()

#Applying halftone effect to all frames
#Every parameter are explained at the original repo  https://github.com/philgyford/python-halftone
#Requires pillow in oder to work, use "pip install pillow" to install it.
def htgen():
  for i in tqdm.tqdm (range(fcount), desc="Applying halftone effect..."):
    filename = os.path.join(image_path ,"frame" + str(i).zfill(4) + ".jpg")
    h = ht.Halftone(filename)
    h.make(angles=[45],
      antialias=True,
      filename_addition="_halftone",
      output_format="jpeg",
      output_quality=95,
      percentage=0,
      sample=7,
      save_channels=False,
      save_channels_format="jpeg",
      save_channels_style="grayscale",
      scale=3,
      style="grayscale")

#Merge all frames to video
def framestovid():
  image_files = glob.glob(os.path.join(image_path, "frame*_halftone.jpg"))
  image_files.sort
  fps = 30
  global length
  image = cv2.imread(image_files[0])
  height, width, color = image.shape
  fourcc = cv2.VideoWriter_fourcc(*'mp4v')
  out = cv2.VideoWriter('Output.mp4', fourcc, fps, (width, height))
  for i in tqdm.tqdm (range(fcount), desc="Creating video............."):
      image = cv2.imread(os.path.join(image_path, image_files[i]))
      out.write(image)
  out.release()

#Combine video with an audio
def combine():
  audio = mp.AudioFileClip("YOUR AUDIO NAME")
  video = mp.VideoFileClip("Output.mp4")
  final_clip = video.set_audio(audio)
  final_clip.write_videofile("Output_with_audio.mp4")

if __name__ == "__main__":
  vidcap()
  htgen()
  framestovid()
  combine()