# VideoToHalftone
## Applying halftone filter to a video.

The software is fairly straightforward. It extracts frames from video files and applies filters frame by frame. Reassemble it into a single video file.

- Making use of a modified version of [python-halftone](https://github.com/philgyford/python-halftone) by [philgyford](https://github.com/philgyford) with grayscale halftone inverted from white dot to black dot instead.
- Every halftone parameter is identical to the original! All choices are detailed on the [repo](https://github.com/philgyford/python-halftone).
- I built this application just to produce a halftone version of Bad Apple!! This has just 6751 frames. You may also need to adjust the zfill() value to match your frame counts. (I'd do it later if I had the time.)
- Optimization would not be performed right now because I am a python rookie and am considering taking some time to learn Python more.
