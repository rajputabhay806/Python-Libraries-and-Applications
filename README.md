# Python Labsheet Solutions

This project organizes the completed working examples from the uploaded **Python Labsheet.pdf**.

## Folder structure
- `Labsheet 1 - NumPy/` — Q1–Q28
- `Labsheet 2 - Pandas/` — Q1–Q33 and the merit-list challenge
- `Labsheet 4 - TensorFlow/` — Q1–Q15
- `Labsheet 5 - OpenCV/` — Q1–Q15
- `Labsheet 3` was not present in the supplied PDF, so no questions were invented for it.

Each question is a separate Python file, as required by the PDF. The scripts include comments and print/display results where appropriate.

## Setup
Use Python 3.10 or 3.11 for the broadest compatibility with the listed libraries.

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
python -m pip install -r requirements.txt
```

Some tasks require optional local inputs:
- OpenCV image tasks: put an image named `sample.jpg` in the same question folder, or change `IMAGE_PATH`.
- Webcam tasks require a connected camera.
- TensorFlow scripts may take longer and some tasks need internet access only if downloading/installing packages or datasets.
- `plot_model()` may require Graphviz and the Python `pydot` package.

Run an individual task from its folder, for example:
```bash
python "Q01_multiples_of_7.py"
```

## Notes
- Results involving random data vary between runs.
- TensorFlow model training is kept intentionally small for lab demonstrations.
- For Lab Sheet 2, the DataFrame values follow the PDF's provided sample data.
