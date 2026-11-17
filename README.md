# Image Processing Tools from Scratch

PyQt desktop tools I built during my biomedical engineering degree, one task per folder. Most of the processing is written from scratch with NumPy.

## Try it online

These now run in the browser in [BioMed Lab](https://mohamed-halemo.github.io/biomed-lab/), no install needed:

| Task | What it does | Try it |
|---|---|---|
| Task 1 | Image and DICOM info: size, bit depth, header tags | [Inspector →](https://mohamed-halemo.github.io/biomed-lab/#/inspector) |
| Task 2 | Zoom with nearest-neighbour and bilinear interpolation | [Zoom →](https://mohamed-halemo.github.io/biomed-lab/#/zoom) |
| Task 3 | Histogram equalization | [Equalization →](https://mohamed-halemo.github.io/biomed-lab/#/equalization) |
| Task 4 + 7 | Unsharp masking, noise, denoising | [Filters →](https://mohamed-halemo.github.io/biomed-lab/#/filters) |
| Task 5 + 6 | Fourier magnitude/phase and frequency-domain filtering | [Fourier →](https://mohamed-halemo.github.io/biomed-lab/#/fourier) |
| Task 8 | CT back-projection on the Shepp-Logan phantom | [CT reconstruction →](https://mohamed-halemo.github.io/biomed-lab/#/ct) |
| Task 9 | Colour maps | [Colour maps →](https://mohamed-halemo.github.io/biomed-lab/#/colormap) |

## Run the desktop version

Each folder is a separate PyQt5 app:

```bash
cd Task3-Equalization
python main.py
```
